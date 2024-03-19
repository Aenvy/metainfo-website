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

class ResultSchema(MetainfoBase):
    """
    The result schema describe a test result
    """
    class _env:
            class _system:



                    _types_map = {
                        'os': {'type': str, 'subtype': None},
                        'k8s': {'type': str, 'subtype': None},
                        'helm': {'type': str, 'subtype': None},
                        'CNI': {'type': str, 'subtype': None},
                        'CSI': {'type': str, 'subtype': None},
                        'CRI': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'os': { 'required': False,},
                        'k8s': { 'required': False,},
                        'helm': { 'required': False,},
                        'CNI': { 'required': False,},
                        'CSI': { 'required': False,},
                        'CRI': { 'required': False,},
                    }

                    def __init__(self
                            , os=None
                            , k8s=None
                            , helm=None
                            , CNI=None
                            , CSI=None
                            , CRI=None
                            ):
                        self.__os = os
                        self.__k8s = k8s
                        self.__helm = helm
                        self.__CNI = CNI
                        self.__CSI = CSI
                        self.__CRI = CRI
                        pass

                    def _get_os(self):
                        return self.__os
                    def _set_os(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("os must be str")

                        self.__os = value
                    os = property(_get_os, _set_os)

                    def _get_k8s(self):
                        return self.__k8s
                    def _set_k8s(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("k8s must be str")

                        self.__k8s = value
                    k8s = property(_get_k8s, _set_k8s)

                    def _get_helm(self):
                        return self.__helm
                    def _set_helm(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("helm must be str")

                        self.__helm = value
                    helm = property(_get_helm, _set_helm)

                    def _get_CNI(self):
                        return self.__CNI
                    def _set_CNI(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("CNI must be str")

                        self.__CNI = value
                    CNI = property(_get_CNI, _set_CNI)

                    def _get_CSI(self):
                        return self.__CSI
                    def _set_CSI(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("CSI must be str")

                        self.__CSI = value
                    CSI = property(_get_CSI, _set_CSI)

                    def _get_CRI(self):
                        return self.__CRI
                    def _set_CRI(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("CRI must be str")

                        self.__CRI = value
                    CRI = property(_get_CRI, _set_CRI)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "os" in d:
                            v["os"] = str.from_dict(d["os"]) if hasattr(str, 'from_dict') else d["os"]
                        if "k8s" in d:
                            v["k8s"] = str.from_dict(d["k8s"]) if hasattr(str, 'from_dict') else d["k8s"]
                        if "helm" in d:
                            v["helm"] = str.from_dict(d["helm"]) if hasattr(str, 'from_dict') else d["helm"]
                        if "CNI" in d:
                            v["CNI"] = str.from_dict(d["CNI"]) if hasattr(str, 'from_dict') else d["CNI"]
                        if "CSI" in d:
                            v["CSI"] = str.from_dict(d["CSI"]) if hasattr(str, 'from_dict') else d["CSI"]
                        if "CRI" in d:
                            v["CRI"] = str.from_dict(d["CRI"]) if hasattr(str, 'from_dict') else d["CRI"]
                        return ResultSchema._env._system(**v)


                    def as_dict(self):
                        d = {}
                        if self.__os is not None:
                            d['os'] = self.__os.as_dict() if hasattr(self.__os, 'as_dict') else self.__os
                        if self.__k8s is not None:
                            d['k8s'] = self.__k8s.as_dict() if hasattr(self.__k8s, 'as_dict') else self.__k8s
                        if self.__helm is not None:
                            d['helm'] = self.__helm.as_dict() if hasattr(self.__helm, 'as_dict') else self.__helm
                        if self.__CNI is not None:
                            d['CNI'] = self.__CNI.as_dict() if hasattr(self.__CNI, 'as_dict') else self.__CNI
                        if self.__CSI is not None:
                            d['CSI'] = self.__CSI.as_dict() if hasattr(self.__CSI, 'as_dict') else self.__CSI
                        if self.__CRI is not None:
                            d['CRI'] = self.__CRI.as_dict() if hasattr(self.__CRI, 'as_dict') else self.__CRI
                        return d

                    def __repr__(self):
                        return "<Class _system. os: {}, k8s: {}, helm: {}, CNI: {}, CSI: {}, CRI: {}>".format(limitedRepr(self.__os[:20] if isinstance(self.__os, bytes) else self.__os), limitedRepr(self.__k8s[:20] if isinstance(self.__k8s, bytes) else self.__k8s), limitedRepr(self.__helm[:20] if isinstance(self.__helm, bytes) else self.__helm), limitedRepr(self.__CNI[:20] if isinstance(self.__CNI, bytes) else self.__CNI), limitedRepr(self.__CSI[:20] if isinstance(self.__CSI, bytes) else self.__CSI), limitedRepr(self.__CRI[:20] if isinstance(self.__CRI, bytes) else self.__CRI))

            class _services:



                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'namespace': {'type': str, 'subtype': None},
                        'chart': {'type': str, 'subtype': None},
                        'appversion': {'type': str, 'subtype': None},
                        'status': {'type': str, 'subtype': None},
                        'revision': {'type': int, 'subtype': None},
                        'updated': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                        'updated': 'date-time',
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'namespace': { 'required': False,},
                        'chart': { 'required': False,},
                        'appversion': { 'required': False,},
                        'status': { 'required': False,},
                        'revision': { 'required': False,'minimum': 1,},
                        'updated': { 'required': False,},
                    }

                    def __init__(self
                            , name=None
                            , namespace=None
                            , chart=None
                            , appversion=None
                            , status=None
                            , revision=None
                            , updated=None
                            ):
                        self.__name = name
                        self.__namespace = namespace
                        self.__chart = chart
                        self.__appversion = appversion
                        self.__status = status
                        self.__revision = revision
                        self.__updated = updated
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_namespace(self):
                        return self.__namespace
                    def _set_namespace(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("namespace must be str")

                        self.__namespace = value
                    namespace = property(_get_namespace, _set_namespace)

                    def _get_chart(self):
                        return self.__chart
                    def _set_chart(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("chart must be str")

                        self.__chart = value
                    chart = property(_get_chart, _set_chart)

                    def _get_appversion(self):
                        return self.__appversion
                    def _set_appversion(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("appversion must be str")

                        self.__appversion = value
                    appversion = property(_get_appversion, _set_appversion)

                    def _get_status(self):
                        return self.__status
                    def _set_status(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("status must be str")

                        self.__status = value
                    status = property(_get_status, _set_status)

                    def _get_revision(self):
                        return self.__revision
                    def _set_revision(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("revision must be int")

                        self.__revision = value
                    revision = property(_get_revision, _set_revision)

                    def _get_updated(self):
                        return self.__updated
                    def _set_updated(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("updated must be str")

                        self.__updated = value
                    updated = property(_get_updated, _set_updated)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "namespace" in d:
                            v["namespace"] = str.from_dict(d["namespace"]) if hasattr(str, 'from_dict') else d["namespace"]
                        if "chart" in d:
                            v["chart"] = str.from_dict(d["chart"]) if hasattr(str, 'from_dict') else d["chart"]
                        if "appversion" in d:
                            v["appversion"] = str.from_dict(d["appversion"]) if hasattr(str, 'from_dict') else d["appversion"]
                        if "status" in d:
                            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
                        if "revision" in d:
                            v["revision"] = int.from_dict(d["revision"]) if hasattr(int, 'from_dict') else d["revision"]
                        if "updated" in d:
                            v["updated"] = str.from_dict(d["updated"]) if hasattr(str, 'from_dict') else d["updated"]
                        return ResultSchema._env._services(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__namespace is not None:
                            d['namespace'] = self.__namespace.as_dict() if hasattr(self.__namespace, 'as_dict') else self.__namespace
                        if self.__chart is not None:
                            d['chart'] = self.__chart.as_dict() if hasattr(self.__chart, 'as_dict') else self.__chart
                        if self.__appversion is not None:
                            d['appversion'] = self.__appversion.as_dict() if hasattr(self.__appversion, 'as_dict') else self.__appversion
                        if self.__status is not None:
                            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
                        if self.__revision is not None:
                            d['revision'] = self.__revision.as_dict() if hasattr(self.__revision, 'as_dict') else self.__revision
                        if self.__updated is not None:
                            d['updated'] = self.__updated.as_dict() if hasattr(self.__updated, 'as_dict') else self.__updated
                        return d

                    def __repr__(self):
                        return "<Class _services. name: {}, namespace: {}, chart: {}, appversion: {}, status: {}, revision: {}, updated: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__namespace[:20] if isinstance(self.__namespace, bytes) else self.__namespace), limitedRepr(self.__chart[:20] if isinstance(self.__chart, bytes) else self.__chart), limitedRepr(self.__appversion[:20] if isinstance(self.__appversion, bytes) else self.__appversion), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status), limitedRepr(self.__revision[:20] if isinstance(self.__revision, bytes) else self.__revision), limitedRepr(self.__updated[:20] if isinstance(self.__updated, bytes) else self.__updated))

            class _pods:
                    class _containers:
                            class _ports:



                                    _types_map = {
                                        'name': {'type': str, 'subtype': None},
                                        'protocol': {'type': str, 'subtype': None},
                                        'containerPort': {'type': str, 'subtype': None},
                                    }
                                    _formats_map = {
                                    }
                                    _validations_map = {
                                        'name': { 'required': False,},
                                        'protocol': { 'required': False,},
                                        'containerPort': { 'required': False,},
                                    }

                                    def __init__(self
                                            , name=None
                                            , protocol=None
                                            , containerPort=None
                                            ):
                                        self.__name = name
                                        self.__protocol = protocol
                                        self.__containerPort = containerPort
                                        pass

                                    def _get_name(self):
                                        return self.__name
                                    def _set_name(self, value):
                                        if value is not None and  not isinstance(value, str):
                                            raise TypeError("name must be str")

                                        self.__name = value
                                    name = property(_get_name, _set_name)

                                    def _get_protocol(self):
                                        return self.__protocol
                                    def _set_protocol(self, value):
                                        if value is not None and  not isinstance(value, str):
                                            raise TypeError("protocol must be str")

                                        self.__protocol = value
                                    protocol = property(_get_protocol, _set_protocol)

                                    def _get_containerPort(self):
                                        return self.__containerPort
                                    def _set_containerPort(self, value):
                                        if value is not None and  not isinstance(value, str):
                                            raise TypeError("containerPort must be str")

                                        self.__containerPort = value
                                    containerPort = property(_get_containerPort, _set_containerPort)


                                    @staticmethod
                                    def from_dict(d):
                                        v = {}
                                        if "name" in d:
                                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                                        if "protocol" in d:
                                            v["protocol"] = str.from_dict(d["protocol"]) if hasattr(str, 'from_dict') else d["protocol"]
                                        if "containerPort" in d:
                                            v["containerPort"] = str.from_dict(d["containerPort"]) if hasattr(str, 'from_dict') else d["containerPort"]
                                        return ResultSchema._env._pods._containers._ports(**v)


                                    def as_dict(self):
                                        d = {}
                                        if self.__name is not None:
                                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                                        if self.__protocol is not None:
                                            d['protocol'] = self.__protocol.as_dict() if hasattr(self.__protocol, 'as_dict') else self.__protocol
                                        if self.__containerPort is not None:
                                            d['containerPort'] = self.__containerPort.as_dict() if hasattr(self.__containerPort, 'as_dict') else self.__containerPort
                                        return d

                                    def __repr__(self):
                                        return "<Class _ports. name: {}, protocol: {}, containerPort: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__protocol[:20] if isinstance(self.__protocol, bytes) else self.__protocol), limitedRepr(self.__containerPort[:20] if isinstance(self.__containerPort, bytes) else self.__containerPort))

                            class _volumeMounts:



                                    _types_map = {
                                        'name': {'type': str, 'subtype': None},
                                        'mountPath': {'type': str, 'subtype': None},
                                    }
                                    _formats_map = {
                                    }
                                    _validations_map = {
                                        'name': { 'required': False,},
                                        'mountPath': { 'required': False,},
                                    }

                                    def __init__(self
                                            , name=None
                                            , mountPath=None
                                            ):
                                        self.__name = name
                                        self.__mountPath = mountPath
                                        pass

                                    def _get_name(self):
                                        return self.__name
                                    def _set_name(self, value):
                                        if value is not None and  not isinstance(value, str):
                                            raise TypeError("name must be str")

                                        self.__name = value
                                    name = property(_get_name, _set_name)

                                    def _get_mountPath(self):
                                        return self.__mountPath
                                    def _set_mountPath(self, value):
                                        if value is not None and  not isinstance(value, str):
                                            raise TypeError("mountPath must be str")

                                        self.__mountPath = value
                                    mountPath = property(_get_mountPath, _set_mountPath)


                                    @staticmethod
                                    def from_dict(d):
                                        v = {}
                                        if "name" in d:
                                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                                        if "mountPath" in d:
                                            v["mountPath"] = str.from_dict(d["mountPath"]) if hasattr(str, 'from_dict') else d["mountPath"]
                                        return ResultSchema._env._pods._containers._volumeMounts(**v)


                                    def as_dict(self):
                                        d = {}
                                        if self.__name is not None:
                                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                                        if self.__mountPath is not None:
                                            d['mountPath'] = self.__mountPath.as_dict() if hasattr(self.__mountPath, 'as_dict') else self.__mountPath
                                        return d

                                    def __repr__(self):
                                        return "<Class _volumeMounts. name: {}, mountPath: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__mountPath[:20] if isinstance(self.__mountPath, bytes) else self.__mountPath))




                            _types_map = {
                                'name': {'type': str, 'subtype': None},
                                'image': {'type': str, 'subtype': None},
                                'ports': {'type': list, 'subtype': _ports},
                                'volumeMounts': {'type': list, 'subtype': _volumeMounts},
                            }
                            _formats_map = {
                            }
                            _validations_map = {
                                'name': { 'required': False,},
                                'image': { 'required': False,},
                                'ports': { 'required': False,},
                                'volumeMounts': { 'required': False,},
                            }

                            def __init__(self
                                    , name=None
                                    , image=None
                                    , ports=None
                                    , volumeMounts=None
                                    ):
                                self.__name = name
                                self.__image = image
                                self.__ports = ports
                                self.__volumeMounts = volumeMounts
                                pass

                            def _get_name(self):
                                return self.__name
                            def _set_name(self, value):
                                if value is not None and  not isinstance(value, str):
                                    raise TypeError("name must be str")

                                self.__name = value
                            name = property(_get_name, _set_name)

                            def _get_image(self):
                                return self.__image
                            def _set_image(self, value):
                                if value is not None and  not isinstance(value, str):
                                    raise TypeError("image must be str")

                                self.__image = value
                            image = property(_get_image, _set_image)

                            def _get_ports(self):
                                return self.__ports
                            def _set_ports(self, value):
                                if value is not None and  not isinstance(value, list):
                                    raise TypeError("ports must be list")
                                if value is not None and  not all(isinstance(i, ResultSchema._env._pods._containers._ports) for i in value):
                                    raise TypeError("ports list values must be ResultSchema._env._pods._containers._ports")

                                self.__ports = value
                            ports = property(_get_ports, _set_ports)

                            def _get_volumeMounts(self):
                                return self.__volumeMounts
                            def _set_volumeMounts(self, value):
                                if value is not None and  not isinstance(value, list):
                                    raise TypeError("volumeMounts must be list")
                                if value is not None and  not all(isinstance(i, ResultSchema._env._pods._containers._volumeMounts) for i in value):
                                    raise TypeError("volumeMounts list values must be ResultSchema._env._pods._containers._volumeMounts")

                                self.__volumeMounts = value
                            volumeMounts = property(_get_volumeMounts, _set_volumeMounts)


                            @staticmethod
                            def from_dict(d):
                                v = {}
                                if "name" in d:
                                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                                if "image" in d:
                                    v["image"] = str.from_dict(d["image"]) if hasattr(str, 'from_dict') else d["image"]
                                if "ports" in d:
                                    v["ports"] = [ResultSchema._env._pods._containers._ports.from_dict(p) if hasattr(ResultSchema._env._pods._containers._ports, 'from_dict') else p for p in d["ports"]]
                                if "volumeMounts" in d:
                                    v["volumeMounts"] = [ResultSchema._env._pods._containers._volumeMounts.from_dict(p) if hasattr(ResultSchema._env._pods._containers._volumeMounts, 'from_dict') else p for p in d["volumeMounts"]]
                                return ResultSchema._env._pods._containers(**v)


                            def as_dict(self):
                                d = {}
                                if self.__name is not None:
                                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                                if self.__image is not None:
                                    d['image'] = self.__image.as_dict() if hasattr(self.__image, 'as_dict') else self.__image
                                if self.__ports is not None:
                                    d['ports'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__ports]
                                if self.__volumeMounts is not None:
                                    d['volumeMounts'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__volumeMounts]
                                return d

                            def __repr__(self):
                                return "<Class _containers. name: {}, image: {}, ports: {}, volumeMounts: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__image[:20] if isinstance(self.__image, bytes) else self.__image), limitedRepr(self.__ports[:20] if isinstance(self.__ports, bytes) else self.__ports), limitedRepr(self.__volumeMounts[:20] if isinstance(self.__volumeMounts, bytes) else self.__volumeMounts))

                    class _volumes:



                            _types_map = {
                                'name': {'type': str, 'subtype': None},
                                'source': {'type': str, 'subtype': None},
                            }
                            _formats_map = {
                            }
                            _validations_map = {
                                'name': { 'required': False,},
                                'source': { 'required': False,},
                            }

                            def __init__(self
                                    , name=None
                                    , source=None
                                    ):
                                self.__name = name
                                self.__source = source
                                pass

                            def _get_name(self):
                                return self.__name
                            def _set_name(self, value):
                                if value is not None and  not isinstance(value, str):
                                    raise TypeError("name must be str")

                                self.__name = value
                            name = property(_get_name, _set_name)

                            def _get_source(self):
                                return self.__source
                            def _set_source(self, value):
                                if value is not None and  not isinstance(value, str):
                                    raise TypeError("source must be str")

                                self.__source = value
                            source = property(_get_source, _set_source)


                            @staticmethod
                            def from_dict(d):
                                v = {}
                                if "name" in d:
                                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                                if "source" in d:
                                    v["source"] = str.from_dict(d["source"]) if hasattr(str, 'from_dict') else d["source"]
                                return ResultSchema._env._pods._volumes(**v)


                            def as_dict(self):
                                d = {}
                                if self.__name is not None:
                                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                                if self.__source is not None:
                                    d['source'] = self.__source.as_dict() if hasattr(self.__source, 'as_dict') else self.__source
                                return d

                            def __repr__(self):
                                return "<Class _volumes. name: {}, source: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__source[:20] if isinstance(self.__source, bytes) else self.__source))




                    _types_map = {
                        'name': {'type': str, 'subtype': None},
                        'labels': {'type': dict, 'subtype': None},
                        'containers': {'type': list, 'subtype': _containers},
                        'volumes': {'type': list, 'subtype': _volumes},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'name': { 'required': False,},
                        'labels': { 'required': False,},
                        'containers': { 'required': False,},
                        'volumes': { 'required': False,},
                    }

                    def __init__(self
                            , name=None
                            , labels=None
                            , containers=None
                            , volumes=None
                            ):
                        self.__name = name
                        self.__labels = labels
                        self.__containers = containers
                        self.__volumes = volumes
                        pass

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)

                    def _get_labels(self):
                        return self.__labels
                    def _set_labels(self, value):
                        if value is not None and  not isinstance(value, dict):
                            raise TypeError("labels must be dict")

                        self.__labels = value
                    labels = property(_get_labels, _set_labels)

                    def _get_containers(self):
                        return self.__containers
                    def _set_containers(self, value):
                        if value is not None and  not isinstance(value, list):
                            raise TypeError("containers must be list")
                        if value is not None and  not all(isinstance(i, ResultSchema._env._pods._containers) for i in value):
                            raise TypeError("containers list values must be ResultSchema._env._pods._containers")

                        self.__containers = value
                    containers = property(_get_containers, _set_containers)

                    def _get_volumes(self):
                        return self.__volumes
                    def _set_volumes(self, value):
                        if value is not None and  not isinstance(value, list):
                            raise TypeError("volumes must be list")
                        if value is not None and  not all(isinstance(i, ResultSchema._env._pods._volumes) for i in value):
                            raise TypeError("volumes list values must be ResultSchema._env._pods._volumes")

                        self.__volumes = value
                    volumes = property(_get_volumes, _set_volumes)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "labels" in d:
                            v["labels"] = dict.from_dict(d["labels"]) if hasattr(dict, 'from_dict') else d["labels"]
                        if "containers" in d:
                            v["containers"] = [ResultSchema._env._pods._containers.from_dict(p) if hasattr(ResultSchema._env._pods._containers, 'from_dict') else p for p in d["containers"]]
                        if "volumes" in d:
                            v["volumes"] = [ResultSchema._env._pods._volumes.from_dict(p) if hasattr(ResultSchema._env._pods._volumes, 'from_dict') else p for p in d["volumes"]]
                        return ResultSchema._env._pods(**v)


                    def as_dict(self):
                        d = {}
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__labels is not None:
                            d['labels'] = self.__labels.as_dict() if hasattr(self.__labels, 'as_dict') else self.__labels
                        if self.__containers is not None:
                            d['containers'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__containers]
                        if self.__volumes is not None:
                            d['volumes'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__volumes]
                        return d

                    def __repr__(self):
                        return "<Class _pods. name: {}, labels: {}, containers: {}, volumes: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__labels[:20] if isinstance(self.__labels, bytes) else self.__labels), limitedRepr(self.__containers[:20] if isinstance(self.__containers, bytes) else self.__containers), limitedRepr(self.__volumes[:20] if isinstance(self.__volumes, bytes) else self.__volumes))




            _types_map = {
                'system': {'type': _system, 'subtype': None},
                'services': {'type': list, 'subtype': _services},
                'pods': {'type': list, 'subtype': _pods},
            }
            _formats_map = {
            }
            _validations_map = {
                'system': { 'required': False,},
                'services': { 'required': False,},
                'pods': { 'required': False,},
            }

            def __init__(self
                    , system=None
                    , services=None
                    , pods=None
                    ):
                self.__system = system
                self.__services = services
                self.__pods = pods
                pass

            def _get_system(self):
                return self.__system
            def _set_system(self, value):
                if value is not None and  not isinstance(value, ResultSchema._env._system):
                    raise TypeError("system must be ResultSchema._env._system")

                self.__system = value
            system = property(_get_system, _set_system)

            def _get_services(self):
                return self.__services
            def _set_services(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("services must be list")
                if value is not None and  not all(isinstance(i, ResultSchema._env._services) for i in value):
                    raise TypeError("services list values must be ResultSchema._env._services")

                self.__services = value
            services = property(_get_services, _set_services)

            def _get_pods(self):
                return self.__pods
            def _set_pods(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("pods must be list")
                if value is not None and  not all(isinstance(i, ResultSchema._env._pods) for i in value):
                    raise TypeError("pods list values must be ResultSchema._env._pods")

                self.__pods = value
            pods = property(_get_pods, _set_pods)


            @staticmethod
            def from_dict(d):
                v = {}
                if "system" in d:
                    v["system"] = ResultSchema._env._system.from_dict(d["system"]) if hasattr(ResultSchema._env._system, 'from_dict') else d["system"]
                if "services" in d:
                    v["services"] = [ResultSchema._env._services.from_dict(p) if hasattr(ResultSchema._env._services, 'from_dict') else p for p in d["services"]]
                if "pods" in d:
                    v["pods"] = [ResultSchema._env._pods.from_dict(p) if hasattr(ResultSchema._env._pods, 'from_dict') else p for p in d["pods"]]
                return ResultSchema._env(**v)


            def as_dict(self):
                d = {}
                if self.__system is not None:
                    d['system'] = self.__system.as_dict() if hasattr(self.__system, 'as_dict') else self.__system
                if self.__services is not None:
                    d['services'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__services]
                if self.__pods is not None:
                    d['pods'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__pods]
                return d

            def __repr__(self):
                return "<Class _env. system: {}, services: {}, pods: {}>".format(limitedRepr(self.__system[:20] if isinstance(self.__system, bytes) else self.__system), limitedRepr(self.__services[:20] if isinstance(self.__services, bytes) else self.__services), limitedRepr(self.__pods[:20] if isinstance(self.__pods, bytes) else self.__pods))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'ident': {'type': identifier, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'history': {'type': list, 'subtype': event},
        'tags': {'type': list, 'subtype': str},
        'repositories': {'type': repositories, 'subtype': None},
        'packages': {'type': packages, 'subtype': None},
        'test': {'type': identifier, 'subtype': None},
        'caas': {'type': identifier, 'subtype': None},
        'testSuites': {'type': dict, 'subtype': None},
        'status': {'type': str, 'subtype': None},
        'identifiers': {'type': list, 'subtype': identifier},
        'tool': {'type': tool, 'subtype': None},
        'env': {'type': _env, 'subtype': None},
        'deployer': {'type': identifier, 'subtype': None},
        'testType': {'type': str, 'subtype': None},
        'inventory': {'type': str, 'subtype': None},
    }
    _formats_map = {
        'inventory': 'uri',
    }
    _validations_map = {
        'schema': { 'required': False,},
        'ident': { 'required': True,},
        'name': { 'required': True,},
        'description': { 'required': True,},
        'history': { 'required': False,},
        'tags': { 'required': False,},
        'repositories': { 'required': False,},
        'packages': { 'required': False,},
        'test': { 'required': True,},
        'caas': { 'required': False,},
        'testSuites': { 'required': False,},
        'status': { 'required': True,},
        'identifiers': { 'required': False,},
        'tool': { 'required': False,},
        'env': { 'required': False,},
        'deployer': { 'required': False,},
        'testType': { 'required': False,},
        'inventory': { 'required': False,},
    }

    def __init__(self
            , *args
            , schema=None
            , ident=None
            , name=None
            , description=None
            , history=None
            , tags=None
            , repositories=None
            , packages=None
            , test=None
            , caas=None
            , testSuites=None
            , status='Failed'
            , identifiers=None
            , tool=None
            , env=None
            , deployer=None
            , testType=None
            , inventory=None
            , **kwargs
            ):
        """
        :param test: An explanation about the purpose of this instance.
        :param identifiers: List of component, Product or solution identifiers tested
        :param inventory: The location of the AD inventory used for IT test
        """
        self.__schema = schema
        self.__ident = ident
        self.__name = name
        self.__description = description
        self.__history = history
        self.__tags = tags
        self.__repositories = repositories
        self.__packages = packages
        self.__test = test
        self.__caas = caas
        self.__testSuites = testSuites
        self.__status = status
        self.__identifiers = identifiers
        self.__tool = tool
        self.__env = env
        self.__deployer = deployer
        self.__testType = testType
        self.__inventory = inventory
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

    def _get_test(self):
        return self.__test
    def _set_test(self, value):
        if  not isinstance(value, identifier):
            raise TypeError("test must be identifier")

        self.__test = value
    test = property(_get_test, _set_test)
    """
    An explanation about the purpose of this instance.
    """

    def _get_caas(self):
        return self.__caas
    def _set_caas(self, value):
        if value is not None and  not isinstance(value, identifier):
            raise TypeError("caas must be identifier")

        self.__caas = value
    caas = property(_get_caas, _set_caas)

    def _get_testSuites(self):
        return self.__testSuites
    def _set_testSuites(self, value):
        if value is not None and  not isinstance(value, dict):
            raise TypeError("testSuites must be dict")

        self.__testSuites = value
    testSuites = property(_get_testSuites, _set_testSuites)

    def _get_status(self):
        return self.__status
    def _set_status(self, value):
        if  not isinstance(value, str):
            raise TypeError("status must be str")

        self.__status = value
    status = property(_get_status, _set_status)

    def _get_identifiers(self):
        return self.__identifiers
    def _set_identifiers(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("identifiers must be list")
        if value is not None and  not all(isinstance(i, identifier) for i in value):
            raise TypeError("identifiers list values must be identifier")

        self.__identifiers = value
    identifiers = property(_get_identifiers, _set_identifiers)
    """
    List of component, Product or solution identifiers tested
    """

    def _get_tool(self):
        return self.__tool
    def _set_tool(self, value):
        if value is not None and  not isinstance(value, tool):
            raise TypeError("tool must be tool")

        self.__tool = value
    tool = property(_get_tool, _set_tool)

    def _get_env(self):
        return self.__env
    def _set_env(self, value):
        if value is not None and  not isinstance(value, ResultSchema._env):
            raise TypeError("env must be ResultSchema._env")

        self.__env = value
    env = property(_get_env, _set_env)

    def _get_deployer(self):
        return self.__deployer
    def _set_deployer(self, value):
        if value is not None and  not isinstance(value, identifier):
            raise TypeError("deployer must be identifier")

        self.__deployer = value
    deployer = property(_get_deployer, _set_deployer)

    def _get_testType(self):
        return self.__testType
    def _set_testType(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("testType must be str")

        self.__testType = value
    testType = property(_get_testType, _set_testType)

    def _get_inventory(self):
        return self.__inventory
    def _set_inventory(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("inventory must be str")

        self.__inventory = value
    inventory = property(_get_inventory, _set_inventory)
    """
    The location of the AD inventory used for IT test
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
        if "repositories" in d:
            v["repositories"] = repositories.from_dict(d["repositories"]) if hasattr(repositories, 'from_dict') else d["repositories"]
        if "packages" in d:
            v["packages"] = packages.from_dict(d["packages"]) if hasattr(packages, 'from_dict') else d["packages"]
        if "test" in d:
            v["test"] = identifier.from_dict(d["test"]) if hasattr(identifier, 'from_dict') else d["test"]
        if "caas" in d:
            v["caas"] = identifier.from_dict(d["caas"]) if hasattr(identifier, 'from_dict') else d["caas"]
        if "testSuites" in d:
            v["testSuites"] = dict.from_dict(d["testSuites"]) if hasattr(dict, 'from_dict') else d["testSuites"]
        if "status" in d:
            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
        if "identifiers" in d:
            v["identifiers"] = [identifier.from_dict(p) if hasattr(identifier, 'from_dict') else p for p in d["identifiers"]]
        if "tool" in d:
            v["tool"] = tool.from_dict(d["tool"]) if hasattr(tool, 'from_dict') else d["tool"]
        if "env" in d:
            v["env"] = ResultSchema._env.from_dict(d["env"]) if hasattr(ResultSchema._env, 'from_dict') else d["env"]
        if "deployer" in d:
            v["deployer"] = identifier.from_dict(d["deployer"]) if hasattr(identifier, 'from_dict') else d["deployer"]
        if "testType" in d:
            v["testType"] = str.from_dict(d["testType"]) if hasattr(str, 'from_dict') else d["testType"]
        if "inventory" in d:
            v["inventory"] = str.from_dict(d["inventory"]) if hasattr(str, 'from_dict') else d["inventory"]
        return ResultSchema(**v)


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
        if self.__repositories is not None:
            d['repositories'] = self.__repositories.as_dict() if hasattr(self.__repositories, 'as_dict') else self.__repositories
        if self.__packages is not None:
            d['packages'] = self.__packages.as_dict() if hasattr(self.__packages, 'as_dict') else self.__packages
        if self.__test is not None:
            d['test'] = self.__test.as_dict() if hasattr(self.__test, 'as_dict') else self.__test
        if self.__caas is not None:
            d['caas'] = self.__caas.as_dict() if hasattr(self.__caas, 'as_dict') else self.__caas
        if self.__testSuites is not None:
            d['testSuites'] = self.__testSuites.as_dict() if hasattr(self.__testSuites, 'as_dict') else self.__testSuites
        if self.__status is not None:
            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
        if self.__identifiers is not None:
            d['identifiers'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__identifiers]
        if self.__tool is not None:
            d['tool'] = self.__tool.as_dict() if hasattr(self.__tool, 'as_dict') else self.__tool
        if self.__env is not None:
            d['env'] = self.__env.as_dict() if hasattr(self.__env, 'as_dict') else self.__env
        if self.__deployer is not None:
            d['deployer'] = self.__deployer.as_dict() if hasattr(self.__deployer, 'as_dict') else self.__deployer
        if self.__testType is not None:
            d['testType'] = self.__testType.as_dict() if hasattr(self.__testType, 'as_dict') else self.__testType
        if self.__inventory is not None:
            d['inventory'] = self.__inventory.as_dict() if hasattr(self.__inventory, 'as_dict') else self.__inventory
        return d

    def __repr__(self):
        return "<Class ResultSchema. schema: {}, ident: {}, name: {}, description: {}, history: {}, tags: {}, repositories: {}, packages: {}, test: {}, caas: {}, testSuites: {}, status: {}, identifiers: {}, tool: {}, env: {}, deployer: {}, testType: {}, inventory: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__ident[:20] if isinstance(self.__ident, bytes) else self.__ident), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__history[:20] if isinstance(self.__history, bytes) else self.__history), limitedRepr(self.__tags[:20] if isinstance(self.__tags, bytes) else self.__tags), limitedRepr(self.__repositories[:20] if isinstance(self.__repositories, bytes) else self.__repositories), limitedRepr(self.__packages[:20] if isinstance(self.__packages, bytes) else self.__packages), limitedRepr(self.__test[:20] if isinstance(self.__test, bytes) else self.__test), limitedRepr(self.__caas[:20] if isinstance(self.__caas, bytes) else self.__caas), limitedRepr(self.__testSuites[:20] if isinstance(self.__testSuites, bytes) else self.__testSuites), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status), limitedRepr(self.__identifiers[:20] if isinstance(self.__identifiers, bytes) else self.__identifiers), limitedRepr(self.__tool[:20] if isinstance(self.__tool, bytes) else self.__tool), limitedRepr(self.__env[:20] if isinstance(self.__env, bytes) else self.__env), limitedRepr(self.__deployer[:20] if isinstance(self.__deployer, bytes) else self.__deployer), limitedRepr(self.__testType[:20] if isinstance(self.__testType, bytes) else self.__testType), limitedRepr(self.__inventory[:20] if isinstance(self.__inventory, bytes) else self.__inventory))

