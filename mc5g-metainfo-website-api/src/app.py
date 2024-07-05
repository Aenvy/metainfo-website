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
from metainfo import Artefact, ProdInfo, Releases
from stats import Stats
from packages import PackagesApi


# Note on mongoDB request cache.
# It is handled in ansible-metainfo-collection/plugins/module_utils/mongo_metainfo.py
# Each time a request is made, it is cached, and if the exact same request is being made
# there is no call on mongoDB.
# The cache is generic for all kind of requests.
# Clearing the cache will clear the whole cache.
# So clearing it often enough is enough to make sure no page will get stuck with old data.
#
# Cache is still useful for less-than-fully-optimized hierarchical searches,
# where we could be looking for the same metainfo several times.
# Also for some pages like stats, which is very long to generate, the cache will speed up
# things tremendously when refreshing the page.
#
# Also the cach uses a TTL (Time To Live) meaning a cache clear request is ignored for a
# few minutes after the last one, default value is in the mongo.clear_cache method
# it is 300s, ie 5 minutes.
#
# That should be enough to keep the benefits of the cache while not having an outdated
# website with obsolete data.

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
    Releases(mongo).routes()
    PackagesApi(mongo).routes()
    # Static routes (serving static files, like pure HTMLM, CSS, JS, etc.)
    StaticRoutes()
    # Other routes
    Stats(mongo)
    # Launching the app
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=port, server='waitress')  # , server='bjoern')
