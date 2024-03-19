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

class TestSchema(MetainfoBase):
    """
    The test schema describes a test.
    """
    class _suite:
            """
            Parameters to launch test suite
            """



            _types_map = {
                'path': {'type': str, 'subtype': None},
                'target': {'type': str, 'subtype': None},
                'script': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'path': { 'required': False,},
                'target': { 'required': False,},
                'script': { 'required': False,},
            }

            def __init__(self
                    , path=None
                    , target='K8S'
                    , script='functional_tests.cfg'
                    ):
                self.__path = path
                self.__target = target
                self.__script = script
                pass

            def _get_path(self):
                return self.__path
            def _set_path(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("path must be str")

                self.__path = value
            path = property(_get_path, _set_path)

            def _get_target(self):
                return self.__target
            def _set_target(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("target must be str")

                self.__target = value
            target = property(_get_target, _set_target)

            def _get_script(self):
                return self.__script
            def _set_script(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("script must be str")

                self.__script = value
            script = property(_get_script, _set_script)


            @staticmethod
            def from_dict(d):
                v = {}
                if "path" in d:
                    v["path"] = str.from_dict(d["path"]) if hasattr(str, 'from_dict') else d["path"]
                if "target" in d:
                    v["target"] = str.from_dict(d["target"]) if hasattr(str, 'from_dict') else d["target"]
                if "script" in d:
                    v["script"] = str.from_dict(d["script"]) if hasattr(str, 'from_dict') else d["script"]
                return TestSchema._suite(**v)


            def as_dict(self):
                d = {}
                if self.__path is not None:
                    d['path'] = self.__path.as_dict() if hasattr(self.__path, 'as_dict') else self.__path
                if self.__target is not None:
                    d['target'] = self.__target.as_dict() if hasattr(self.__target, 'as_dict') else self.__target
                if self.__script is not None:
                    d['script'] = self.__script.as_dict() if hasattr(self.__script, 'as_dict') else self.__script
                return d

            def __repr__(self):
                return "<Class _suite. path: {}, target: {}, script: {}>".format(limitedRepr(self.__path[:20] if isinstance(self.__path, bytes) else self.__path), limitedRepr(self.__target[:20] if isinstance(self.__target, bytes) else self.__target), limitedRepr(self.__script[:20] if isinstance(self.__script, bytes) else self.__script))

    class _run:
            """
            Parameters to run test
            """



            _types_map = {
                'mail': {'type': str, 'subtype': None},
                'inventory': {'type': str, 'subtype': None},
                'timeout': {'type': int, 'subtype': None},
                'resource': {'type': str, 'subtype': None},
                'pipelines': {'type': dict, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'mail': { 'required': True,},
                'inventory': { 'required': True,},
                'timeout': { 'required': True,'minimum': 0,},
                'resource': { 'required': True,},
                'pipelines': { 'required': False,},
            }

            def __init__(self
                    , mail=None
                    , inventory='ci5g-ad'
                    , timeout=30
                    , resource='OCP_ProjectSmall'
                    , pipelines=None
                    ):
                """
                :param mail: Mail to send result
                :param inventory: Inventory template
                :param timeout: Test timeout
                :param resource: Resource to deploy
                :param pipelines: List of custom pipelines by nf_type
                """
                self.__mail = mail
                self.__inventory = inventory
                self.__timeout = timeout
                self.__resource = resource
                self.__pipelines = pipelines
                pass

            def _get_mail(self):
                return self.__mail
            def _set_mail(self, value):
                if  not isinstance(value, str):
                    raise TypeError("mail must be str")

                self.__mail = value
            mail = property(_get_mail, _set_mail)
            """
            Mail to send result
            """

            def _get_inventory(self):
                return self.__inventory
            def _set_inventory(self, value):
                if  not isinstance(value, str):
                    raise TypeError("inventory must be str")

                self.__inventory = value
            inventory = property(_get_inventory, _set_inventory)
            """
            Inventory template
            """

            def _get_timeout(self):
                return self.__timeout
            def _set_timeout(self, value):
                if  not isinstance(value, int):
                    raise TypeError("timeout must be int")

                self.__timeout = value
            timeout = property(_get_timeout, _set_timeout)
            """
            Test timeout
            """

            def _get_resource(self):
                return self.__resource
            def _set_resource(self, value):
                if  not isinstance(value, str):
                    raise TypeError("resource must be str")

                self.__resource = value
            resource = property(_get_resource, _set_resource)
            """
            Resource to deploy
            """

            def _get_pipelines(self):
                return self.__pipelines
            def _set_pipelines(self, value):
                if value is not None and  not isinstance(value, dict):
                    raise TypeError("pipelines must be dict")

                self.__pipelines = value
            pipelines = property(_get_pipelines, _set_pipelines)
            """
            List of custom pipelines by nf_type
            """


            @staticmethod
            def from_dict(d):
                v = {}
                if "mail" in d:
                    v["mail"] = str.from_dict(d["mail"]) if hasattr(str, 'from_dict') else d["mail"]
                if "inventory" in d:
                    v["inventory"] = str.from_dict(d["inventory"]) if hasattr(str, 'from_dict') else d["inventory"]
                if "timeout" in d:
                    v["timeout"] = int.from_dict(d["timeout"]) if hasattr(int, 'from_dict') else d["timeout"]
                if "resource" in d:
                    v["resource"] = str.from_dict(d["resource"]) if hasattr(str, 'from_dict') else d["resource"]
                if "pipelines" in d:
                    v["pipelines"] = dict.from_dict(d["pipelines"]) if hasattr(dict, 'from_dict') else d["pipelines"]
                return TestSchema._run(**v)


            def as_dict(self):
                d = {}
                if self.__mail is not None:
                    d['mail'] = self.__mail.as_dict() if hasattr(self.__mail, 'as_dict') else self.__mail
                if self.__inventory is not None:
                    d['inventory'] = self.__inventory.as_dict() if hasattr(self.__inventory, 'as_dict') else self.__inventory
                if self.__timeout is not None:
                    d['timeout'] = self.__timeout.as_dict() if hasattr(self.__timeout, 'as_dict') else self.__timeout
                if self.__resource is not None:
                    d['resource'] = self.__resource.as_dict() if hasattr(self.__resource, 'as_dict') else self.__resource
                if self.__pipelines is not None:
                    d['pipelines'] = self.__pipelines.as_dict() if hasattr(self.__pipelines, 'as_dict') else self.__pipelines
                return d

            def __repr__(self):
                return "<Class _run. mail: {}, inventory: {}, timeout: {}, resource: {}, pipelines: {}>".format(limitedRepr(self.__mail[:20] if isinstance(self.__mail, bytes) else self.__mail), limitedRepr(self.__inventory[:20] if isinstance(self.__inventory, bytes) else self.__inventory), limitedRepr(self.__timeout[:20] if isinstance(self.__timeout, bytes) else self.__timeout), limitedRepr(self.__resource[:20] if isinstance(self.__resource, bytes) else self.__resource), limitedRepr(self.__pipelines[:20] if isinstance(self.__pipelines, bytes) else self.__pipelines))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'ident': {'type': identifier, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'scm': {'type': scm, 'subtype': None},
        'history': {'type': list, 'subtype': event},
        'tags': {'type': list, 'subtype': str},
        'repositories': {'type': repositories, 'subtype': None},
        'dependencies': {'type': list, 'subtype': identifier},
        'packages': {'type': packages, 'subtype': None},
        'status': {'type': str, 'subtype': None},
        'suite': {'type': _suite, 'subtype': None},
        'run': {'type': _run, 'subtype': None},
        'type': {'type': str, 'subtype': None},
        'tool': {'type': tool, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'schema': { 'required': True,},
        'ident': { 'required': True,},
        'name': { 'required': True,},
        'description': { 'required': True,},
        'scm': { 'required': False,},
        'history': { 'required': False,},
        'tags': { 'required': False,},
        'repositories': { 'required': True,},
        'dependencies': { 'required': False,},
        'packages': { 'required': False,},
        'status': { 'required': True,},
        'suite': { 'required': True,},
        'run': { 'required': True,},
        'type': { 'required': False,},
        'tool': { 'required': False,},
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
            , repositories=None
            , dependencies=None
            , packages=None
            , status='Init'
            , suite=None
            , run=None
            , type=None
            , tool=None
            , **kwargs
            ):
        """
        :param suite: Parameters to launch test suite
        :param run: Parameters to run test
        """
        self.__schema = schema
        self.__ident = ident
        self.__name = name
        self.__description = description
        self.__scm = scm
        self.__history = history
        self.__tags = tags
        self.__repositories = repositories
        self.__dependencies = dependencies
        self.__packages = packages
        self.__status = status
        self.__suite = suite
        self.__run = run
        self.__type = type
        self.__tool = tool
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

    def _get_repositories(self):
        return self.__repositories
    def _set_repositories(self, value):
        if  not isinstance(value, repositories):
            raise TypeError("repositories must be repositories")

        self.__repositories = value
    repositories = property(_get_repositories, _set_repositories)

    def _get_dependencies(self):
        return self.__dependencies
    def _set_dependencies(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("dependencies must be list")
        if value is not None and  not all(isinstance(i, identifier) for i in value):
            raise TypeError("dependencies list values must be identifier")

        self.__dependencies = value
    dependencies = property(_get_dependencies, _set_dependencies)

    def _get_packages(self):
        return self.__packages
    def _set_packages(self, value):
        if value is not None and  not isinstance(value, packages):
            raise TypeError("packages must be packages")

        self.__packages = value
    packages = property(_get_packages, _set_packages)

    def _get_status(self):
        return self.__status
    def _set_status(self, value):
        if  not isinstance(value, str):
            raise TypeError("status must be str")

        self.__status = value
    status = property(_get_status, _set_status)

    def _get_suite(self):
        return self.__suite
    def _set_suite(self, value):
        if  not isinstance(value, TestSchema._suite):
            raise TypeError("suite must be TestSchema._suite")

        self.__suite = value
    suite = property(_get_suite, _set_suite)
    """
    Parameters to launch test suite
    """

    def _get_run(self):
        return self.__run
    def _set_run(self, value):
        if  not isinstance(value, TestSchema._run):
            raise TypeError("run must be TestSchema._run")

        self.__run = value
    run = property(_get_run, _set_run)
    """
    Parameters to run test
    """

    def _get_type(self):
        return self.__type
    def _set_type(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("type must be str")

        self.__type = value
    type = property(_get_type, _set_type)

    def _get_tool(self):
        return self.__tool
    def _set_tool(self, value):
        if value is not None and  not isinstance(value, tool):
            raise TypeError("tool must be tool")

        self.__tool = value
    tool = property(_get_tool, _set_tool)


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
        if "repositories" in d:
            v["repositories"] = repositories.from_dict(d["repositories"]) if hasattr(repositories, 'from_dict') else d["repositories"]
        if "dependencies" in d:
            v["dependencies"] = [identifier.from_dict(p) if hasattr(identifier, 'from_dict') else p for p in d["dependencies"]]
        if "packages" in d:
            v["packages"] = packages.from_dict(d["packages"]) if hasattr(packages, 'from_dict') else d["packages"]
        if "status" in d:
            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
        if "suite" in d:
            v["suite"] = TestSchema._suite.from_dict(d["suite"]) if hasattr(TestSchema._suite, 'from_dict') else d["suite"]
        if "run" in d:
            v["run"] = TestSchema._run.from_dict(d["run"]) if hasattr(TestSchema._run, 'from_dict') else d["run"]
        if "type" in d:
            v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
        if "tool" in d:
            v["tool"] = tool.from_dict(d["tool"]) if hasattr(tool, 'from_dict') else d["tool"]
        return TestSchema(**v)


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
        if self.__repositories is not None:
            d['repositories'] = self.__repositories.as_dict() if hasattr(self.__repositories, 'as_dict') else self.__repositories
        if self.__dependencies is not None:
            d['dependencies'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dependencies]
        if self.__packages is not None:
            d['packages'] = self.__packages.as_dict() if hasattr(self.__packages, 'as_dict') else self.__packages
        if self.__status is not None:
            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
        if self.__suite is not None:
            d['suite'] = self.__suite.as_dict() if hasattr(self.__suite, 'as_dict') else self.__suite
        if self.__run is not None:
            d['run'] = self.__run.as_dict() if hasattr(self.__run, 'as_dict') else self.__run
        if self.__type is not None:
            d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
        if self.__tool is not None:
            d['tool'] = self.__tool.as_dict() if hasattr(self.__tool, 'as_dict') else self.__tool
        return d

    def __repr__(self):
        return "<Class TestSchema. schema: {}, ident: {}, name: {}, description: {}, scm: {}, history: {}, tags: {}, repositories: {}, dependencies: {}, packages: {}, status: {}, suite: {}, run: {}, type: {}, tool: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__ident[:20] if isinstance(self.__ident, bytes) else self.__ident), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__scm[:20] if isinstance(self.__scm, bytes) else self.__scm), limitedRepr(self.__history[:20] if isinstance(self.__history, bytes) else self.__history), limitedRepr(self.__tags[:20] if isinstance(self.__tags, bytes) else self.__tags), limitedRepr(self.__repositories[:20] if isinstance(self.__repositories, bytes) else self.__repositories), limitedRepr(self.__dependencies[:20] if isinstance(self.__dependencies, bytes) else self.__dependencies), limitedRepr(self.__packages[:20] if isinstance(self.__packages, bytes) else self.__packages), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status), limitedRepr(self.__suite[:20] if isinstance(self.__suite, bytes) else self.__suite), limitedRepr(self.__run[:20] if isinstance(self.__run, bytes) else self.__run), limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type), limitedRepr(self.__tool[:20] if isinstance(self.__tool, bytes) else self.__tool))

