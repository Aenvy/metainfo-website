from reprlib import repr as limitedRepr


import enum
try:
    from ansible.module_utils.schema.definitions import *
except ImportError:
    from module_utils.schema.definitions import *


class ProductInfoSchema:
    """
    The root schema is the schema that comprises the entire JSON document.
    """
    class _jira:
            """
            Contain all jira-related informations
            """



            _types_map = {
                'productName': {'type': str, 'subtype': None},
                'projectName': {'type': str, 'subtype': None},
                'projectNames': {'type': list, 'subtype': str},
                'releaseProjectId': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'productName': { 'required': True,},
                'projectName': { 'required': True,},
                'projectNames': { 'required': True,},
                'releaseProjectId': { 'required': True,},
            }

            def __init__(self
                    , productName=None
                    , projectName=None
                    , projectNames=None
                    , releaseProjectId=None
                    ):
                self.__productName = productName
                self.__projectName = projectName
                self.__projectNames = projectNames
                self.__releaseProjectId = releaseProjectId
                pass

            def _get_productName(self):
                return self.__productName
            def _set_productName(self, value):
                if  not isinstance(value, str):
                    raise TypeError("productName must be str")

                self.__productName = value
            productName = property(_get_productName, _set_productName)

            def _get_projectName(self):
                return self.__projectName
            def _set_projectName(self, value):
                if  not isinstance(value, str):
                    raise TypeError("projectName must be str")

                self.__projectName = value
            projectName = property(_get_projectName, _set_projectName)

            def _get_projectNames(self):
                return self.__projectNames
            def _set_projectNames(self, value):
                if  not isinstance(value, list):
                    raise TypeError("projectNames must be list")
                if  not all(isinstance(i, str) for i in value):
                    raise TypeError("projectNames list values must be str")

                self.__projectNames = value
            projectNames = property(_get_projectNames, _set_projectNames)

            def _get_releaseProjectId(self):
                return self.__releaseProjectId
            def _set_releaseProjectId(self, value):
                if  not isinstance(value, str):
                    raise TypeError("releaseProjectId must be str")

                self.__releaseProjectId = value
            releaseProjectId = property(_get_releaseProjectId, _set_releaseProjectId)


            @staticmethod
            def from_dict(d):
                v = {}
                if "productName" in d:
                    v["productName"] = str.from_dict(d["productName"]) if hasattr(str, 'from_dict') else d["productName"]
                if "projectName" in d:
                    v["projectName"] = str.from_dict(d["projectName"]) if hasattr(str, 'from_dict') else d["projectName"]
                if "projectNames" in d:
                    v["projectNames"] = [str.from_dict(p) if hasattr(str, 'from_dict') else p for p in d["projectNames"]]
                if "releaseProjectId" in d:
                    v["releaseProjectId"] = str.from_dict(d["releaseProjectId"]) if hasattr(str, 'from_dict') else d["releaseProjectId"]
                return ProductInfoSchema._jira(**v)


            def as_dict(self):
                d = {}
                if self.__productName is not None:
                    d['productName'] = self.__productName.as_dict() if hasattr(self.__productName, 'as_dict') else self.__productName
                if self.__projectName is not None:
                    d['projectName'] = self.__projectName.as_dict() if hasattr(self.__projectName, 'as_dict') else self.__projectName
                if self.__projectNames is not None:
                    d['projectNames'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__projectNames]
                if self.__releaseProjectId is not None:
                    d['releaseProjectId'] = self.__releaseProjectId.as_dict() if hasattr(self.__releaseProjectId, 'as_dict') else self.__releaseProjectId
                return d

            def __repr__(self):
                return "<Class _jira. productName: {}, projectName: {}, projectNames: {}, releaseProjectId: {}>".format(limitedRepr(self.__productName[:20] if isinstance(self.__productName, bytes) else self.__productName), limitedRepr(self.__projectName[:20] if isinstance(self.__projectName, bytes) else self.__projectName), limitedRepr(self.__projectNames[:20] if isinstance(self.__projectNames, bytes) else self.__projectNames), limitedRepr(self.__releaseProjectId[:20] if isinstance(self.__releaseProjectId, bytes) else self.__releaseProjectId))

    class _vtn:
            """
            Contain all vtn-related informations
            """



            _types_map = {
                'distributionList': {'type': str, 'subtype': None},
                'productName': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'distributionList': { 'required': True,},
                'productName': { 'required': True,},
            }

            def __init__(self
                    , distributionList=None
                    , productName=None
                    ):
                self.__distributionList = distributionList
                self.__productName = productName
                pass

            def _get_distributionList(self):
                return self.__distributionList
            def _set_distributionList(self, value):
                if  not isinstance(value, str):
                    raise TypeError("distributionList must be str")

                self.__distributionList = value
            distributionList = property(_get_distributionList, _set_distributionList)

            def _get_productName(self):
                return self.__productName
            def _set_productName(self, value):
                if  not isinstance(value, str):
                    raise TypeError("productName must be str")

                self.__productName = value
            productName = property(_get_productName, _set_productName)


            @staticmethod
            def from_dict(d):
                v = {}
                if "distributionList" in d:
                    v["distributionList"] = str.from_dict(d["distributionList"]) if hasattr(str, 'from_dict') else d["distributionList"]
                if "productName" in d:
                    v["productName"] = str.from_dict(d["productName"]) if hasattr(str, 'from_dict') else d["productName"]
                return ProductInfoSchema._vtn(**v)


            def as_dict(self):
                d = {}
                if self.__distributionList is not None:
                    d['distributionList'] = self.__distributionList.as_dict() if hasattr(self.__distributionList, 'as_dict') else self.__distributionList
                if self.__productName is not None:
                    d['productName'] = self.__productName.as_dict() if hasattr(self.__productName, 'as_dict') else self.__productName
                return d

            def __repr__(self):
                return "<Class _vtn. distributionList: {}, productName: {}>".format(limitedRepr(self.__distributionList[:20] if isinstance(self.__distributionList, bytes) else self.__distributionList), limitedRepr(self.__productName[:20] if isinstance(self.__productName, bytes) else self.__productName))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'productName': {'type': str, 'subtype': None},
        'releasePrefix': {'type': str, 'subtype': None},
        'metainfo': {'type': str, 'subtype': None},
        'mail': {'type': str, 'subtype': None},
        'jira': {'type': _jira, 'subtype': None},
        'nf': {'type': partialIdentifier, 'subtype': None},
        'prod': {'type': partialIdentifier, 'subtype': None},
        'quality': {'type': partialIdentifier, 'subtype': None},
        'test': {'type': partialIdentifier, 'subtype': None},
        'result': {'type': partialIdentifier, 'subtype': None},
        'components': {'type': list, 'subtype': partialIdentifier},
        'supplantedProducts': {'type': list, 'subtype': partialIdentifier},
        'sku': {'type': str, 'subtype': None},
        'testSku': {'type': str, 'subtype': None},
        'vtn': {'type': _vtn, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'schema': { 'required': True,},
        'name': { 'required': True,},
        'productName': { 'required': True,},
        'releasePrefix': { 'required': True,},
        'metainfo': { 'required': True,},
        'mail': { 'required': True,},
        'jira': { 'required': True,},
        'nf': { 'required': True,},
        'prod': { 'required': True,},
        'quality': { 'required': True,},
        'test': { 'required': True,},
        'result': { 'required': True,},
        'components': { 'required': True,},
        'supplantedProducts': { 'required': False,},
        'sku': { 'required': False,},
        'testSku': { 'required': False,},
        'vtn': { 'required': True,},
    }

    def __init__(self
            , schema=None
            , name=None
            , productName=None
            , releasePrefix=None
            , metainfo=None
            , mail=None
            , jira=None
            , nf=None
            , prod=None
            , quality=None
            , test=None
            , result=None
            , components=None
            , supplantedProducts=None
            , sku=None
            , testSku=None
            , vtn=None
            ):
        """
        :param jira: Contain all jira-related informations
        :param components: A list of components
        :param supplantedProducts: A list of products supplanted by this product
        :param vtn: Contain all vtn-related informations
        """
        self.__schema = schema
        self.__name = name
        self.__productName = productName
        self.__releasePrefix = releasePrefix
        self.__metainfo = metainfo
        self.__mail = mail
        self.__jira = jira
        self.__nf = nf
        self.__prod = prod
        self.__quality = quality
        self.__test = test
        self.__result = result
        self.__components = components
        self.__supplantedProducts = supplantedProducts
        self.__sku = sku
        self.__testSku = testSku
        self.__vtn = vtn
        pass

    def _get_schema(self):
        return self.__schema
    def _set_schema(self, value):
        if  not isinstance(value, str):
            raise TypeError("schema must be str")

        self.__schema = value
    schema = property(_get_schema, _set_schema)

    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if  not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value
    name = property(_get_name, _set_name)

    def _get_productName(self):
        return self.__productName
    def _set_productName(self, value):
        if  not isinstance(value, str):
            raise TypeError("productName must be str")

        self.__productName = value
    productName = property(_get_productName, _set_productName)

    def _get_releasePrefix(self):
        return self.__releasePrefix
    def _set_releasePrefix(self, value):
        if  not isinstance(value, str):
            raise TypeError("releasePrefix must be str")

        self.__releasePrefix = value
    releasePrefix = property(_get_releasePrefix, _set_releasePrefix)

    def _get_metainfo(self):
        return self.__metainfo
    def _set_metainfo(self, value):
        if  not isinstance(value, str):
            raise TypeError("metainfo must be str")

        self.__metainfo = value
    metainfo = property(_get_metainfo, _set_metainfo)

    def _get_mail(self):
        return self.__mail
    def _set_mail(self, value):
        if  not isinstance(value, str):
            raise TypeError("mail must be str")

        self.__mail = value
    mail = property(_get_mail, _set_mail)

    def _get_jira(self):
        return self.__jira
    def _set_jira(self, value):
        if  not isinstance(value, ProductInfoSchema._jira):
            raise TypeError("jira must be ProductInfoSchema._jira")

        self.__jira = value
    jira = property(_get_jira, _set_jira)
    """
    Contain all jira-related informations
    """

    def _get_nf(self):
        return self.__nf
    def _set_nf(self, value):
        if  not isinstance(value, partialIdentifier):
            raise TypeError("nf must be partialIdentifier")

        self.__nf = value
    nf = property(_get_nf, _set_nf)

    def _get_prod(self):
        return self.__prod
    def _set_prod(self, value):
        if  not isinstance(value, partialIdentifier):
            raise TypeError("prod must be partialIdentifier")

        self.__prod = value
    prod = property(_get_prod, _set_prod)

    def _get_quality(self):
        return self.__quality
    def _set_quality(self, value):
        if  not isinstance(value, partialIdentifier):
            raise TypeError("quality must be partialIdentifier")

        self.__quality = value
    quality = property(_get_quality, _set_quality)

    def _get_test(self):
        return self.__test
    def _set_test(self, value):
        if  not isinstance(value, partialIdentifier):
            raise TypeError("test must be partialIdentifier")

        self.__test = value
    test = property(_get_test, _set_test)

    def _get_result(self):
        return self.__result
    def _set_result(self, value):
        if  not isinstance(value, partialIdentifier):
            raise TypeError("result must be partialIdentifier")

        self.__result = value
    result = property(_get_result, _set_result)

    def _get_components(self):
        return self.__components
    def _set_components(self, value):
        if  not isinstance(value, list):
            raise TypeError("components must be list")
        if  not all(isinstance(i, partialIdentifier) for i in value):
            raise TypeError("components list values must be partialIdentifier")

        self.__components = value
    components = property(_get_components, _set_components)
    """
    A list of components
    """

    def _get_supplantedProducts(self):
        return self.__supplantedProducts
    def _set_supplantedProducts(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("supplantedProducts must be list")
        if value is not None and  not all(isinstance(i, partialIdentifier) for i in value):
            raise TypeError("supplantedProducts list values must be partialIdentifier")

        self.__supplantedProducts = value
    supplantedProducts = property(_get_supplantedProducts, _set_supplantedProducts)
    """
    A list of products supplanted by this product
    """

    def _get_sku(self):
        return self.__sku
    def _set_sku(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("sku must be str")

        self.__sku = value
    sku = property(_get_sku, _set_sku)

    def _get_testSku(self):
        return self.__testSku
    def _set_testSku(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("testSku must be str")

        self.__testSku = value
    testSku = property(_get_testSku, _set_testSku)

    def _get_vtn(self):
        return self.__vtn
    def _set_vtn(self, value):
        if  not isinstance(value, ProductInfoSchema._vtn):
            raise TypeError("vtn must be ProductInfoSchema._vtn")

        self.__vtn = value
    vtn = property(_get_vtn, _set_vtn)
    """
    Contain all vtn-related informations
    """


    @staticmethod
    def from_dict(d):
        v = {}
        if "schema" in d:
            v["schema"] = str.from_dict(d["schema"]) if hasattr(str, 'from_dict') else d["schema"]
        if "name" in d:
            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
        if "productName" in d:
            v["productName"] = str.from_dict(d["productName"]) if hasattr(str, 'from_dict') else d["productName"]
        if "releasePrefix" in d:
            v["releasePrefix"] = str.from_dict(d["releasePrefix"]) if hasattr(str, 'from_dict') else d["releasePrefix"]
        if "metainfo" in d:
            v["metainfo"] = str.from_dict(d["metainfo"]) if hasattr(str, 'from_dict') else d["metainfo"]
        if "mail" in d:
            v["mail"] = str.from_dict(d["mail"]) if hasattr(str, 'from_dict') else d["mail"]
        if "jira" in d:
            v["jira"] = ProductInfoSchema._jira.from_dict(d["jira"]) if hasattr(ProductInfoSchema._jira, 'from_dict') else d["jira"]
        if "nf" in d:
            v["nf"] = partialIdentifier.from_dict(d["nf"]) if hasattr(partialIdentifier, 'from_dict') else d["nf"]
        if "prod" in d:
            v["prod"] = partialIdentifier.from_dict(d["prod"]) if hasattr(partialIdentifier, 'from_dict') else d["prod"]
        if "quality" in d:
            v["quality"] = partialIdentifier.from_dict(d["quality"]) if hasattr(partialIdentifier, 'from_dict') else d["quality"]
        if "test" in d:
            v["test"] = partialIdentifier.from_dict(d["test"]) if hasattr(partialIdentifier, 'from_dict') else d["test"]
        if "result" in d:
            v["result"] = partialIdentifier.from_dict(d["result"]) if hasattr(partialIdentifier, 'from_dict') else d["result"]
        if "components" in d:
            v["components"] = [partialIdentifier.from_dict(p) if hasattr(partialIdentifier, 'from_dict') else p for p in d["components"]]
        if "supplantedProducts" in d:
            v["supplantedProducts"] = [partialIdentifier.from_dict(p) if hasattr(partialIdentifier, 'from_dict') else p for p in d["supplantedProducts"]]
        if "sku" in d:
            v["sku"] = str.from_dict(d["sku"]) if hasattr(str, 'from_dict') else d["sku"]
        if "testSku" in d:
            v["testSku"] = str.from_dict(d["testSku"]) if hasattr(str, 'from_dict') else d["testSku"]
        if "vtn" in d:
            v["vtn"] = ProductInfoSchema._vtn.from_dict(d["vtn"]) if hasattr(ProductInfoSchema._vtn, 'from_dict') else d["vtn"]
        return ProductInfoSchema(**v)


    def as_dict(self):
        d = {}
        if self.__schema is not None:
            d['schema'] = self.__schema.as_dict() if hasattr(self.__schema, 'as_dict') else self.__schema
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__productName is not None:
            d['productName'] = self.__productName.as_dict() if hasattr(self.__productName, 'as_dict') else self.__productName
        if self.__releasePrefix is not None:
            d['releasePrefix'] = self.__releasePrefix.as_dict() if hasattr(self.__releasePrefix, 'as_dict') else self.__releasePrefix
        if self.__metainfo is not None:
            d['metainfo'] = self.__metainfo.as_dict() if hasattr(self.__metainfo, 'as_dict') else self.__metainfo
        if self.__mail is not None:
            d['mail'] = self.__mail.as_dict() if hasattr(self.__mail, 'as_dict') else self.__mail
        if self.__jira is not None:
            d['jira'] = self.__jira.as_dict() if hasattr(self.__jira, 'as_dict') else self.__jira
        if self.__nf is not None:
            d['nf'] = self.__nf.as_dict() if hasattr(self.__nf, 'as_dict') else self.__nf
        if self.__prod is not None:
            d['prod'] = self.__prod.as_dict() if hasattr(self.__prod, 'as_dict') else self.__prod
        if self.__quality is not None:
            d['quality'] = self.__quality.as_dict() if hasattr(self.__quality, 'as_dict') else self.__quality
        if self.__test is not None:
            d['test'] = self.__test.as_dict() if hasattr(self.__test, 'as_dict') else self.__test
        if self.__result is not None:
            d['result'] = self.__result.as_dict() if hasattr(self.__result, 'as_dict') else self.__result
        if self.__components is not None:
            d['components'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__components]
        if self.__supplantedProducts is not None:
            d['supplantedProducts'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__supplantedProducts]
        if self.__sku is not None:
            d['sku'] = self.__sku.as_dict() if hasattr(self.__sku, 'as_dict') else self.__sku
        if self.__testSku is not None:
            d['testSku'] = self.__testSku.as_dict() if hasattr(self.__testSku, 'as_dict') else self.__testSku
        if self.__vtn is not None:
            d['vtn'] = self.__vtn.as_dict() if hasattr(self.__vtn, 'as_dict') else self.__vtn
        return d

    def __repr__(self):
        return "<Class ProductInfoSchema. schema: {}, name: {}, productName: {}, releasePrefix: {}, metainfo: {}, mail: {}, jira: {}, nf: {}, prod: {}, quality: {}, test: {}, result: {}, components: {}, supplantedProducts: {}, sku: {}, testSku: {}, vtn: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__productName[:20] if isinstance(self.__productName, bytes) else self.__productName), limitedRepr(self.__releasePrefix[:20] if isinstance(self.__releasePrefix, bytes) else self.__releasePrefix), limitedRepr(self.__metainfo[:20] if isinstance(self.__metainfo, bytes) else self.__metainfo), limitedRepr(self.__mail[:20] if isinstance(self.__mail, bytes) else self.__mail), limitedRepr(self.__jira[:20] if isinstance(self.__jira, bytes) else self.__jira), limitedRepr(self.__nf[:20] if isinstance(self.__nf, bytes) else self.__nf), limitedRepr(self.__prod[:20] if isinstance(self.__prod, bytes) else self.__prod), limitedRepr(self.__quality[:20] if isinstance(self.__quality, bytes) else self.__quality), limitedRepr(self.__test[:20] if isinstance(self.__test, bytes) else self.__test), limitedRepr(self.__result[:20] if isinstance(self.__result, bytes) else self.__result), limitedRepr(self.__components[:20] if isinstance(self.__components, bytes) else self.__components), limitedRepr(self.__supplantedProducts[:20] if isinstance(self.__supplantedProducts, bytes) else self.__supplantedProducts), limitedRepr(self.__sku[:20] if isinstance(self.__sku, bytes) else self.__sku), limitedRepr(self.__testSku[:20] if isinstance(self.__testSku, bytes) else self.__testSku), limitedRepr(self.__vtn[:20] if isinstance(self.__vtn, bytes) else self.__vtn))

