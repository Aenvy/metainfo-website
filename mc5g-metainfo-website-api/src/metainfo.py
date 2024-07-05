#!/usr/bin/python3
#
# Copyright (c) 2021 Hewlett-Packard Enterprise Development LP.
# All Rights Reserved.
#
# This software is the confidential and proprietary information of
# Hewlett-Packard Enterprise Development LP.
#
# Metainfo classes
import sys
import json
import requests
from datetime import datetime
import bottle
from api import Api
from static import templates
from module_utils.artefacts.artefact import ArteFactory
from module_utils.artefacts.status import Status, min_status
from module_utils.artefacts.version import Version
from module_utils.artefacts.packages import Packages


def debug(msg, category="INFO"):
    sys.stderr.write(f"{datetime.today()} [{category}] {msg}\n")


def sorted_status(status, reverse=False):
    return [x[1] for x in sorted(((Status.create(s).value, s) for s in status), reverse=reverse)]

####
# Generic Artefact handling
#
class Artefact(Api):
    mongo = None
    collection = None
    modules = {
        "sol": 'solutions',
        "prod": 'products',
        "comp": 'components',
        "result": 'results',
        "test": 'tests',
        "quality": 'quality',
        "caas": 'caas',
        "prod_info": 'prodinfo',
    }
    # Regexp definitions for routage variables
    artifactId = r'<artifactId:re:[-a-z0-9]+>'
    version = r'<version:re:\d+(.\d+)*-\d{8,12}(-\d+)?>'
    versions = r'<versions:re:[-.\d*]*[-\d*]>'

    def init(self, mongo, collection=None):
        self.mongo = mongo
        if collection:
            self.collection = collection
        if not self.collection:
            raise ValueError("'collection' is required for Artefact classes")
        self.module = self.modules.get(self.collection, self.collection)

    def routes(self):
        backend = "general"
        self.add_route(f"/{self.module}", backend)
        backend = "metainfo"
        self.add_route(f"/{self.module}/{self.artifactId}/{self.version}", backend)
        backend = "recursive"
        self.add_route(f"/{self.module}/{self.artifactId}/{self.version}/recursive", backend)
        if self.module == "solutions":
            backend = "inventory"
            self.add_route(f"/{self.module}/{self.artifactId}/{self.version}/inventory", backend)
            self.add_route(f"/{self.module}/{self.artifactId}/{self.version}/inventory.<ext:re:url|yml>", backend)
        backend = "versions_bystatus"
        self.add_route(f"/{self.module}/{self.artifactId}/versions/bystatus/{self.versions}", backend)
        self.add_route(f"/{self.module}/{self.artifactId}/versions/bystatus", backend)
        self.add_route(f"/{self.module}/versions/bystatus/{self.versions}", backend)
        self.add_route(f"/{self.module}/versions/bystatus", backend)
        backend = "versions"
        self.add_route(f"/{self.module}/{self.artifactId}/versions/{self.versions}", backend)
        self.add_route(f"/{self.module}/{self.artifactId}/versions", backend)
        self.add_route(f"/{self.module}/versions/{self.versions}", backend)
        self.add_route(f"/{self.module}/versions", backend)

    @classmethod
    def ident_url(cls, groupId, artifactId, version, **kwargs):
        module = cls.modules.get(groupId.split('.')[4])
        return f"/{module}/{artifactId}/{Version(version).base()}"

    @classmethod
    def ident_href(cls, groupId, artifactId, version, **kwargs):
        return f"""
<a href="{Artefact.ident_url(groupId, artifactId, version, **kwargs)}{kwargs.get('html', True) and '.html' or ''}">{artifactId}@{version}#{kwargs.get('status')}</a>"""

    @classmethod
    def package_url(cls, repository, name, version=None, tag=None, **kwargs):
        version = f"/{version or tag}" if (version or tag) else ""
        return f"/packages/{repository}/{name}{version}"

    @classmethod
    def versions_url(cls, collection, artifactId=None, version=None, status=None, html=False, bystatus=False):
        module = cls.modules.get(collection, collection)
        artifactId = f"/{artifactId}" if artifactId else ""
        bystatus = '/bystatus' if bystatus else ''
        html = '.html' if html else ''
        status = f"?status={status.replace(' ', '%20')}" if status else ""
        version = f"/{Version(version).base()}" if version else ""
        return f"/{module}{artifactId}/versions{bystatus}{version}{html}{status}"

    @classmethod
    def versions_href(cls, collection, artifactId=None, version=None, status=None, html=False, bystatus=False, text=False):
        url = cls.versions_url(collection, artifactId, version, status, html, bystatus)
        return f"""<a href="{url}">{url if text is False else text}</a>"""

    # Backend metainfo
    # Return one metainfo, possibly recursively
    # Needs to be updated fast, mongo cache is therefore cleared
    # But only do it on JSON API request, not on HTML (the HTML page calls the JSON one anyway)
    @classmethod
    def artefact_from_metainfo(cls, metainfo, **kwargs):
        """Creates an Artefact object from a metainfo dict"""
        arteclass = ArteFactory.get_class_from_ident(metainfo.get('ident', {}).get('groupId', ""))
        artefact = arteclass(
            autoload=False,
            **kwargs
        )
        artefact.prepare_metainfo(metainfo)
        return artefact

    def _metainfo(self, artifactId, version):
        return ArteFactory(
            groupId=f'com.hpe.cms.5g.{self.collection}.*',
            artifactId=artifactId,
            version=version,
            force_load_from_db=True,
            load_all=False,
            load_discarded=True,
            autoload=True,
            get_latest=True,
            load_deps=True,
            mongo=self.mongo,
        )

    def get_metainfo(self, artifactId, version):
        self.mongo.clear_cache()
        return self._metainfo(artifactId, version).render()

    def _recursive_metainfos(self, artifactId, version):
        metainfo = self._metainfo(artifactId, version)
        children = metainfo.get_all_children()
        discarded = bottle.request.params.get('discarded', False)
        parents = [
            p
            for p in sorted(metainfo.get_all_parents())
            if discarded or p.status != Status.DISCARDED
        ]
        return metainfo, children, parents

    def get_metainfo_html(self, artifactId, version):
        d = datetime.today()
        metainfo, children, parents = self._recursive_metainfos(artifactId, version)
        children = "\n".join(
            f"<li><a href='{Artefact.ident_url(**c.ident())}.html'>{c}</a></li>"
            for c in sorted(children)
        )
        parents = "\n".join(
            f"<li><a href='{Artefact.ident_url(**p.ident())}.html'>{p}</a></li>"
            for p in sorted(parents)
        )
        pkgs = "\n".join(
            f"<li><a href='{Artefact.package_url(p.repo_type, p.nexus_name, p.nexus_version)}.html'>{repr(p)}</a></li>"
            for p in Packages.list_artefact_packages(metainfo)
        )
        discarded = bottle.request.params.get('discarded', False)
        results = "\n".join(
            f"<li><a href='{Artefact.ident_url(**r.ident())}.html'>{r}</a></li>"
            for r in sorted(metainfo.get_all_results())
            if discarded or r.status != Status.DISCARDED
        )
        return templates(
            "metainfo",
            title=repr(metainfo),
            subtitle=Artefact.versions_href(self.collection, artifactId, html=True),
            children=children,
            parents=parents,
            packages=pkgs,
            results=results,
            iframe_src=Artefact.ident_url(**metainfo.ident()),
            recursive_url=Artefact.ident_url(**metainfo.ident()) + "/recursive",
            inventory_url=self._inventory_url(artifactId, version),
            d=datetime.today() - d,
        )

    def get_recursive(self, artifactId, version):
        self.mongo.clear_cache()
        metainfo, children, parents = self._recursive_metainfos(artifactId, version)
        return {
            "metainfo": metainfo.render(),
            "children": {
                name: [
                    c.render()
                    for c in children
                    if c.__class__.__name__ == name
                ]
                for name in {_.__class__.__name__ for _ in children}
            },
            "parents": {
                name: [
                    p.render()
                    for p in parents
                    if p.__class__.__name__ == name
                ]
                for name in {_.__class__.__name__ for _ in parents}
            },
        }

    def _inventory_url(self, artifactId, version):
        solution = self._metainfo(artifactId, version)
        result = sorted(
            r
            for r in solution.get_all_results()
            if hasattr(r.metainfo, "inventory")
        )[-1:]
        return result[0].metainfo.inventory if result else ""

    def get_inventory(self, artifactId, version, ext=False):
        url = self._inventory_url(artifactId, version)
        if not url:
            return ""
        if ext=="url":
            return url
        r = requests.get(url, verify="/etc/pki/tls/cert.pem")
        if not ext:
            for name, value in r.headers.items():
                bottle.response.add_header(name, value)
        return r.text

    # Backend versions and versions_bystatus
    # Lists all versions, needs to be updated on new arrivals
    # Hence mongo cache is cleared. Again, only on JSON calls.
    def _versions(self, artifactId, versions, filters=None, query=None):
        filters = filters or {}
        query = query or {}
        if artifactId:
            filters["ident.artifactId"] = artifactId
        if versions:
            filters["ident.version"] = {'$regex': versions.replace("*", ".*")}
        if 'status' in bottle.request.params:
            if Status.create(bottle.request.params['status']) == Status.UNKNOWN:
                query['status'] = None
            else:
                query['status'] = bottle.request.params['status']
        else:
            query.update({'status': {'$ne': str(Status.DISCARDED)}})
        return [
            (version, {
                "groupId": ident[0],
                "artifactId": ident[1],
                "version": ident[2],
                "status": ident[3],
            })
            for version, ident in sorted(set(
                (Version(ver['ident']['version']), (
                    ver['ident']['groupId'],
                    ver['ident']['artifactId'],
                    ver['ident']['version'],
                    ver.get('status', str(Status.UNKNOWN)),
                ))
                for ver in self.mongo.find_artefact(
                    self.collection,
                    filters,
                    query,
                    projection={'_id': 0, 'ident': 1, 'status': 1},
                )
            ), reverse=True)
        ]

    def get_versions(self, artifactId=None, versions='*'):
        self.mongo.clear_cache()
        bottle.response.content_type = 'application/json'
        return json.dumps([
            version.base()
            for (version, ident) in self._versions(artifactId, versions)
        ])

    def get_versions_html(self, artifactId=None, versions='*'):
        d = datetime.today()
        return templates(
            "versions.html",
            versions="</li>\n<li>".join((
                Artefact.ident_href(**ident)
                for version, ident in self._versions(artifactId, versions)
            )),
            d=datetime.today() - d,
        )

    def get_versions_bystatus(self, artifactId=None, versions='*'):
        self.mongo.clear_cache()
        result = self._versions(artifactId, versions)
        return {
            status: [version.base() for version, ident in result if ident['status'] == status]
            for status in sorted_status((x['status'] for _, x in result), reverse=True)
        }

    # Backend general
    # To get generic informations about a collection: list of name and artifactIds
    # This moves slowly, hence it doesn't require mongo cache cleared here
    def _general(self):
        whitelist = bottle.request.params.get('whitelist', True)
        if self.collection == "prod" and whitelist:
            return self._prod_general()
        return (self.mongo.find_artefact(
            self.collection,
            None,
            None,
            {"_id": 0, "name": 1, "ident": 1},
            self.collection,
            {"$group": {"_id": "$ident.artifactId", "metainfo": {"$last": "$$ROOT"}}},
            {"$replaceRoot": {"newRoot": "$metainfo"}},
        )) or []

    def _prod_general(self):
        return [
            {"name": prod['name'], "ident": prod['prod']}
            for prod in self.mongo.find(
                "prod_info",
                {"prod.artifactId": {"$in": [x['artifactId'] for x in self.mongo.find("whli", {})]}},
                projection={"_id": 0, "name": 1, "prod": 1},
            )
        ] or []

    def get_general_html(self):
        d = datetime.today()
        return templates(
            "versions.html",
            versions="</li>\n<li>".join((
                Artefact.ident_href(**e['ident'])
                for e in self._general()
            )),
            d=datetime.today() - d,
        )

    def get_general(self):
        bottle.response.content_type = 'application/json'
        return json.dumps(self._general())


