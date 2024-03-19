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

class ProductSchema(MetainfoBase):
    """
    The root schema is the schema that comprises the entire JSON document.
    """
    class _release:
            """
            Contain all release-related informations
            """
            class _releaseNotes:
                    """
                    Release notes
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                        'uri': {'type': str, 'subtype': None},
                        'comment': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': True,},
                        'version': { 'required': True,},
                        'uri': { 'required': False,},
                        'comment': { 'required': False,},
                    }

                    def __init__(self
                            , name=None
                            , version=None
                            , uri=None
                            , comment=None
                            ):
                        self.__name = name
                        self.__version = version
                        self.__uri = uri
                        self.__comment = comment
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)

                    def _get_uri(self):
                        return self.__uri
                    def _set_uri(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("uri must be str")

                        self.__uri = value
                    uri = property(_get_uri, _set_uri)

                    def _get_comment(self):
                        return self.__comment
                    def _set_comment(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("comment must be str")

                        self.__comment = value
                    comment = property(_get_comment, _set_comment)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        if "uri" in d:
                            v["uri"] = str.from_dict(d["uri"]) if hasattr(str, 'from_dict') else d["uri"]
                        if "comment" in d:
                            v["comment"] = str.from_dict(d["comment"]) if hasattr(str, 'from_dict') else d["comment"]
                        return ProductSchema._release._releaseNotes(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        if self.__uri is not None:
                            d['uri'] = self.__uri.as_dict() if hasattr(self.__uri, 'as_dict') else self.__uri
                        if self.__comment is not None:
                            d['comment'] = self.__comment.as_dict() if hasattr(self.__comment, 'as_dict') else self.__comment
                        return d

                    def __repr__(self):
                        return "<Class _releaseNotes. name: {}, version: {}, uri: {}, comment: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__uri[:20] if isinstance(self.__uri, bytes) else self.__uri), limitedRepr(self.__comment[:20] if isinstance(self.__comment, bytes) else self.__comment))

            class _addons:
                    """
                    A Product AddOn
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'uri': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': True,},
                        'uri': { 'required': True,},
                    }

                    def __init__(self
                            , name=None
                            , uri=None
                            ):
                        self.__name = name
                        self.__uri = uri
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_uri(self):
                        return self.__uri
                    def _set_uri(self, value):
                        if  not isinstance(value, str):
                            raise TypeError("uri must be str")

                        self.__uri = value
                    uri = property(_get_uri, _set_uri)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "uri" in d:
                            v["uri"] = str.from_dict(d["uri"]) if hasattr(str, 'from_dict') else d["uri"]
                        return ProductSchema._release._addons(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__uri is not None:
                            d['uri'] = self.__uri.as_dict() if hasattr(self.__uri, 'as_dict') else self.__uri
                        return d

                    def __repr__(self):
                        return "<Class _addons. name: {}, uri: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__uri[:20] if isinstance(self.__uri, bytes) else self.__uri))

            class _docsets:
                    """
                    A Product DocSet
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'uri': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': True,},
                        'uri': { 'required': True,},
                    }

                    def __init__(self
                            , name=None
                            , uri=None
                            ):
                        self.__name = name
                        self.__uri = uri
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_uri(self):
                        return self.__uri
                    def _set_uri(self, value):
                        if  not isinstance(value, str):
                            raise TypeError("uri must be str")

                        self.__uri = value
                    uri = property(_get_uri, _set_uri)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "uri" in d:
                            v["uri"] = str.from_dict(d["uri"]) if hasattr(str, 'from_dict') else d["uri"]
                        return ProductSchema._release._docsets(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__uri is not None:
                            d['uri'] = self.__uri.as_dict() if hasattr(self.__uri, 'as_dict') else self.__uri
                        return d

                    def __repr__(self):
                        return "<Class _docsets. name: {}, uri: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__uri[:20] if isinstance(self.__uri, bytes) else self.__uri))




            _types_map = {
                'releaseNotes': {'type': _releaseNotes, 'subtype': None},
                'version': {'type': str, 'subtype': None},
                'sku': {'type': str, 'subtype': None},
                'addons': {'type': list, 'subtype': _addons},
                'docsets': {'type': list, 'subtype': _docsets},
            }
            _formats_map = {
            }
            _validations_map = {
                'releaseNotes': { 'required': False,},
                'version': { 'required': False,},
                'sku': { 'required': False,},
                'addons': { 'required': False,},
                'docsets': { 'required': False,},
            }

            def __init__(self
                    , releaseNotes=None
                    , version=None
                    , sku=None
                    , addons=None
                    , docsets=None
                    ):
                """
                :param releaseNotes: Release notes
                :param addons: List AddOns linked to the Product
                :param docsets: List DocSets linked to the Product
                """
                self.__releaseNotes = releaseNotes
                self.__version = version
                self.__sku = sku
                self.__addons = addons
                self.__docsets = docsets
                pass

            def _get_releaseNotes(self):
                return self.__releaseNotes
            def _set_releaseNotes(self, value):
                if value is not None and  not isinstance(value, ProductSchema._release._releaseNotes):
                    raise TypeError("releaseNotes must be ProductSchema._release._releaseNotes")

                self.__releaseNotes = value
            releaseNotes = property(_get_releaseNotes, _set_releaseNotes)
            """
            Release notes
            """

            def _get_version(self):
                return self.__version
            def _set_version(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("version must be str")

                self.__version = value
            version = property(_get_version, _set_version)

            def _get_sku(self):
                return self.__sku
            def _set_sku(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("sku must be str")

                self.__sku = value
            sku = property(_get_sku, _set_sku)

            def _get_addons(self):
                return self.__addons
            def _set_addons(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("addons must be list")
                if value is not None and  not all(isinstance(i, ProductSchema._release._addons) for i in value):
                    raise TypeError("addons list values must be ProductSchema._release._addons")

                self.__addons = value
            addons = property(_get_addons, _set_addons)
            """
            List AddOns linked to the Product
            """

            def _get_docsets(self):
                return self.__docsets
            def _set_docsets(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("docsets must be list")
                if value is not None and  not all(isinstance(i, ProductSchema._release._docsets) for i in value):
                    raise TypeError("docsets list values must be ProductSchema._release._docsets")

                self.__docsets = value
            docsets = property(_get_docsets, _set_docsets)
            """
            List DocSets linked to the Product
            """


            @staticmethod
            def from_dict(d):
                v = {}
                if "releaseNotes" in d:
                    v["releaseNotes"] = ProductSchema._release._releaseNotes.from_dict(d["releaseNotes"]) if hasattr(ProductSchema._release._releaseNotes, 'from_dict') else d["releaseNotes"]
                if "version" in d:
                    v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                if "sku" in d:
                    v["sku"] = str.from_dict(d["sku"]) if hasattr(str, 'from_dict') else d["sku"]
                if "addons" in d:
                    v["addons"] = [ProductSchema._release._addons.from_dict(p) if hasattr(ProductSchema._release._addons, 'from_dict') else p for p in d["addons"]]
                if "docsets" in d:
                    v["docsets"] = [ProductSchema._release._docsets.from_dict(p) if hasattr(ProductSchema._release._docsets, 'from_dict') else p for p in d["docsets"]]
                return ProductSchema._release(**v)


            def as_dict(self):
                d = {}
                if self.__releaseNotes is not None:
                    d['releaseNotes'] = self.__releaseNotes.as_dict() if hasattr(self.__releaseNotes, 'as_dict') else self.__releaseNotes
                if self.__version is not None:
                    d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                if self.__sku is not None:
                    d['sku'] = self.__sku.as_dict() if hasattr(self.__sku, 'as_dict') else self.__sku
                if self.__addons is not None:
                    d['addons'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__addons]
                if self.__docsets is not None:
                    d['docsets'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__docsets]
                return d

            def __repr__(self):
                return "<Class _release. releaseNotes: {}, version: {}, sku: {}, addons: {}, docsets: {}>".format(limitedRepr(self.__releaseNotes[:20] if isinstance(self.__releaseNotes, bytes) else self.__releaseNotes), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__sku[:20] if isinstance(self.__sku, bytes) else self.__sku), limitedRepr(self.__addons[:20] if isinstance(self.__addons, bytes) else self.__addons), limitedRepr(self.__docsets[:20] if isinstance(self.__docsets, bytes) else self.__docsets))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'ident': {'type': identifier, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'scm': {'type': scm, 'subtype': None},
        'history': {'type': list, 'subtype': event},
        'tags': {'type': list, 'subtype': str},
        'status': {'type': str, 'subtype': None},
        'shared': {'type': bool, 'subtype': None},
        'components': {'type': list, 'subtype': identifier},
        'repositories': {'type': repositories, 'subtype': None},
        'packages': {'type': packages, 'subtype': None},
        'quality': {'type': identifier, 'subtype': None},
        'deliverable': {'type': deliverable, 'subtype': None},
        'release': {'type': _release, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'schema': { 'required': False,},
        'ident': { 'required': True,},
        'name': { 'required': True,},
        'description': { 'required': True,},
        'scm': { 'required': False,},
        'history': { 'required': False,},
        'tags': { 'required': False,},
        'status': { 'required': True,},
        'shared': { 'required': False,},
        'components': { 'required': True,},
        'repositories': { 'required': False,},
        'packages': { 'required': False,},
        'quality': { 'required': False,},
        'deliverable': { 'required': False,},
        'release': { 'required': False,},
    }

    def __init__(self
            , *args
            , schema=None
            , ident=None
            , name=None
            , description=None
            , scm=None
            , history=None
            , tags=None
            , status='FT Ready'
            , shared=None
            , components=None
            , repositories=None
            , packages=None
            , quality=None
            , deliverable=None
            , release=None
            , **kwargs
            ):
        """
        :param shared: Use it when the packages of an artifact are shared between several repository
        :param components: A list of components
        :param release: Contain all release-related informations
        """
        self.__schema = schema
        self.__ident = ident
        self.__name = name
        self.__description = description
        self.__scm = scm
        self.__history = history
        self.__tags = tags
        self.__status = status
        self.__shared = shared
        self.__components = components
        self.__repositories = repositories
        self.__packages = packages
        self.__quality = quality
        self.__deliverable = deliverable
        self.__release = release
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

    def _get_scm(self):
        return self.__scm
    def _set_scm(self, value):
        if value is not None and  not isinstance(value, scm):
            raise TypeError("scm must be scm")

        self.__scm = value
    scm = property(_get_scm, _set_scm)

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

    def _get_components(self):
        return self.__components
    def _set_components(self, value):
        if  not isinstance(value, list):
            raise TypeError("components must be list")
        if  not all(isinstance(i, identifier) for i in value):
            raise TypeError("components list values must be identifier")

        self.__components = value
    components = property(_get_components, _set_components)
    """
    A list of components
    """

    def _get_repositories(self):
        return self.__repositories
    def _set_repositories(self, value):
        if value is not None and  not isinstance(value, repositories):
            raise TypeError("repositories must be repositories")

        self.__repositories = value
    repositories = property(_get_repositories, _set_repositories)

    def _get_packages(self):
        return self.__packages
    def _set_packages(self, value):
        if value is not None and  not isinstance(value, packages):
            raise TypeError("packages must be packages")

        self.__packages = value
    packages = property(_get_packages, _set_packages)

    def _get_quality(self):
        return self.__quality
    def _set_quality(self, value):
        if value is not None and  not isinstance(value, identifier):
            raise TypeError("quality must be identifier")

        self.__quality = value
    quality = property(_get_quality, _set_quality)

    def _get_deliverable(self):
        return self.__deliverable
    def _set_deliverable(self, value):
        if value is not None and  not isinstance(value, deliverable):
            raise TypeError("deliverable must be deliverable")

        self.__deliverable = value
    deliverable = property(_get_deliverable, _set_deliverable)

    def _get_release(self):
        return self.__release
    def _set_release(self, value):
        if value is not None and  not isinstance(value, ProductSchema._release):
            raise TypeError("release must be ProductSchema._release")

        self.__release = value
    release = property(_get_release, _set_release)
    """
    Contain all release-related informations
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
        if "scm" in d:
            v["scm"] = scm.from_dict(d["scm"]) if hasattr(scm, 'from_dict') else d["scm"]
        if "history" in d:
            v["history"] = [event.from_dict(p) if hasattr(event, 'from_dict') else p for p in d["history"]]
        if "tags" in d:
            v["tags"] = [str.from_dict(p) if hasattr(str, 'from_dict') else p for p in d["tags"]]
        if "status" in d:
            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
        if "shared" in d:
            v["shared"] = bool.from_dict(d["shared"]) if hasattr(bool, 'from_dict') else d["shared"]
        if "components" in d:
            v["components"] = [identifier.from_dict(p) if hasattr(identifier, 'from_dict') else p for p in d["components"]]
        if "repositories" in d:
            v["repositories"] = repositories.from_dict(d["repositories"]) if hasattr(repositories, 'from_dict') else d["repositories"]
        if "packages" in d:
            v["packages"] = packages.from_dict(d["packages"]) if hasattr(packages, 'from_dict') else d["packages"]
        if "quality" in d:
            v["quality"] = identifier.from_dict(d["quality"]) if hasattr(identifier, 'from_dict') else d["quality"]
        if "deliverable" in d:
            v["deliverable"] = deliverable.from_dict(d["deliverable"]) if hasattr(deliverable, 'from_dict') else d["deliverable"]
        if "release" in d:
            v["release"] = ProductSchema._release.from_dict(d["release"]) if hasattr(ProductSchema._release, 'from_dict') else d["release"]
        return ProductSchema(**v)


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
        if self.__scm is not None:
            d['scm'] = self.__scm.as_dict() if hasattr(self.__scm, 'as_dict') else self.__scm
        if self.__history is not None:
            d['history'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__history]
        if self.__tags is not None:
            d['tags'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__tags]
        if self.__status is not None:
            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
        if self.__shared is not None:
            d['shared'] = self.__shared.as_dict() if hasattr(self.__shared, 'as_dict') else self.__shared
        if self.__components is not None:
            d['components'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__components]
        if self.__repositories is not None:
            d['repositories'] = self.__repositories.as_dict() if hasattr(self.__repositories, 'as_dict') else self.__repositories
        if self.__packages is not None:
            d['packages'] = self.__packages.as_dict() if hasattr(self.__packages, 'as_dict') else self.__packages
        if self.__quality is not None:
            d['quality'] = self.__quality.as_dict() if hasattr(self.__quality, 'as_dict') else self.__quality
        if self.__deliverable is not None:
            d['deliverable'] = self.__deliverable.as_dict() if hasattr(self.__deliverable, 'as_dict') else self.__deliverable
        if self.__release is not None:
            d['release'] = self.__release.as_dict() if hasattr(self.__release, 'as_dict') else self.__release
        return d

    def __repr__(self):
        return "<Class ProductSchema. schema: {}, ident: {}, name: {}, description: {}, scm: {}, history: {}, tags: {}, status: {}, shared: {}, components: {}, repositories: {}, packages: {}, quality: {}, deliverable: {}, release: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__ident[:20] if isinstance(self.__ident, bytes) else self.__ident), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__scm[:20] if isinstance(self.__scm, bytes) else self.__scm), limitedRepr(self.__history[:20] if isinstance(self.__history, bytes) else self.__history), limitedRepr(self.__tags[:20] if isinstance(self.__tags, bytes) else self.__tags), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status), limitedRepr(self.__shared[:20] if isinstance(self.__shared, bytes) else self.__shared), limitedRepr(self.__components[:20] if isinstance(self.__components, bytes) else self.__components), limitedRepr(self.__repositories[:20] if isinstance(self.__repositories, bytes) else self.__repositories), limitedRepr(self.__packages[:20] if isinstance(self.__packages, bytes) else self.__packages), limitedRepr(self.__quality[:20] if isinstance(self.__quality, bytes) else self.__quality), limitedRepr(self.__deliverable[:20] if isinstance(self.__deliverable, bytes) else self.__deliverable), limitedRepr(self.__release[:20] if isinstance(self.__release, bytes) else self.__release))

