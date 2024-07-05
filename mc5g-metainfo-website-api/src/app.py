#!/usr/bin/python3
#
# Copyright (c) 2021 Hewlett-Packard Enterprise Development LP.
# All Rights Reserved.
#
# This software is the confidential and proprietary information of
# Hewlett-Packard Enterprise Development LP.
#
# Bottle API for metainfo manipulation
import sys
import bottle
from module_utils.mongo_metainfo import MongoMetainfo
from static import StaticRoutes
from metainfo import Artefact, ProdInfo
from stats import Stats
from packages import PackagesApi


if __name__ == '__main__':
    def intargv(n, default):
        try:
            return int(sys.argv[n])
        except (IndexError, ValueError):
            return default
    port = intargv(1, 18080)
    mongo = MongoMetainfo(
        "cmsgvm05.gre.hpecorp.net",
        "cms5gciuser",
        "cms5gciuser",
        "metainfo",
        None,
        True,
    )
    # artefact.mongo = mongo
    # Standard modules routes
    for collection in ["sol", "prod", "comp", "result", "test", "quality", "caas"]:
        Artefact(mongo, collection).routes()
    ProdInfo(mongo).routes()
    PackagesApi(mongo).routes()
    # Static routes (serving static files, like pure HTMLM, CSS, JS, etc.)
    StaticRoutes()
    # Other routes
    Stats(mongo)
    # Launching the app
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=port, server='waitress')  # , server='bjoern')
