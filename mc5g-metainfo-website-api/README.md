# 5G metainfo API
This does 2 things:
- Provide a JSON API for getting metainfos
- Provide some basic HTML pages for browsing through hierarchical mateinfos

## Requirements
This is based upon a WSGI application using the `bottle` framework, with the `waitress` server, and the classes from `Ansible Metainfo Collection` (`AMC`).
`MongoDB` connection uses the `mongo_metainfo.py` module from `AMC`.
`ansible` module is required for the parameters handling in `AMC`, even as it is not currently used for the code parts we need.

### Providing the `module_utils`
It needs to be available in `src/ansible_collections/hpe/metainfo/plugins/module_utils`
Creating links for ansible metainfo collection, on the mc5g-metainfo-website-api directory.
The ansible metainfo collection is available alongside mc5g-metainfo-website.
- `ansible-metainfo-collection`
 - `plugins/module_utils`
- `mc5g-metainfo-website`
 - `mc5g-metainfo-website-api`
  - `src`
   - `module_utils` -> `../../../ansible-metainfo-collection/plugins/module_utils/`
   - `ansible_collections/hpe/metainfo/plugins/`
    - `module_utils` -> `../../../../module_utils`

Creating everything from the `mc5g-metainfo-website-api` directory:
```
mkdir -p src/ansible_collections/hpe/metainfo/plugins/
ln -s ../../../../module_utils src/ansible_collections/hpe/metainfo/plugins/
ln -s ../../../ansible-metainfo-collection/plugins/module_utils/ src/
```

### Creating the python environment
Using a Python Virtual Environment
```
mkdir -p venv
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install bottle ansible requests pymongo pystache waitress
```

## Starting the API
Here using the Python virtual environment
```
cd mc5g-metainfo-website-api
source ./venv/bin/activate
cd src/
python3 app.py
```

# Codebase
## The bottle App
Created by `app.py`, this will load all other modules and create the routes.
- A `metainfo.Artefact` set of routes for all listed `collections`
- The `ProdInfo` routes for the specific `product_info` collection
- Routes from `packages.PackagesAPI` for packages
- Some static routes
- The statistics pages

## `api.Api` metaclass
Defines a set of standard routes for metainfo API.
With generic methods to be overloaded.

The basic principle is to call `add_route(routing, backend)` for each kind of route.
- routing is a standard WSGI routing expression, like:
```
/solutions/<artifactId:re:[-a-z0-9]+>/<version:re:\d+(.\d+)*-\d{8,12}(-\d+)?>
```
- backend is a suffix name for method called, for example a GET request will call the `self.get_backend()` method
-> If a method called `get_backend_html()` exists, another route is created using the routing suffixed with '.html', and this method as backend.

When initialization is being done, the app will output the routing rules and the backend method name in stderr, for debugging, and reference, purposes.
eg: `GET:/solutions/versions/bystatus#get_versions_bystatus`

## Artefact classes
Based on meta-class `api.Api`, this will call `add_route()` with all standard routes for a metainfo collection.
```
self.artifactId = r'<artifactId:re:[-a-z0-9]+>'
self.version = r'<version:re:\d+(.\d+)*-\d{8,12}(-\d+)?>'
self.add_route(f"/{self.module}/{self.artifactId}/{self.version}", "metainfo")
```
This will create the following route, for `module=products`, with `get_metainfo(artifactId, version)` as backend method:
`/products/<artifactId:re:[-a-z0-9]+>/<version:re:\d+(.\d+)*-\d{8,12}(-\d+)?>`
Also, since the `get_metainfo_html(artifactId, version)` exists, this route will be added:
`/products/<artifactId:re:[-a-z0-9]+>/<version:re:\d+(.\d+)*-\d{8,12}(-\d+)?>.html`

To create for example a POST route at the same place, there is only need to write a `post_metainfo(artifactId, version)` method, and it will be called on POST requests there.

Usually, for simpler codebase, both `get_backend()` and `get_backend_html()` method will call on a `_backend()` method that will collect the datas, and each final method will present the same data in its own way.
For example `_metainfo()` is the method that will call the ansible collection's `Artefact.ArteFactory` class to generate an `Artefact` object for the metainfo requested.
Then `get_metainfo()` will `render()` the Artefact into JSON and return it directly, whereas `get_metainfo_html()` will do a lot more work, using a template file etc.

## The ProdInfo class
it is a simplification upon a standard Artefact class, restricting the routes to its minimum necessary.

## The packages API
That one is still somewhat incomplete or buggy, it is also based on `api.Api` metaclass.

## Static routes
The static.StaticRoutes class is used for non-API routes, it will serve any file inside the `static/` directory.
The files are loaded and prepared on App startup, and are then served directly from memory.
So do not use this for large files, it is ok for simple HTML like the `index.html` file, and some CSS, JS or images.
Currently only an index.html file present.
This module is blazing fast for static files.

## Templates
The `static.templates()` method is used for static templating.
Why it is on the `static` module is a mystery.

This method has one argument, the name of a `.html` file inside the `templates/` directory, for example `metainfo` for `templates/metainfo.html`.
All other arguments are named and used for the templating.
This templating is extremely basic, and uses no templating engine, only the Python's `str.format()` method, replacing all named parameters with their values.
For example `{something}` will be replaced by `kwargs['something']`.
If `kwargs` doesn't have `something` in it, this'll crash, but if it has an unused `otherthing` it won't matter.

Since `{something}` is the `str.format()` special syntax for templating, CSS standard notation using a lot of `{` and `}` breaks everything.
Hence they need to be doubled, like that: `#hierarchy {{display:grid;}}`

As for static routes, the files are loaded at the start of the WSGI app, and never after, all being served from memory.
This means that it is not possible to tweak the files on the fly for development purposes, you always need to stop/start the server.

Those templates files are only used for html pages, therefore have absolutely no usefulness for the API in itself!

Usage example, using the `metainfo` template with several parameters:
```
templates(
  "metainfo",
  title=repr(metainfo),
  subtitle=Artefact.versions_href(self.collection, artifactId, html=True),
  children=children,
  parents=parents,
  packages=pkgs,
  results=results,
  iframe_src=Artefact.ident_url(**metainfo.ident()),
  d=datetime.today()-d,
)
```

## The statistics page
This module creates two routes : `/stats` and `/stats.html`
They are non-static content for a static route.
This generates a lot of statistics for all metainfos inside the mongoDb database, and takes quite some time.
It takes one optional GET parameter: `discarded`
If it is present, statistics will include Discarded packages, else it won't.
The pages takes around 20s to be generated, and 40s with Discarded packages.

Just go and look at the page to see its content.
The HTML version is full of links to various parts of the API, with some filters, etc.
It allows for a nice global view of what exists, and to delve into the depths of what lies beneath the mongoDb database.
