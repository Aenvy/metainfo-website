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
from datetime import datetime
import bottle
from api import Api
from static import templates
from module_utils.artefacts.artefact import ArteFactory
from module_utils.artefacts.status import Status
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
        return self._metainfo(artifactId, version).render()

    def get_metainfo_html(self, artifactId, version):
        d = datetime.today()
        metainfo = self._metainfo(artifactId, version)
        children = "\n".join(
            f"<li><a href='{Artefact.ident_url(**c.ident())}.html'>{c}</a></li>"
            for c in sorted(metainfo.get_all_children())
        )
        discarded = bottle.request.params.get('discarded', False)
        parents = "\n".join(
            f"<li><a href='{Artefact.ident_url(**p.ident())}.html'>{p}</a></li>"
            for p in sorted(metainfo.get_all_parents())
            if discarded or p.status != Status.DISCARDED
        )
        pkgs = "\n".join(
            f"<li><a href='{Artefact.package_url(p.repo_type, p.nexus_name, p.nexus_version)}.html'>{repr(p)}</a></li>"
            for p in Packages.list_artefact_packages(metainfo)
        )
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
            d=datetime.today() - d,
        )

    # Backend versions and versions_bystatus
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
        result = self._versions(artifactId, versions)
        return {
            status: [version.base() for version, ident in result if ident['status'] == status]
            for status in sorted_status((x['status'] for _, x in result), reverse=True)
        }

    # Backend general
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
        return (self.mongo.find(
            self.collection,
            query={'metainfo': artifactId[:-5] if artifactId.endswith('-prod') else artifactId},
        ) or [{}])[0]
