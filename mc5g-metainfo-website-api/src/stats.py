#!/usr/bin/python3
#
# Copyright (c) 2021 Hewlett-Packard Enterprise Development LP.
# All Rights Reserved.
#
# This software is the confidential and proprietary information of
# Hewlett-Packard Enterprise Development LP.
#
# Bottle API for metainfo manipulation
from datetime import datetime
import bottle
from module_utils.artefacts.version import Version
from module_utils.artefacts.status import Status
from static import templates
from metainfo import Artefact, sorted_status


class Stats():
    def __init__(self, mongo):
        self.mongo = mongo
        bottle.route('/stats', 'GET', self.stats)
        bottle.route('/stats.html', 'GET', self.stats_html)

    def stats(self):
        query = None if bottle.request.params.get('discarded', False) \
            else {'status': {'$ne': str(Status.DISCARDED)}}
        # {sol: {version: status, version: status, ...}, prod: {v:s, ...}, ...}
        all_data = {
            collection: {
                (Version(ver['ident']['version']), ver['ident']['artifactId']):
                ver.get('status', str(Status.UNKNOWN))
                for ver in self.mongo.find_artefact(
                    collection=collection,
                    filters={'ident.version': {'$not': {'$regex': "SNAPSHOT"}}},
                    query=query,
                    projection={'_id': 0, 'ident': 1, 'status': 1},
                )
            }
            for collection in ['sol', 'prod', 'comp', 'test', 'result', 'quality', 'caas']
        }
        years = sorted(set(y[0].date[:4] for x in all_data.values() for y in x.keys()))
        # {2020: {sol: {status: nb, s:nb, ...}, prod: {s:n, ...}, ...}, 2021...}
        r = {year: {} for year in years}
        for collection in all_data:
            for (version, _), status in all_data[collection].items():
                year = r[version.date[:4]]
                if collection not in year:
                    year[collection] = {}
                if status not in year[collection]:
                    year[collection][status] = 1
                else:
                    year[collection][status] += 1
        return r

    def stats_html(self):
        d = datetime.today()
        data = self.stats()
        status = sorted_status(set().union(*(
            set(data[year][collection].keys())
            for year in data
            for collection in data[year]
        )))
        headers = "<tr><th>Year</th><th>Collection</th><th>" + "</th><th>".join(
            str(x) for x in status
        ) + "</th></tr>"
        table = []
        for year in data:
            table.append(headers)
            table.append(f"<tr><th rowspan={len(data[year])+1}>{year}<th></tr>")
            for collection in data[year]:
                table.append(f"<tr><th>{collection}</th><td>" + "</td><td>".join(
                    Artefact.versions_href(
                        collection,
                        version=f"-{year}",
                        status=s,
                        html=True,
                        text=data[year][collection].get(s, "")
                    )
                    for s in status
                ) + "</td></tr>")
            table.append("</tr>")
        return templates(
            "stats.html",
            table="\n".join(table),
            d=datetime.today() - d,
        )
