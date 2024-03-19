from reprlib import repr as limitedRepr


import enum
try:
    from ansible.module_utils.schema.definitions import *
except ImportError:
    from module_utils.schema.definitions import *


try:
    from ansible.module_utils.schema.metainfobase import MetainfoBase
except ImportError:
    from module_utils.schema.metainfobase import MetainfoBase

class ComponentSchema(MetainfoBase):
    """
    The component schema describes a component.
    """
    class _deps:



            _types_map = {
                'build': {'type': list, 'subtype': identifier},
                'runtime': {'type': list, 'subtype': identifier},
            }
            _formats_map = {
            }
            _validations_map = {
                'build': { 'required': False,},
                'runtime': { 'required': False,},
            }

            def __init__(self
                    , build=None
                    , runtime=None
                    ):
                """
                :param build: An explanation about the purpose of this instance.
                :param runtime: An explanation about the purpose of this instance.
                """
                self.__build = build
                self.__runtime = runtime
                pass

            def _get_build(self):
                return self.__build
            def _set_build(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("build must be list")
                if value is not None and  not all(isinstance(i, identifier) for i in value):
                    raise TypeError("build list values must be identifier")

                self.__build = value
            build = property(_get_build, _set_build)
            """
            An explanation about the purpose of this instance.
            """

            def _get_runtime(self):
                return self.__runtime
            def _set_runtime(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("runtime must be list")
                if value is not None and  not all(isinstance(i, identifier) for i in value):
                    raise TypeError("runtime list values must be identifier")

                self.__runtime = value
            runtime = property(_get_runtime, _set_runtime)
            """
            An explanation about the purpose of this instance.
            """


            @staticmethod
            def from_dict(d):
                v = {}
                if "build" in d:
                    v["build"] = [identifier.from_dict(p) if hasattr(identifier, 'from_dict') else p for p in d["build"]]
                if "runtime" in d:
                    v["runtime"] = [identifier.from_dict(p) if hasattr(identifier, 'from_dict') else p for p in d["runtime"]]
                return ComponentSchema._deps(**v)


            def as_dict(self):
                d = {}
                if self.__build is not None:
                    d['build'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__build]
                if self.__runtime is not None:
                    d['runtime'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__runtime]
                return d

            def __repr__(self):
                return "<Class _deps. build: {}, runtime: {}>".format(limitedRepr(self.__build[:20] if isinstance(self.__build, bytes) else self.__build), limitedRepr(self.__runtime[:20] if isinstance(self.__runtime, bytes) else self.__runtime))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'ident': {'type': identifier, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'history': {'type': list, 'subtype': event},
        'tags': {'type': list, 'subtype': str},
        'status': {'type': str, 'subtype': None},
        'shared': {'type': bool, 'subtype': None},
        'repositories': {'type': repositories, 'subtype': None},
        'scm': {'type': scm, 'subtype': None},
        'packages': {'type': packages, 'subtype': None},
        'deps': {'type': _deps, 'subtype': None},
        'quality': {'type': identifier, 'subtype': None},
        'results': {'type': list, 'subtype': identifier},
    }
    _formats_map = {
    }
    _validations_map = {
        'schema': { 'required': False,},
        'ident': { 'required': True,},
        'name': { 'required': True,},
        'description': { 'required': True,},
        'history': { 'required': False,},
        'tags': { 'required': False,},
        'status': { 'required': True,},
        'shared': { 'required': False,},
        'repositories': { 'required': True,},
        'scm': { 'required': False,},
        'packages': { 'required': False,},
        'deps': { 'required': False,},
        'quality': { 'required': False,},
        'results': { 'required': False,},
    }

    def __init__(self
            , *args
            , schema=None
            , ident=None
            , name=None
            , description=None
            , history=None
            , tags=None
            , status='CT Ready'
            , shared=None
            , repositories=None
            , scm=None
            , packages=None
            , deps=None
            , quality=None
            , results=None
            , **kwargs
            ):
        """
        :param shared: Use it when the packages of an artifact are shared between several repository
        :param results: Test Results associated with this Component
        """
        self.__schema = schema
        self.__ident = ident
        self.__name = name
        self.__description = description
        self.__history = history
        self.__tags = tags
        self.__status = status
        self.__shared = shared
        self.__repositories = repositories
        self.__scm = scm
        self.__packages = packages
        self.__deps = deps
        self.__quality = quality
        self.__results = results
        super().__init__(*args, **kwargs)
        pass

    def _get_schema(self):
        return self.__schema
    def _set_schema(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("schema must be str")

        self.__schema = value
    schema = property(_get_schema, _set_schema)

    def _get_ident(self):
        return self.__ident
    def _set_ident(self, value):
        if  not isinstance(value, identifier):
            raise TypeError("ident must be identifier")

        self.__ident = value
    ident = property(_get_ident, _set_ident)

    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if  not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value
    name = property(_get_name, _set_name)

    def _get_description(self):
        return self.__description
    def _set_description(self, value):
        if  not isinstance(value, str):
            raise TypeError("description must be str")

        self.__description = value
    description = property(_get_description, _set_description)

    def _get_history(self):
        return self.__history
    def _set_history(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("history must be list")
        if value is not None and  not all(isinstance(i, event) for i in value):
            raise TypeError("history list values must be event")

        self.__history = value
    history = property(_get_history, _set_history)

    def _get_tags(self):
        return self.__tags
    def _set_tags(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("tags must be list")
        if value is not None and  not all(isinstance(i, str) for i in value):
            raise TypeError("tags list values must be str")

        self.__tags = value
    tags = property(_get_tags, _set_tags)

    def _get_status(self):
        return self.__status
    def _set_status(self, value):
        if  not isinstance(value, str):
            raise TypeError("status must be str")

        self.__status = value
    status = property(_get_status, _set_status)

    def _get_shared(self):
        return self.__shared
    def _set_shared(self, value):
        if value is not None and  not isinstance(value, bool):
            raise TypeError("shared must be bool")

        self.__shared = value
    shared = property(_get_shared, _set_shared)
    """
    Use it when the packages of an artifact are shared between several repository
    """

    def _get_repositories(self):
        return self.__repositories
    def _set_repositories(self, value):
        if  not isinstance(value, repositories):
            raise TypeError("repositories must be repositories")

        self.__repositories = value
    repositories = property(_get_repositories, _set_repositories)

    def _get_scm(self):
        return self.__scm
    def _set_scm(self, value):
        if value is not None and  not isinstance(value, scm):
            raise TypeError("scm must be scm")

        self.__scm = value
    scm = property(_get_scm, _set_scm)

    def _get_packages(self):
        return self.__packages
    def _set_packages(self, value):
        if value is not None and  not isinstance(value, packages):
            raise TypeError("packages must be packages")

        self.__packages = value
    packages = property(_get_packages, _set_packages)

    def _get_deps(self):
        return self.__deps
    def _set_deps(self, value):
        if value is not None and  not isinstance(value, ComponentSchema._deps):
            raise TypeError("deps must be ComponentSchema._deps")

        self.__deps = value
    deps = property(_get_deps, _set_deps)

    def _get_quality(self):
        return self.__quality
    def _set_quality(self, value):
        if value is not None and  not isinstance(value, identifier):
            raise TypeError("quality must be identifier")

        self.__quality = value
    quality = property(_get_quality, _set_quality)

    def _get_results(self):
        return self.__results
    def _set_results(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("results must be list")
        if value is not None and  not all(isinstance(i, identifier) for i in value):
            raise TypeError("results list values must be identifier")

        self.__results = value
    results = property(_get_results, _set_results)
    """
    Test Results associated with this Component
    """


    @staticmethod
    def from_dict(d):
        v = d.copy()
        if "schema" in d:
            v["schema"] = str.from_dict(d["schema"]) if hasattr(str, 'from_dict') else d["schema"]
        if "ident" in d:
            v["ident"] = identifier.from_dict(d["ident"]) if hasattr(identifier, 'from_dict') else d["ident"]
        if "name" in d:
            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
        if "description" in d:
            v["description"] = str.from_dict(d["description"]) if hasattr(str, 'from_dict') else d["description"]
        if "history" in d:
            v["history"] = [event.from_dict(p) if hasattr(event, 'from_dict') else p for p in d["history"]]
        if "tags" in d:
            v["tags"] = [str.from_dict(p) if hasattr(str, 'from_dict') else p for p in d["tags"]]
        if "status" in d:
            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
        if "shared" in d:
            v["shared"] = bool.from_dict(d["shared"]) if hasattr(bool, 'from_dict') else d["shared"]
        if "repositories" in d:
            v["repositories"] = repositories.from_dict(d["repositories"]) if hasattr(repositories, 'from_dict') else d["repositories"]
        if "scm" in d:
            v["scm"] = scm.from_dict(d["scm"]) if hasattr(scm, 'from_dict') else d["scm"]
        if "packages" in d:
            v["packages"] = packages.from_dict(d["packages"]) if hasattr(packages, 'from_dict') else d["packages"]
        if "deps" in d:
            v["deps"] = ComponentSchema._deps.from_dict(d["deps"]) if hasattr(ComponentSchema._deps, 'from_dict') else d["deps"]
        if "quality" in d:
            v["quality"] = identifier.from_dict(d["quality"]) if hasattr(identifier, 'from_dict') else d["quality"]
        if "results" in d:
            v["results"] = [identifier.from_dict(p) if hasattr(identifier, 'from_dict') else p for p in d["results"]]
        return ComponentSchema(**v)


    def as_dict(self):
        d = super().as_dict()
        if self.__schema is not None:
            d['schema'] = self.__schema.as_dict() if hasattr(self.__schema, 'as_dict') else self.__schema
        if self.__ident is not None:
            d['ident'] = self.__ident.as_dict() if hasattr(self.__ident, 'as_dict') else self.__ident
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__description is not None:
            d['description'] = self.__description.as_dict() if hasattr(self.__description, 'as_dict') else self.__description
        if self.__history is not None:
            d['history'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__history]
        if self.__tags is not None:
            d['tags'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__tags]
        if self.__status is not None:
            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
        if self.__shared is not None:
            d['shared'] = self.__shared.as_dict() if hasattr(self.__shared, 'as_dict') else self.__shared
        if self.__repositories is not None:
            d['repositories'] = self.__repositories.as_dict() if hasattr(self.__repositories, 'as_dict') else self.__repositories
        if self.__scm is not None:
            d['scm'] = self.__scm.as_dict() if hasattr(self.__scm, 'as_dict') else self.__scm
        if self.__packages is not None:
            d['packages'] = self.__packages.as_dict() if hasattr(self.__packages, 'as_dict') else self.__packages
        if self.__deps is not None:
            d['deps'] = self.__deps.as_dict() if hasattr(self.__deps, 'as_dict') else self.__deps
        if self.__quality is not None:
            d['quality'] = self.__quality.as_dict() if hasattr(self.__quality, 'as_dict') else self.__quality
        if self.__results is not None:
            d['results'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__results]
        return d

    def __repr__(self):
        return "<Class ComponentSchema. schema: {}, ident: {}, name: {}, description: {}, history: {}, tags: {}, status: {}, shared: {}, repositories: {}, scm: {}, packages: {}, deps: {}, quality: {}, results: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__ident[:20] if isinstance(self.__ident, bytes) else self.__ident), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__history[:20] if isinstance(self.__history, bytes) else self.__history), limitedRepr(self.__tags[:20] if isinstance(self.__tags, bytes) else self.__tags), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status), limitedRepr(self.__shared[:20] if isinstance(self.__shared, bytes) else self.__shared), limitedRepr(self.__repositories[:20] if isinstance(self.__repositories, bytes) else self.__repositories), limitedRepr(self.__scm[:20] if isinstance(self.__scm, bytes) else self.__scm), limitedRepr(self.__packages[:20] if isinstance(self.__packages, bytes) else self.__packages), limitedRepr(self.__deps[:20] if isinstance(self.__deps, bytes) else self.__deps), limitedRepr(self.__quality[:20] if isinstance(self.__quality, bytes) else self.__quality), limitedRepr(self.__results[:20] if isinstance(self.__results, bytes) else self.__results))

