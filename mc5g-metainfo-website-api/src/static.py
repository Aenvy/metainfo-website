#!/usr/bin/python3
import glob
import os
import sys
from datetime import datetime
import bottle


def debug(msg, category="INFO"):
    sys.stderr.write(f"{datetime.today()} [{category}] {msg}\n")


####
# Static routing and f-string templating from files
#
class StaticRoutes():
    path = 'static'
    errors = []

    def __init__(self):
        self.files = {
            name: (content, len(content), self.content_type(name))
            for (name, content) in [
                self.readfile(path)
                for path in glob.glob(f'{self.path}/*')
            ]
            if name
        }
        errors = "\n".join(self.errors)
        self.files['errors'] = (errors, len(errors), self.content_type("errors.txt"))
        for file in self.files:
            debug(f'GET:/{file}', "ROUTE")
            bottle.route(f'/{file}', 'GET', self.get, name=file)
        debug('GET:/ (index.html)', "ROUTE")
        bottle.route('/', 'GET', self.get, name="index.html")

    def get(self):
        if(not os.path.exists(f"{self.path}/{bottle.request.route.name}")
           or bottle.request.route.name.endswith('js')):
            content, size, ctype = self.files[bottle.request.route.name]
        else:
            with open(f"{self.path}/{bottle.request.route.name}", 'rb') as f:
                content = f.read()
                ctype = self.content_type(bottle.request.route.name)
                size = len(content)
        bottle.response.set_header('Content-Type', ctype)
        bottle.response.add_header('Content-Length', size)
        return content

    def readfile(self, path):
        try:
            with open(path, 'rb') as f:
                return (os.path.basename(path), f.read())
        except (FileNotFoundError, TypeError, PermissionError) as e:
            self.errors.append(str(e))
            return None, None

    def content_type(self, name):
        return {
            "html": "text/html",
            "txt": "text/plain",
            "json": "application/json",
            "js": "application/javascript",
            "css": "text/css",
            "jpg": "image/jpg",
            "png": "image/png",
            "bry": "application/python",
            "py": "application/python",
        }.get(os.path.splitext(name)[1][1:], "text/plain")


def templates(name=None, **kwargs):
    if not name or not hasattr(templates, 'files'):
        def readfile(path):
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    return (os.path.basename(path), f.read())
            except (FileNotFoundError, TypeError, PermissionError):
                return None, None
        templates.files = {
            name: content
            for (name, content) in (readfile(path) for path in glob.glob('templates/*'))
            if name
        }
    return templates.files.get(
        name,
        templates.files.get(f"{name}.html", "")
    ).format(name=name, **kwargs) if name else None
