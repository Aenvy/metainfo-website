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

class CaasSchema(MetainfoBase):
    """
    The CaaS schema describes a Caas.
    """
    class _project:
            class _cluster:
                    """
                    OCP cluster API URL and location
                    """



                    _types_map = {
                        'uri': {'type': str, 'subtype': None},
                        'location': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'uri': { 'required': False,},
                        'location': { 'required': False,},
                    }

                    def __init__(self
                            , uri=None
                            , location='Grenoble'
                            ):
                        self.__uri = uri
                        self.__location = location
                        pass

                    def _get_uri(self):
                        return self.__uri
                    def _set_uri(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("uri must be str")

                        self.__uri = value
                    uri = property(_get_uri, _set_uri)

                    def _get_location(self):
                        return self.__location
                    def _set_location(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("location must be str")

                        self.__location = value
                    location = property(_get_location, _set_location)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "uri" in d:
                            v["uri"] = str.from_dict(d["uri"]) if hasattr(str, 'from_dict') else d["uri"]
                        if "location" in d:
                            v["location"] = str.from_dict(d["location"]) if hasattr(str, 'from_dict') else d["location"]
                        return CaasSchema._project._cluster(**v)


                    def as_dict(self):
                        d = {}
                        if self.__uri is not None:
                            d['uri'] = self.__uri.as_dict() if hasattr(self.__uri, 'as_dict') else self.__uri
                        if self.__location is not None:
                            d['location'] = self.__location.as_dict() if hasattr(self.__location, 'as_dict') else self.__location
                        return d

                    def __repr__(self):
                        return "<Class _cluster. uri: {}, location: {}>".format(limitedRepr(self.__uri[:20] if isinstance(self.__uri, bytes) else self.__uri), limitedRepr(self.__location[:20] if isinstance(self.__location, bytes) else self.__location))

            class _quotas:
                    """
                    OCP quota details about cpu, memory, pods and storage
                    """
                    class _limits:
                            """
                            OCP limit details about cpu, memory and pods
                            """



                            _types_map = {
                                'cpu': {'type': int, 'subtype': None},
                                'memory': {'type': str, 'subtype': None},
                                'pods': {'type': int, 'subtype': None},
                            }
                            _formats_map = {
                            }
                            _validations_map = {
                                'cpu': { 'required': False,},
                                'memory': { 'required': False,'pattern': '[0-9]+Gi',},
                                'pods': { 'required': False,},
                            }

                            def __init__(self
                                    , cpu=None
                                    , memory=None
                                    , pods=None
                                    ):
                                self.__cpu = cpu
                                self.__memory = memory
                                self.__pods = pods
                                pass

                            def _get_cpu(self):
                                return self.__cpu
                            def _set_cpu(self, value):
                                if value is not None and  not isinstance(value, int):
                                    raise TypeError("cpu must be int")

                                self.__cpu = value
                            cpu = property(_get_cpu, _set_cpu)

                            def _get_memory(self):
                                return self.__memory
                            def _set_memory(self, value):
                                if value is not None and  not isinstance(value, str):
                                    raise TypeError("memory must be str")

                                self.__memory = value
                            memory = property(_get_memory, _set_memory)

                            def _get_pods(self):
                                return self.__pods
                            def _set_pods(self, value):
                                if value is not None and  not isinstance(value, int):
                                    raise TypeError("pods must be int")

                                self.__pods = value
                            pods = property(_get_pods, _set_pods)


                            @staticmethod
                            def from_dict(d):
                                v = {}
                                if "cpu" in d:
                                    v["cpu"] = int.from_dict(d["cpu"]) if hasattr(int, 'from_dict') else d["cpu"]
                                if "memory" in d:
                                    v["memory"] = str.from_dict(d["memory"]) if hasattr(str, 'from_dict') else d["memory"]
                                if "pods" in d:
                                    v["pods"] = int.from_dict(d["pods"]) if hasattr(int, 'from_dict') else d["pods"]
                                return CaasSchema._project._quotas._limits(**v)


                            def as_dict(self):
                                d = {}
                                if self.__cpu is not None:
                                    d['cpu'] = self.__cpu.as_dict() if hasattr(self.__cpu, 'as_dict') else self.__cpu
                                if self.__memory is not None:
                                    d['memory'] = self.__memory.as_dict() if hasattr(self.__memory, 'as_dict') else self.__memory
                                if self.__pods is not None:
                                    d['pods'] = self.__pods.as_dict() if hasattr(self.__pods, 'as_dict') else self.__pods
                                return d

                            def __repr__(self):
                                return "<Class _limits. cpu: {}, memory: {}, pods: {}>".format(limitedRepr(self.__cpu[:20] if isinstance(self.__cpu, bytes) else self.__cpu), limitedRepr(self.__memory[:20] if isinstance(self.__memory, bytes) else self.__memory), limitedRepr(self.__pods[:20] if isinstance(self.__pods, bytes) else self.__pods))

                    class _requests:
                            """
                            OCP request details about cpu, memory and storage
                            """



                            _types_map = {
                                'cpu': {'type': int, 'subtype': None},
                                'memory': {'type': str, 'subtype': None},
                                'rwo': {'type': None, 'subtype': None},
                                'rwx': {'type': None, 'subtype': None},
                            }
                            _formats_map = {
                            }
                            _validations_map = {
                                'cpu': { 'required': False,},
                                'memory': { 'required': False,'pattern': '[0-9]+Gi',},
                                'rwo': { 'required': False,},
                                'rwx': { 'required': False,},
                            }

                            def __init__(self
                                    , cpu=None
                                    , memory=None
                                    , rwo=None
                                    , rwx=None
                                    ):
                                self.__cpu = cpu
                                self.__memory = memory
                                self.__rwo = rwo
                                self.__rwx = rwx
                                pass

                            def _get_cpu(self):
                                return self.__cpu
                            def _set_cpu(self, value):
                                if value is not None and  not isinstance(value, int):
                                    raise TypeError("cpu must be int")

                                self.__cpu = value
                            cpu = property(_get_cpu, _set_cpu)

                            def _get_memory(self):
                                return self.__memory
                            def _set_memory(self, value):
                                if value is not None and  not isinstance(value, str):
                                    raise TypeError("memory must be str")

                                self.__memory = value
                            memory = property(_get_memory, _set_memory)

                            def _get_rwo(self):
                                return self.__rwo
                            def _set_rwo(self, value):
                                
                                self.__rwo = value
                            rwo = property(_get_rwo, _set_rwo)

                            def _get_rwx(self):
                                return self.__rwx
                            def _set_rwx(self, value):
                                
                                self.__rwx = value
                            rwx = property(_get_rwx, _set_rwx)


                            @staticmethod
                            def from_dict(d):
                                v = {}
                                if "cpu" in d:
                                    v["cpu"] = int.from_dict(d["cpu"]) if hasattr(int, 'from_dict') else d["cpu"]
                                if "memory" in d:
                                    v["memory"] = str.from_dict(d["memory"]) if hasattr(str, 'from_dict') else d["memory"]
                                if "rwo" in d:
                                    v["rwo"] = None.from_dict(d["rwo"]) if hasattr(None, 'from_dict') else d["rwo"]
                                if "rwx" in d:
                                    v["rwx"] = None.from_dict(d["rwx"]) if hasattr(None, 'from_dict') else d["rwx"]
                                return CaasSchema._project._quotas._requests(**v)


                            def as_dict(self):
                                d = {}
                                if self.__cpu is not None:
                                    d['cpu'] = self.__cpu.as_dict() if hasattr(self.__cpu, 'as_dict') else self.__cpu
                                if self.__memory is not None:
                                    d['memory'] = self.__memory.as_dict() if hasattr(self.__memory, 'as_dict') else self.__memory
                                if self.__rwo is not None:
                                    d['rwo'] = self.__rwo.as_dict() if hasattr(self.__rwo, 'as_dict') else self.__rwo
                                if self.__rwx is not None:
                                    d['rwx'] = self.__rwx.as_dict() if hasattr(self.__rwx, 'as_dict') else self.__rwx
                                return d

                            def __repr__(self):
                                return "<Class _requests. cpu: {}, memory: {}, rwo: {}, rwx: {}>".format(limitedRepr(self.__cpu[:20] if isinstance(self.__cpu, bytes) else self.__cpu), limitedRepr(self.__memory[:20] if isinstance(self.__memory, bytes) else self.__memory), limitedRepr(self.__rwo[:20] if isinstance(self.__rwo, bytes) else self.__rwo), limitedRepr(self.__rwx[:20] if isinstance(self.__rwx, bytes) else self.__rwx))




                    _types_map = {
                        'limits': {'type': _limits, 'subtype': None},
                        'requests': {'type': _requests, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'limits': { 'required': True,},
                        'requests': { 'required': True,},
                    }

                    def __init__(self
                            , limits=None
                            , requests=None
                            ):
                        """
                        :param limits: OCP limit details about cpu, memory and pods
                        :param requests: OCP request details about cpu, memory and storage
                        """
                        self.__limits = limits
                        self.__requests = requests
                        pass

                    def _get_limits(self):
                        return self.__limits
                    def _set_limits(self, value):
                        if  not isinstance(value, CaasSchema._project._quotas._limits):
                            raise TypeError("limits must be CaasSchema._project._quotas._limits")

                        self.__limits = value
                    limits = property(_get_limits, _set_limits)
                    """
                    OCP limit details about cpu, memory and pods
                    """

                    def _get_requests(self):
                        return self.__requests
                    def _set_requests(self, value):
                        if  not isinstance(value, CaasSchema._project._quotas._requests):
                            raise TypeError("requests must be CaasSchema._project._quotas._requests")

                        self.__requests = value
                    requests = property(_get_requests, _set_requests)
                    """
                    OCP request details about cpu, memory and storage
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "limits" in d:
                            v["limits"] = CaasSchema._project._quotas._limits.from_dict(d["limits"]) if hasattr(CaasSchema._project._quotas._limits, 'from_dict') else d["limits"]
                        if "requests" in d:
                            v["requests"] = CaasSchema._project._quotas._requests.from_dict(d["requests"]) if hasattr(CaasSchema._project._quotas._requests, 'from_dict') else d["requests"]
                        return CaasSchema._project._quotas(**v)


                    def as_dict(self):
                        d = {}
                        if self.__limits is not None:
                            d['limits'] = self.__limits.as_dict() if hasattr(self.__limits, 'as_dict') else self.__limits
                        if self.__requests is not None:
                            d['requests'] = self.__requests.as_dict() if hasattr(self.__requests, 'as_dict') else self.__requests
                        return d

                    def __repr__(self):
                        return "<Class _quotas. limits: {}, requests: {}>".format(limitedRepr(self.__limits[:20] if isinstance(self.__limits, bytes) else self.__limits), limitedRepr(self.__requests[:20] if isinstance(self.__requests, bytes) else self.__requests))




            _types_map = {
                'cluster': {'type': _cluster, 'subtype': None},
                'namespace': {'type': str, 'subtype': None},
                'quotas': {'type': _quotas, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'cluster': { 'required': False,},
                'namespace': { 'required': False,},
                'quotas': { 'required': False,},
            }

            def __init__(self
                    , cluster=None
                    , namespace=None
                    , quotas=None
                    ):
                """
                :param cluster: OCP cluster API URL and location
                :param namespace: Namespace used
                :param quotas: OCP quota details about cpu, memory, pods and storage
                """
                self.__cluster = cluster
                self.__namespace = namespace
                self.__quotas = quotas
                pass

            def _get_cluster(self):
                return self.__cluster
            def _set_cluster(self, value):
                if value is not None and  not isinstance(value, CaasSchema._project._cluster):
                    raise TypeError("cluster must be CaasSchema._project._cluster")

                self.__cluster = value
            cluster = property(_get_cluster, _set_cluster)
            """
            OCP cluster API URL and location
            """

            def _get_namespace(self):
                return self.__namespace
            def _set_namespace(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("namespace must be str")

                self.__namespace = value
            namespace = property(_get_namespace, _set_namespace)
            """
            Namespace used
            """

            def _get_quotas(self):
                return self.__quotas
            def _set_quotas(self, value):
                if value is not None and  not isinstance(value, CaasSchema._project._quotas):
                    raise TypeError("quotas must be CaasSchema._project._quotas")

                self.__quotas = value
            quotas = property(_get_quotas, _set_quotas)
            """
            OCP quota details about cpu, memory, pods and storage
            """


            @staticmethod
            def from_dict(d):
                v = {}
                if "cluster" in d:
                    v["cluster"] = CaasSchema._project._cluster.from_dict(d["cluster"]) if hasattr(CaasSchema._project._cluster, 'from_dict') else d["cluster"]
                if "namespace" in d:
                    v["namespace"] = str.from_dict(d["namespace"]) if hasattr(str, 'from_dict') else d["namespace"]
                if "quotas" in d:
                    v["quotas"] = CaasSchema._project._quotas.from_dict(d["quotas"]) if hasattr(CaasSchema._project._quotas, 'from_dict') else d["quotas"]
                return CaasSchema._project(**v)


            def as_dict(self):
                d = {}
                if self.__cluster is not None:
                    d['cluster'] = self.__cluster.as_dict() if hasattr(self.__cluster, 'as_dict') else self.__cluster
                if self.__namespace is not None:
                    d['namespace'] = self.__namespace.as_dict() if hasattr(self.__namespace, 'as_dict') else self.__namespace
                if self.__quotas is not None:
                    d['quotas'] = self.__quotas.as_dict() if hasattr(self.__quotas, 'as_dict') else self.__quotas
                return d

            def __repr__(self):
                return "<Class _project. cluster: {}, namespace: {}, quotas: {}>".format(limitedRepr(self.__cluster[:20] if isinstance(self.__cluster, bytes) else self.__cluster), limitedRepr(self.__namespace[:20] if isinstance(self.__namespace, bytes) else self.__namespace), limitedRepr(self.__quotas[:20] if isinstance(self.__quotas, bytes) else self.__quotas))

    class _caas:
            class _platform:
                    """
                    Platform name and version
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                        'apiVersions': {'type': list, 'subtype': str},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'version': { 'required': False,'pattern': '[0-9.]',},
                        'apiVersions': { 'required': False,},
                    }

                    def __init__(self
                            , name='OCP'
                            , version=None
                            , apiVersions=None
                            ):
                        """
                        :param apiVersions: Output of oc api-versions command
                        """
                        self.__name = name
                        self.__version = version
                        self.__apiVersions = apiVersions
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)

                    def _get_apiVersions(self):
                        return self.__apiVersions
                    def _set_apiVersions(self, value):
                        if value is not None and  not isinstance(value, list):
                            raise TypeError("apiVersions must be list")
                        if value is not None and  not all(isinstance(i, str) for i in value):
                            raise TypeError("apiVersions list values must be str")

                        self.__apiVersions = value
                    apiVersions = property(_get_apiVersions, _set_apiVersions)
                    """
                    Output of oc api-versions command
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        if "apiVersions" in d:
                            v["apiVersions"] = [str.from_dict(p) if hasattr(str, 'from_dict') else p for p in d["apiVersions"]]
                        return CaasSchema._caas._platform(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        if self.__apiVersions is not None:
                            d['apiVersions'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__apiVersions]
                        return d

                    def __repr__(self):
                        return "<Class _platform. name: {}, version: {}, apiVersions: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__apiVersions[:20] if isinstance(self.__apiVersions, bytes) else self.__apiVersions))

            class _loadBalancer:
                    """
                    Tool name and version
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'version': { 'required': False,'pattern': '[0-9.]',},
                    }

                    def __init__(self
                            , name=None
                            , version=None
                            ):
                        self.__name = name
                        self.__version = version
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        return CaasSchema._caas._loadBalancer(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        return d

                    def __repr__(self):
                        return "<Class _loadBalancer. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))

            class _cri:
                    """
                    CRI tool and version
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'version': { 'required': False,'pattern': '[0-9.]',},
                    }

                    def __init__(self
                            , name=None
                            , version=None
                            ):
                        self.__name = name
                        self.__version = version
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        return CaasSchema._caas._cri(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        return d

                    def __repr__(self):
                        return "<Class _cri. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))

            class _cni:
                    """
                    CNI tool and version
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'version': { 'required': False,'pattern': '[0-9.]',},
                    }

                    def __init__(self
                            , name=None
                            , version=None
                            ):
                        self.__name = name
                        self.__version = version
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        return CaasSchema._caas._cni(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        return d

                    def __repr__(self):
                        return "<Class _cni. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))

            class _csi:
                    """
                    CSI tool and version
                    """



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'version': { 'required': False,'pattern': '[0-9.]',},
                    }

                    def __init__(self
                            , name=None
                            , version=None
                            ):
                        self.__name = name
                        self.__version = version
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        return CaasSchema._caas._csi(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        return d

                    def __repr__(self):
                        return "<Class _csi. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))

            class _os:



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'version': { 'required': False,'pattern': '[0-9.]',},
                    }

                    def __init__(self
                            , name=None
                            , version=None
                            ):
                        self.__name = name
                        self.__version = version
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        return CaasSchema._caas._os(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        return d

                    def __repr__(self):
                        return "<Class _os. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))

            class _monitoring:



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'version': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'version': { 'required': False,'pattern': '[0-9.]',},
                    }

                    def __init__(self
                            , name=None
                            , version=None
                            ):
                        self.__name = name
                        self.__version = version
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_version(self):
                        return self.__version
                    def _set_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("version must be str")

                        self.__version = value
                    version = property(_get_version, _set_version)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "version" in d:
                            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                        return CaasSchema._caas._monitoring(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__version is not None:
                            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                        return d

                    def __repr__(self):
                        return "<Class _monitoring. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))




            _types_map = {
                'platform': {'type': _platform, 'subtype': None},
                'k8s': {'type': str, 'subtype': None},
                'loadBalancer': {'type': _loadBalancer, 'subtype': None},
                'cri': {'type': _cri, 'subtype': None},
                'cni': {'type': _cni, 'subtype': None},
                'csi': {'type': _csi, 'subtype': None},
                'os': {'type': _os, 'subtype': None},
                'monitoring': {'type': list, 'subtype': _monitoring},
            }
            _formats_map = {
            }
            _validations_map = {
                'platform': { 'required': False,},
                'k8s': { 'required': False,'pattern': '[0-9.]',},
                'loadBalancer': { 'required': False,},
                'cri': { 'required': False,},
                'cni': { 'required': False,},
                'csi': { 'required': False,},
                'os': { 'required': False,},
                'monitoring': { 'required': False,},
            }

            def __init__(self
                    , platform=None
                    , k8s=None
                    , loadBalancer=None
                    , cri=None
                    , cni=None
                    , csi=None
                    , os=None
                    , monitoring=None
                    ):
                """
                :param platform: Platform name and version
                :param k8s: Kubernetes Server version
                :param loadBalancer: Tool name and version
                :param cri: CRI tool and version
                :param cni: CNI tool and version
                :param csi: CSI tool and version
                """
                self.__platform = platform
                self.__k8s = k8s
                self.__loadBalancer = loadBalancer
                self.__cri = cri
                self.__cni = cni
                self.__csi = csi
                self.__os = os
                self.__monitoring = monitoring
                pass

            def _get_platform(self):
                return self.__platform
            def _set_platform(self, value):
                if value is not None and  not isinstance(value, CaasSchema._caas._platform):
                    raise TypeError("platform must be CaasSchema._caas._platform")

                self.__platform = value
            platform = property(_get_platform, _set_platform)
            """
            Platform name and version
            """

            def _get_k8s(self):
                return self.__k8s
            def _set_k8s(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("k8s must be str")

                self.__k8s = value
            k8s = property(_get_k8s, _set_k8s)
            """
            Kubernetes Server version
            """

            def _get_loadBalancer(self):
                return self.__loadBalancer
            def _set_loadBalancer(self, value):
                if value is not None and  not isinstance(value, CaasSchema._caas._loadBalancer):
                    raise TypeError("loadBalancer must be CaasSchema._caas._loadBalancer")

                self.__loadBalancer = value
            loadBalancer = property(_get_loadBalancer, _set_loadBalancer)
            """
            Tool name and version
            """

            def _get_cri(self):
                return self.__cri
            def _set_cri(self, value):
                if value is not None and  not isinstance(value, CaasSchema._caas._cri):
                    raise TypeError("cri must be CaasSchema._caas._cri")

                self.__cri = value
            cri = property(_get_cri, _set_cri)
            """
            CRI tool and version
            """

            def _get_cni(self):
                return self.__cni
            def _set_cni(self, value):
                if value is not None and  not isinstance(value, CaasSchema._caas._cni):
                    raise TypeError("cni must be CaasSchema._caas._cni")

                self.__cni = value
            cni = property(_get_cni, _set_cni)
            """
            CNI tool and version
            """

            def _get_csi(self):
                return self.__csi
            def _set_csi(self, value):
                if value is not None and  not isinstance(value, CaasSchema._caas._csi):
                    raise TypeError("csi must be CaasSchema._caas._csi")

                self.__csi = value
            csi = property(_get_csi, _set_csi)
            """
            CSI tool and version
            """

            def _get_os(self):
                return self.__os
            def _set_os(self, value):
                if value is not None and  not isinstance(value, CaasSchema._caas._os):
                    raise TypeError("os must be CaasSchema._caas._os")

                self.__os = value
            os = property(_get_os, _set_os)

            def _get_monitoring(self):
                return self.__monitoring
            def _set_monitoring(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("monitoring must be list")
                if value is not None and  not all(isinstance(i, CaasSchema._caas._monitoring) for i in value):
                    raise TypeError("monitoring list values must be CaasSchema._caas._monitoring")

                self.__monitoring = value
            monitoring = property(_get_monitoring, _set_monitoring)


            @staticmethod
            def from_dict(d):
                v = {}
                if "platform" in d:
                    v["platform"] = CaasSchema._caas._platform.from_dict(d["platform"]) if hasattr(CaasSchema._caas._platform, 'from_dict') else d["platform"]
                if "k8s" in d:
                    v["k8s"] = str.from_dict(d["k8s"]) if hasattr(str, 'from_dict') else d["k8s"]
                if "loadBalancer" in d:
                    v["loadBalancer"] = CaasSchema._caas._loadBalancer.from_dict(d["loadBalancer"]) if hasattr(CaasSchema._caas._loadBalancer, 'from_dict') else d["loadBalancer"]
                if "cri" in d:
                    v["cri"] = CaasSchema._caas._cri.from_dict(d["cri"]) if hasattr(CaasSchema._caas._cri, 'from_dict') else d["cri"]
                if "cni" in d:
                    v["cni"] = CaasSchema._caas._cni.from_dict(d["cni"]) if hasattr(CaasSchema._caas._cni, 'from_dict') else d["cni"]
                if "csi" in d:
                    v["csi"] = CaasSchema._caas._csi.from_dict(d["csi"]) if hasattr(CaasSchema._caas._csi, 'from_dict') else d["csi"]
                if "os" in d:
                    v["os"] = CaasSchema._caas._os.from_dict(d["os"]) if hasattr(CaasSchema._caas._os, 'from_dict') else d["os"]
                if "monitoring" in d:
                    v["monitoring"] = [CaasSchema._caas._monitoring.from_dict(p) if hasattr(CaasSchema._caas._monitoring, 'from_dict') else p for p in d["monitoring"]]
                return CaasSchema._caas(**v)


            def as_dict(self):
                d = {}
                if self.__platform is not None:
                    d['platform'] = self.__platform.as_dict() if hasattr(self.__platform, 'as_dict') else self.__platform
                if self.__k8s is not None:
                    d['k8s'] = self.__k8s.as_dict() if hasattr(self.__k8s, 'as_dict') else self.__k8s
                if self.__loadBalancer is not None:
                    d['loadBalancer'] = self.__loadBalancer.as_dict() if hasattr(self.__loadBalancer, 'as_dict') else self.__loadBalancer
                if self.__cri is not None:
                    d['cri'] = self.__cri.as_dict() if hasattr(self.__cri, 'as_dict') else self.__cri
                if self.__cni is not None:
                    d['cni'] = self.__cni.as_dict() if hasattr(self.__cni, 'as_dict') else self.__cni
                if self.__csi is not None:
                    d['csi'] = self.__csi.as_dict() if hasattr(self.__csi, 'as_dict') else self.__csi
                if self.__os is not None:
                    d['os'] = self.__os.as_dict() if hasattr(self.__os, 'as_dict') else self.__os
                if self.__monitoring is not None:
                    d['monitoring'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monitoring]
                return d

            def __repr__(self):
                return "<Class _caas. platform: {}, k8s: {}, loadBalancer: {}, cri: {}, cni: {}, csi: {}, os: {}, monitoring: {}>".format(limitedRepr(self.__platform[:20] if isinstance(self.__platform, bytes) else self.__platform), limitedRepr(self.__k8s[:20] if isinstance(self.__k8s, bytes) else self.__k8s), limitedRepr(self.__loadBalancer[:20] if isinstance(self.__loadBalancer, bytes) else self.__loadBalancer), limitedRepr(self.__cri[:20] if isinstance(self.__cri, bytes) else self.__cri), limitedRepr(self.__cni[:20] if isinstance(self.__cni, bytes) else self.__cni), limitedRepr(self.__csi[:20] if isinstance(self.__csi, bytes) else self.__csi), limitedRepr(self.__os[:20] if isinstance(self.__os, bytes) else self.__os), limitedRepr(self.__monitoring[:20] if isinstance(self.__monitoring, bytes) else self.__monitoring))

    class _paas:
            """
            Used CNCF model
            """



            _types_map = {
                'category': {'type': str, 'subtype': None},
                'product': {'type': str, 'subtype': None},
                'name': {'type': str, 'subtype': None},
                'version': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'category': { 'required': False,},
                'product': { 'required': False,},
                'name': { 'required': False,},
                'version': { 'required': False,'pattern': '[0-9.]',},
            }

            def __init__(self
                    , category=None
                    , product=None
                    , name=None
                    , version=None
                    ):
                self.__category = category
                self.__product = product
                self.__name = name
                self.__version = version
                pass

            def _get_category(self):
                return self.__category
            def _set_category(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("category must be str")

                self.__category = value
            category = property(_get_category, _set_category)

            def _get_product(self):
                return self.__product
            def _set_product(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("product must be str")

                self.__product = value
            product = property(_get_product, _set_product)

            def _get_name(self):
                return self.__name
            def _set_name(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("name must be str")

                self.__name = value
            name = property(_get_name, _set_name)

            def _get_version(self):
                return self.__version
            def _set_version(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("version must be str")

                self.__version = value
            version = property(_get_version, _set_version)


            @staticmethod
            def from_dict(d):
                v = {}
                if "category" in d:
                    v["category"] = str.from_dict(d["category"]) if hasattr(str, 'from_dict') else d["category"]
                if "product" in d:
                    v["product"] = str.from_dict(d["product"]) if hasattr(str, 'from_dict') else d["product"]
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "version" in d:
                    v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                return CaasSchema._paas(**v)


            def as_dict(self):
                d = {}
                if self.__category is not None:
                    d['category'] = self.__category.as_dict() if hasattr(self.__category, 'as_dict') else self.__category
                if self.__product is not None:
                    d['product'] = self.__product.as_dict() if hasattr(self.__product, 'as_dict') else self.__product
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__version is not None:
                    d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                return d

            def __repr__(self):
                return "<Class _paas. category: {}, product: {}, name: {}, version: {}>".format(limitedRepr(self.__category[:20] if isinstance(self.__category, bytes) else self.__category), limitedRepr(self.__product[:20] if isinstance(self.__product, bytes) else self.__product), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))

    class _iaas:



            _types_map = {
                'name': {'type': str, 'subtype': None},
                'version': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'name': { 'required': False,},
                'version': { 'required': False,'pattern': '[0-9.]',},
            }

            def __init__(self
                    , name=None
                    , version=None
                    ):
                self.__name = name
                self.__version = version
                pass

            def _get_name(self):
                return self.__name
            def _set_name(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("name must be str")

                self.__name = value
            name = property(_get_name, _set_name)

            def _get_version(self):
                return self.__version
            def _set_version(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("version must be str")

                self.__version = value
            version = property(_get_version, _set_version)


            @staticmethod
            def from_dict(d):
                v = {}
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "version" in d:
                    v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                return CaasSchema._iaas(**v)


            def as_dict(self):
                d = {}
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__version is not None:
                    d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                return d

            def __repr__(self):
                return "<Class _iaas. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'ident': {'type': identifier, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'history': {'type': list, 'subtype': event},
        'tags': {'type': list, 'subtype': str},
        'status': {'type': str, 'subtype': None},
        'project': {'type': _project, 'subtype': None},
        'caas': {'type': _caas, 'subtype': None},
        'paas': {'type': list, 'subtype': _paas},
        'iaas': {'type': _iaas, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'schema': { 'required': True,},
        'ident': { 'required': True,},
        'description': { 'required': False,},
        'history': { 'required': False,},
        'tags': { 'required': False,},
        'status': { 'required': True,},
        'project': { 'required': False,},
        'caas': { 'required': False,},
        'paas': { 'required': False,},
        'iaas': { 'required': False,},
    }

    def __init__(self
            , *args
            , schema=None
            , ident=None
            , description=None
            , history=None
            , tags=None
            , status='Present'
            , project=None
            , caas=None
            , paas=None
            , iaas=None
            , **kwargs
            ):
        self.__schema = schema
        self.__ident = ident
        self.__description = description
        self.__history = history
        self.__tags = tags
        self.__status = status
        self.__project = project
        self.__caas = caas
        self.__paas = paas
        self.__iaas = iaas
        super().__init__(*args, **kwargs)
        pass

    def _get_schema(self):
        return self.__schema
    def _set_schema(self, value):
        if  not isinstance(value, str):
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

    def _get_description(self):
        return self.__description
    def _set_description(self, value):
        if value is not None and  not isinstance(value, str):
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

    def _get_project(self):
        return self.__project
    def _set_project(self, value):
        if value is not None and  not isinstance(value, CaasSchema._project):
            raise TypeError("project must be CaasSchema._project")

        self.__project = value
    project = property(_get_project, _set_project)

    def _get_caas(self):
        return self.__caas
    def _set_caas(self, value):
        if value is not None and  not isinstance(value, CaasSchema._caas):
            raise TypeError("caas must be CaasSchema._caas")

        self.__caas = value
    caas = property(_get_caas, _set_caas)

    def _get_paas(self):
        return self.__paas
    def _set_paas(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("paas must be list")
        if value is not None and  not all(isinstance(i, CaasSchema._paas) for i in value):
            raise TypeError("paas list values must be CaasSchema._paas")

        self.__paas = value
    paas = property(_get_paas, _set_paas)

    def _get_iaas(self):
        return self.__iaas
    def _set_iaas(self, value):
        if value is not None and  not isinstance(value, CaasSchema._iaas):
            raise TypeError("iaas must be CaasSchema._iaas")

        self.__iaas = value
    iaas = property(_get_iaas, _set_iaas)


    @staticmethod
    def from_dict(d):
        v = d.copy()
        if "schema" in d:
            v["schema"] = str.from_dict(d["schema"]) if hasattr(str, 'from_dict') else d["schema"]
        if "ident" in d:
            v["ident"] = identifier.from_dict(d["ident"]) if hasattr(identifier, 'from_dict') else d["ident"]
        if "description" in d:
            v["description"] = str.from_dict(d["description"]) if hasattr(str, 'from_dict') else d["description"]
        if "history" in d:
            v["history"] = [event.from_dict(p) if hasattr(event, 'from_dict') else p for p in d["history"]]
        if "tags" in d:
            v["tags"] = [str.from_dict(p) if hasattr(str, 'from_dict') else p for p in d["tags"]]
        if "status" in d:
            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
        if "project" in d:
            v["project"] = CaasSchema._project.from_dict(d["project"]) if hasattr(CaasSchema._project, 'from_dict') else d["project"]
        if "caas" in d:
            v["caas"] = CaasSchema._caas.from_dict(d["caas"]) if hasattr(CaasSchema._caas, 'from_dict') else d["caas"]
        if "paas" in d:
            v["paas"] = [CaasSchema._paas.from_dict(p) if hasattr(CaasSchema._paas, 'from_dict') else p for p in d["paas"]]
        if "iaas" in d:
            v["iaas"] = CaasSchema._iaas.from_dict(d["iaas"]) if hasattr(CaasSchema._iaas, 'from_dict') else d["iaas"]
        return CaasSchema(**v)


    def as_dict(self):
        d = super().as_dict()
        if self.__schema is not None:
            d['schema'] = self.__schema.as_dict() if hasattr(self.__schema, 'as_dict') else self.__schema
        if self.__ident is not None:
            d['ident'] = self.__ident.as_dict() if hasattr(self.__ident, 'as_dict') else self.__ident
        if self.__description is not None:
            d['description'] = self.__description.as_dict() if hasattr(self.__description, 'as_dict') else self.__description
        if self.__history is not None:
            d['history'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__history]
        if self.__tags is not None:
            d['tags'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__tags]
        if self.__status is not None:
            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
        if self.__project is not None:
            d['project'] = self.__project.as_dict() if hasattr(self.__project, 'as_dict') else self.__project
        if self.__caas is not None:
            d['caas'] = self.__caas.as_dict() if hasattr(self.__caas, 'as_dict') else self.__caas
        if self.__paas is not None:
            d['paas'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__paas]
        if self.__iaas is not None:
            d['iaas'] = self.__iaas.as_dict() if hasattr(self.__iaas, 'as_dict') else self.__iaas
        return d

    def __repr__(self):
        return "<Class CaasSchema. schema: {}, ident: {}, description: {}, history: {}, tags: {}, status: {}, project: {}, caas: {}, paas: {}, iaas: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__ident[:20] if isinstance(self.__ident, bytes) else self.__ident), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__history[:20] if isinstance(self.__history, bytes) else self.__history), limitedRepr(self.__tags[:20] if isinstance(self.__tags, bytes) else self.__tags), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status), limitedRepr(self.__project[:20] if isinstance(self.__project, bytes) else self.__project), limitedRepr(self.__caas[:20] if isinstance(self.__caas, bytes) else self.__caas), limitedRepr(self.__paas[:20] if isinstance(self.__paas, bytes) else self.__paas), limitedRepr(self.__iaas[:20] if isinstance(self.__iaas, bytes) else self.__iaas))

