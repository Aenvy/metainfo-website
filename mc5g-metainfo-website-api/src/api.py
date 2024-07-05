#!/usr/bin/python3
from datetime import datetime
import bottle
from static import debug, templates


class Api():
    module = "api"
    backend = ""

    def __init__(self, *args, **kwargs):
        self.__d = datetime.today()
        self.init(*args, **kwargs)

    def init(self, *args, **kwargs):
        pass

    def elapsed(self):
        return datetime.today() - self.__d

    def routes(self):
        self.add_route(f"/{self.module}", self.backend)

    def add_route(self, routing, backend):
        for action in ('get', 'put', 'post', 'delete'):
            if hasattr(self, f'{action}_{backend}_html'):
                debug(f'{action.upper()}:{routing}.html#{action}_{backend}_html', "ROUTE")
                bottle.route(f"{routing}.html", action.upper(), getattr(self, f'{action}_{backend}_html'))
            if hasattr(self, f'{action}_{backend}'):
                debug(f'{action.upper()}:{routing}#{action}_{backend}', "ROUTE")
                bottle.route(routing, action.upper(), getattr(self, f'{action}_{backend}'))

    def _default(self, method, **kwargs):
        return templates(
            name=self.module,
            method=method,
            path=bottle.request.route.rule,
            d=self.elapsed(),
            **kwargs)

    def get_(self, **kwargs):
        return self._default("GET")

    def post_(self, **kwargs):
        return self._default("POST")

    def put_(self, **kwargs):
        return self._default("PUT")

    def delete_(self, **kwargs):
        return self._default("DELETE")
