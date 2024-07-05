#!/usr/bin/python3
#
# Copyright (c) 2021 Hewlett-Packard Enterprise Development LP.
# All Rights Reserved.
#
# This software is the confidential and proprietary information of
# Hewlett-Packard Enterprise Development LP.
#
# Bottle API for metainfo manipulation
from datetime import timedelta
import bottle
from api import Api
from metainfo import Artefact
from static import templates
from module_utils.artefacts.status import Status
from module_utils.artefacts.packages import Packages


class PackagesApi(Api):
    module = "packages"
    backend = "packages"
    repository = r'<repository:re:(docker|yum|helm|raw)>'

    def init(self, mongo):
        self.mongo = mongo

    def routes(self):
        self.add_route(f"/{self.module}/{self.repository}/<name>", self.backend)
        self.add_route(f"/{self.module}/{self.repository}/<name>/<version>", self.backend)

    def _packages_parents(self, repository, name=None, version=None):
        """Finds Artefacts referencing this package
        Returns them grouped by collection : {sol: {Solution, ...}, prod: {Product, ...}, ...}
        """
        filters = {}
        if repository == "raw" and version:
            name = f"{name}/{version}"
            version = None
        if name:
            filters[f"packages.{repository}.{'path' if repository == 'raw' else 'name'}"] = name
        if version:
            filters[f"packages.{repository}.{'tag' if repository == 'docker' else 'version'}"] = (
                {'$regex': version} if '*' in version else version
            )
        if bottle.request.params.get('discarded', False):
            query = {'status': {'$ne': str(Status.DISCARDED)}}
        else:
            query = None
        return {
            collection: [
                Artefact.artefact_from_metainfo(metainfo)
                for metainfo in self.mongo.find_artefact(
                    collection=collection,
                    filters=filters,
                    query=query,
                )
            ]
            for collection in ['sol', 'prod', 'comp', 'test', 'result', 'quality', 'caas']
        }

    def _packages_info(self, repository, name=None, version=None):
        parents = self._packages_parents(repository, name, version)
        packages = [
            (pkg, pkg.get_status_event())
            for collection, metainfos in parents.items()
            for artefact in metainfos
            for pkg in Packages.list_artefact_packages(artefact)
            if pkg.repo_type == repository
            and pkg.nexus_name == name
            and pkg.nexus_version == version
        ]
        return {
            "parents": parents,
            "packages": {p.reload_as_asset() for p in set(p[0] for p in packages)},
            "events": [p[1] for p in packages],
        }

    def get_packages(self, repository, name=None, version=None):
        infos = self._packages_info(repository, name, version)
        return {
            "package": list({pkg.apiurl for pkg in infos['packages']}),
            "events": [str(e) for e in infos['events']],
            **{
                collection: [
                    Artefact.ident_url(**parent.summary())
                    for parent in parents
                ]
                for collection, parents in infos['parents'].items()
            }
        }

    def get_packages_html(self, repository, name=None, version=None):
        if repository == "raw" and version:
            name = f"{name}/{version}"
            version = None
        infos = self._packages_info(repository, name, version)
        asset = nexus_url = downloaded_after_discard = latest_download = latest_discard = None
        if infos['packages']:
            asset = infos['packages'].pop()
            nexus_url = asset.apiurl
            latest_discard = asset.discarded
            latest_download = getattr(asset, 'lastDownloaded', 0)
            if latest_download and latest_discard:
                downloaded_after_discard = latest_download > latest_discard

        r = []
        for collection, module in Artefact.modules.items():
            parents = infos['parents'].get(collection, [])
            if parents:
                r += [
                    "<div>",
                    f"<h3>{module.capitalize()}</h3>",
                    "<ul>",
                    *[f" <li>{Artefact.ident_href(**parent.summary())}</li>" for parent in parents],
                    "</ul>",
                    "</div>",
                ]
        r += [
            "<div>",
            "<h3>Events</h3>",
            "<ul>",
            *[f" <li>{event}</li>" for event in infos['events']],
            "</ul>",
            "</div>",
        ]
        return templates(
            name=self.module,
            title=f"{self.module.capitalize()} cms5g-{repository} {name or ''} {version or ''}",
            error_class="alert" if downloaded_after_discard else "none",
            error_text=(
                f"Package was downloaded after being Discarded !<br>"
                f"lastDownloaded={latest_download} Discarded={latest_discard}"
                f" : {timedelta(seconds=latest_download-latest_discard)}"
                if downloaded_after_discard else ""
            ),
            subtitle=f"<a href='{nexus_url}'>{repr(asset)}</a>",
            content="\n".join(r),
            iframe_src=nexus_url,
            d=self.elapsed(),
        )
