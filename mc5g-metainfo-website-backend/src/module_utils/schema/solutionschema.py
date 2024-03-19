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

class SolutionSchema(MetainfoBase):
    """
    The root schema is the schema that comprises the entire JSON document.
    """
    class _testCampaigns:
            """
            Test campaign
            """
            class _categories:
                    """
                    Category of test, with status (failed, passed, not tested)
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'status': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'status': { 'required': False,},
                    }

                    def __init__(self
                            , name=None
                            , status='N/A'
                            ):
                        """
                        :param name: Name of this test category for test campaigns of solutions (QA to RC)
                        :param status: Test status for this category of test campaigns
                        """
                        self.__name = name
                        self.__status = status
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)
                    """
                    Name of this test category for test campaigns of solutions (QA to RC)
                    """

                    def _get_status(self):
                        return self.__status
                    def _set_status(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("status must be str")

                        self.__status = value
                    status = property(_get_status, _set_status)
                    """
                    Test status for this category of test campaigns
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "status" in d:
                            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
                        return SolutionSchema._testCampaigns._categories(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__status is not None:
                            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
                        return d

                    def __repr__(self):
                        return "<Class _categories. name: {}, status: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status))




            _types_map = {
                'title': {'type': str, 'subtype': None},
                'description': {'type': str, 'subtype': None},
                'date': {'type': str, 'subtype': None},
                'link': {'type': str, 'subtype': None},
                'categories': {'type': list, 'subtype': _categories},
            }
            _formats_map = {
                'date': 'date-time',
                'link': 'uri',
            }
            _validations_map = {
                'title': { 'required': True,},
                'description': { 'required': True,},
                'date': { 'required': True,},
                'link': { 'required': True,},
                'categories': { 'required': True,},
            }

            def __init__(self
                    , title=None
                    , description=None
                    , date=None
                    , link=None
                    , categories=None
                    ):
                """
                :param title: The name of the test campaign
                :param description: A description of this test campaign
                :param date: The date of the test campaign
                :param link: URL of data concerning this test campaign
                """
                self.__title = title
                self.__description = description
                self.__date = date
                self.__link = link
                self.__categories = categories
                pass

            def _get_title(self):
                return self.__title
            def _set_title(self, value):
                if  not isinstance(value, str):
                    raise TypeError("title must be str")

                self.__title = value
            title = property(_get_title, _set_title)
            """
            The name of the test campaign
            """

            def _get_description(self):
                return self.__description
            def _set_description(self, value):
                if  not isinstance(value, str):
                    raise TypeError("description must be str")

                self.__description = value
            description = property(_get_description, _set_description)
            """
            A description of this test campaign
            """

            def _get_date(self):
                return self.__date
            def _set_date(self, value):
                if  not isinstance(value, str):
                    raise TypeError("date must be str")

                self.__date = value
            date = property(_get_date, _set_date)
            """
            The date of the test campaign
            """

            def _get_link(self):
                return self.__link
            def _set_link(self, value):
                if  not isinstance(value, str):
                    raise TypeError("link must be str")

                self.__link = value
            link = property(_get_link, _set_link)
            """
            URL of data concerning this test campaign
            """

            def _get_categories(self):
                return self.__categories
            def _set_categories(self, value):
                if  not isinstance(value, list):
                    raise TypeError("categories must be list")
                if  not all(isinstance(i, SolutionSchema._testCampaigns._categories) for i in value):
                    raise TypeError("categories list values must be SolutionSchema._testCampaigns._categories")

                self.__categories = value
            categories = property(_get_categories, _set_categories)


            @staticmethod
            def from_dict(d):
                v = {}
                if "title" in d:
                    v["title"] = str.from_dict(d["title"]) if hasattr(str, 'from_dict') else d["title"]
                if "description" in d:
                    v["description"] = str.from_dict(d["description"]) if hasattr(str, 'from_dict') else d["description"]
                if "date" in d:
                    v["date"] = str.from_dict(d["date"]) if hasattr(str, 'from_dict') else d["date"]
                if "link" in d:
                    v["link"] = str.from_dict(d["link"]) if hasattr(str, 'from_dict') else d["link"]
                if "categories" in d:
                    v["categories"] = [SolutionSchema._testCampaigns._categories.from_dict(p) if hasattr(SolutionSchema._testCampaigns._categories, 'from_dict') else p for p in d["categories"]]
                return SolutionSchema._testCampaigns(**v)


            def as_dict(self):
                d = {}
                if self.__title is not None:
                    d['title'] = self.__title.as_dict() if hasattr(self.__title, 'as_dict') else self.__title
                if self.__description is not None:
                    d['description'] = self.__description.as_dict() if hasattr(self.__description, 'as_dict') else self.__description
                if self.__date is not None:
                    d['date'] = self.__date.as_dict() if hasattr(self.__date, 'as_dict') else self.__date
                if self.__link is not None:
                    d['link'] = self.__link.as_dict() if hasattr(self.__link, 'as_dict') else self.__link
                if self.__categories is not None:
                    d['categories'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__categories]
                return d

            def __repr__(self):
                return "<Class _testCampaigns. title: {}, description: {}, date: {}, link: {}, categories: {}>".format(limitedRepr(self.__title[:20] if isinstance(self.__title, bytes) else self.__title), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__date[:20] if isinstance(self.__date, bytes) else self.__date), limitedRepr(self.__link[:20] if isinstance(self.__link, bytes) else self.__link), limitedRepr(self.__categories[:20] if isinstance(self.__categories, bytes) else self.__categories))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'ident': {'type': identifier, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'history': {'type': list, 'subtype': event},
        'tags': {'type': list, 'subtype': str},
        'status': {'type': str, 'subtype': None},
        'parent': {'type': str, 'subtype': None},
        'products': {'type': list, 'subtype': identifier},
        'testCampaigns': {'type': list, 'subtype': _testCampaigns},
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
        'parent': { 'required': True,},
        'products': { 'required': True,},
        'testCampaigns': { 'required': False,},
    }

    def __init__(self
            , *args
            , schema=None
            , ident=None
            , name=None
            , description=None
            , history=None
            , tags=None
            , status='Val Ready'
            , parent=None
            , products=None
            , testCampaigns=None
            , **kwargs
            ):
        """
        :param products: A list of products
        :param testCampaigns: A list of test campaigns
        """
        self.__schema = schema
        self.__ident = ident
        self.__name = name
        self.__description = description
        self.__history = history
        self.__tags = tags
        self.__status = status
        self.__parent = parent
        self.__products = products
        self.__testCampaigns = testCampaigns
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

    def _get_parent(self):
        return self.__parent
    def _set_parent(self, value):
        if  not isinstance(value, str):
            raise TypeError("parent must be str")

        self.__parent = value
    parent = property(_get_parent, _set_parent)

    def _get_products(self):
        return self.__products
    def _set_products(self, value):
        if  not isinstance(value, list):
            raise TypeError("products must be list")
        if  not all(isinstance(i, identifier) for i in value):
            raise TypeError("products list values must be identifier")

        self.__products = value
    products = property(_get_products, _set_products)
    """
    A list of products
    """

    def _get_testCampaigns(self):
        return self.__testCampaigns
    def _set_testCampaigns(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("testCampaigns must be list")
        if value is not None and  not all(isinstance(i, SolutionSchema._testCampaigns) for i in value):
            raise TypeError("testCampaigns list values must be SolutionSchema._testCampaigns")

        self.__testCampaigns = value
    testCampaigns = property(_get_testCampaigns, _set_testCampaigns)
    """
    A list of test campaigns
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
        if "parent" in d:
            v["parent"] = str.from_dict(d["parent"]) if hasattr(str, 'from_dict') else d["parent"]
        if "products" in d:
            v["products"] = [identifier.from_dict(p) if hasattr(identifier, 'from_dict') else p for p in d["products"]]
        if "testCampaigns" in d:
            v["testCampaigns"] = [SolutionSchema._testCampaigns.from_dict(p) if hasattr(SolutionSchema._testCampaigns, 'from_dict') else p for p in d["testCampaigns"]]
        return SolutionSchema(**v)


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
        if self.__parent is not None:
            d['parent'] = self.__parent.as_dict() if hasattr(self.__parent, 'as_dict') else self.__parent
        if self.__products is not None:
            d['products'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__products]
        if self.__testCampaigns is not None:
            d['testCampaigns'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__testCampaigns]
        return d

    def __repr__(self):
        return "<Class SolutionSchema. schema: {}, ident: {}, name: {}, description: {}, history: {}, tags: {}, status: {}, parent: {}, products: {}, testCampaigns: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__ident[:20] if isinstance(self.__ident, bytes) else self.__ident), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__history[:20] if isinstance(self.__history, bytes) else self.__history), limitedRepr(self.__tags[:20] if isinstance(self.__tags, bytes) else self.__tags), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status), limitedRepr(self.__parent[:20] if isinstance(self.__parent, bytes) else self.__parent), limitedRepr(self.__products[:20] if isinstance(self.__products, bytes) else self.__products), limitedRepr(self.__testCampaigns[:20] if isinstance(self.__testCampaigns, bytes) else self.__testCampaigns))