class ProdInfo(Artefact):
    collection = "prod_info"

    def routes(self):
        self.add_route(f"/{self.module}/{self.artifactId}", "prodinfo")

    # Backend prodinfo
    def get_prodinfo(self, artifactId):
        # Moves slowly, don't clear mongo cache here
        return (self.mongo.find(
            self.collection,
            query={'metainfo': artifactId[:-5] if artifactId.endswith('-prod') else artifactId},
        ) or [{}])[0]


# Branches names after feature/patch/release:
#  MC5G(-optional)-1.aamm.[01X]
#  [optional] is something like 5G-EIR, AUSF, HSS-IWF, NAFPM, NFMF, NRF, PGW, UDM, UDR, UDSF
#  Regexp for optional is [A-Z-_0-9]+
#  Example: MC5G-UDSF-1.2112.X
# Tags are very similar:
#  MC5G(-optional)-1.aamm(.[01X] or -RC[0-9] or .[01X]-RC[0-9])
#  Except for stuff like MC5G-1.2306.0-Phenix1
#   or MC5G-1.2406.0-RC1.1
#   or MC5G-CIHSS-05.00.00
#   or MC5G-Internal-23.3.0
#   or TO_NOT_DELETE
# So regexp matching is very hard, and validation is made on code
# And we may want to look for MC5G-*-1.2403*
# Since this is called often, and moves slowly: do not clear mongo cache automatically here!
class Releases(Artefact):
    collection = "sol"
    rc = r'<rc:re:\d\.\d{4}\.\d-.*>'

    def routes(self):
        # Note the absence of "/" between release and <tag>
        # This is done to catch both
        self.add_route("/releases", "releases")
        self.add_route("/releases/<tag>", "releases")

    # Backend releases
    def _tagged_metainfo(self, collection, tag="", rc=True):
        # Removes leading MC5G-
        # This allows looking for MC5G-1.2406 and finding MC5G-AUSF-1.2406
        if tag.startswith("MC5G-"):
            tag = tag[5:]
        query = {'$or': [{'tags': {'$regex': tag}}, {'ident.branch': {'$regex': tag}}]} \
            if tag else {'tags': {'$nin': [None, [], ""]}}
        query['status'] = {'$nin': min_status('RC')}
        if not rc:
            query['status']['$nin'].append('RC')
        return (
            Artefact.artefact_from_metainfo(m, mongo=self.mongo, load_all=False)
            for m in self.mongo.find(collection, query)
        )

    def get_releases(self, tag=""):
        rc = bottle.request.params.get('rc', False)
        # All relevant Solutions should be RC, we need to include that...
        rcsol = self._tagged_metainfo("sol", tag=tag, rc=True)
        prods = {
            f"{p.groupId}/{p.artifactId}/{p.version.base()}": p
            for p in self._tagged_metainfo("prod", tag=tag, rc=rc)
        }
        r = {
            f"{sol.metainfo.name} [{tag.replace('MC5G-', '')}]": {
                'version': sol.version.base(),
                'artifactId': sol.artifactId,
                'groupId': sol.groupId,
                'metainfo': sol.render(),
                'products': {
                    f"{prod.metainfo.name} [{tag.replace('MC5G-', '')}]": {
                        'version': prod.version.base(),
                        'artifactId': prod.artifactId,
                        'groupId': prod.groupId,
                        'metainfo': prod.render(),
                    }
                    for pident, prod in prods.items()
                    if pident in prodident
                    and tag in prod.metainfo.tags
                }
            }
            for sol in rcsol
            for tag in sol.metainfo.tags
            for prodident in [{
                f"{p.groupId}/{p.artifactId}/{Version(p.version).base()}"
                for p in sol.metainfo.products
            }]
        }
        # Filtering when Products list is empty
        # Useful when RC is False, it'll remove all Solutions which are only RC
        return {k: v for k, v in r.items() if v['products']}
