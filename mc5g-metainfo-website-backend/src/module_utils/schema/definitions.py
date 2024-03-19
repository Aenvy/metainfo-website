from reprlib import repr as limitedRepr


import enum


class identifier:
    """
    Maven identifier
    """



    _types_map = {
        'groupId': {'type': str, 'subtype': None},
        'artifactId': {'type': str, 'subtype': None},
        'version': {'type': str, 'subtype': None},
        'branch': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'groupId': { 'required': True,},
        'artifactId': { 'required': True,},
        'version': { 'required': True,},
        'branch': { 'required': False,},
    }

    def __init__(self
            , groupId=None
            , artifactId=None
            , version=None
            , branch=None
            ):
        self.__groupId = groupId
        self.__artifactId = artifactId
        self.__version = version
        self.__branch = branch
        pass

    def _get_groupId(self):
        return self.__groupId
    def _set_groupId(self, value):
        if  not isinstance(value, str):
            raise TypeError("groupId must be str")

        self.__groupId = value
    groupId = property(_get_groupId, _set_groupId)

    def _get_artifactId(self):
        return self.__artifactId
    def _set_artifactId(self, value):
        if  not isinstance(value, str):
            raise TypeError("artifactId must be str")

        self.__artifactId = value
    artifactId = property(_get_artifactId, _set_artifactId)

    def _get_version(self):
        return self.__version
    def _set_version(self, value):
        if  not isinstance(value, str):
            raise TypeError("version must be str")

        self.__version = value
    version = property(_get_version, _set_version)

    def _get_branch(self):
        return self.__branch
    def _set_branch(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("branch must be str")

        self.__branch = value
    branch = property(_get_branch, _set_branch)


    @staticmethod
    def from_dict(d):
        v = {}
        if "groupId" in d:
            v["groupId"] = str.from_dict(d["groupId"]) if hasattr(str, 'from_dict') else d["groupId"]
        if "artifactId" in d:
            v["artifactId"] = str.from_dict(d["artifactId"]) if hasattr(str, 'from_dict') else d["artifactId"]
        if "version" in d:
            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
        if "branch" in d:
            v["branch"] = str.from_dict(d["branch"]) if hasattr(str, 'from_dict') else d["branch"]
        return identifier(**v)


    def as_dict(self):
        d = {}
        if self.__groupId is not None:
            d['groupId'] = self.__groupId.as_dict() if hasattr(self.__groupId, 'as_dict') else self.__groupId
        if self.__artifactId is not None:
            d['artifactId'] = self.__artifactId.as_dict() if hasattr(self.__artifactId, 'as_dict') else self.__artifactId
        if self.__version is not None:
            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
        if self.__branch is not None:
            d['branch'] = self.__branch.as_dict() if hasattr(self.__branch, 'as_dict') else self.__branch
        return d

    def __repr__(self):
        return "<Class identifier. groupId: {}, artifactId: {}, version: {}, branch: {}>".format(limitedRepr(self.__groupId[:20] if isinstance(self.__groupId, bytes) else self.__groupId), limitedRepr(self.__artifactId[:20] if isinstance(self.__artifactId, bytes) else self.__artifactId), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__branch[:20] if isinstance(self.__branch, bytes) else self.__branch))

class partialIdentifier:
    """
    Maven identifier, without version or branch information
    """



    _types_map = {
        'groupId': {'type': str, 'subtype': None},
        'artifactId': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'groupId': { 'required': True,},
        'artifactId': { 'required': True,},
    }

    def __init__(self
            , groupId=None
            , artifactId=None
            ):
        self.__groupId = groupId
        self.__artifactId = artifactId
        pass

    def _get_groupId(self):
        return self.__groupId
    def _set_groupId(self, value):
        if  not isinstance(value, str):
            raise TypeError("groupId must be str")

        self.__groupId = value
    groupId = property(_get_groupId, _set_groupId)

    def _get_artifactId(self):
        return self.__artifactId
    def _set_artifactId(self, value):
        if  not isinstance(value, str):
            raise TypeError("artifactId must be str")

        self.__artifactId = value
    artifactId = property(_get_artifactId, _set_artifactId)


    @staticmethod
    def from_dict(d):
        v = {}
        if "groupId" in d:
            v["groupId"] = str.from_dict(d["groupId"]) if hasattr(str, 'from_dict') else d["groupId"]
        if "artifactId" in d:
            v["artifactId"] = str.from_dict(d["artifactId"]) if hasattr(str, 'from_dict') else d["artifactId"]
        return partialIdentifier(**v)


    def as_dict(self):
        d = {}
        if self.__groupId is not None:
            d['groupId'] = self.__groupId.as_dict() if hasattr(self.__groupId, 'as_dict') else self.__groupId
        if self.__artifactId is not None:
            d['artifactId'] = self.__artifactId.as_dict() if hasattr(self.__artifactId, 'as_dict') else self.__artifactId
        return d

    def __repr__(self):
        return "<Class partialIdentifier. groupId: {}, artifactId: {}>".format(limitedRepr(self.__groupId[:20] if isinstance(self.__groupId, bytes) else self.__groupId), limitedRepr(self.__artifactId[:20] if isinstance(self.__artifactId, bytes) else self.__artifactId))

class pipeline_stages:
    """
    Which pipeline stages to run
    """



    _types_map = {
        'stage_deploy': {'type': bool, 'subtype': None},
        'stage_tests': {'type': bool, 'subtype': None},
        'stage_promote': {'type': bool, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'stage_deploy': { 'required': False,},
        'stage_tests': { 'required': False,},
        'stage_promote': { 'required': False,},
    }

    def __init__(self
            , stage_deploy=True
            , stage_tests=True
            , stage_promote=True
            ):
        self.__stage_deploy = stage_deploy
        self.__stage_tests = stage_tests
        self.__stage_promote = stage_promote
        pass

    def _get_stage_deploy(self):
        return self.__stage_deploy
    def _set_stage_deploy(self, value):
        if value is not None and  not isinstance(value, bool):
            raise TypeError("stage_deploy must be bool")

        self.__stage_deploy = value
    stage_deploy = property(_get_stage_deploy, _set_stage_deploy)

    def _get_stage_tests(self):
        return self.__stage_tests
    def _set_stage_tests(self, value):
        if value is not None and  not isinstance(value, bool):
            raise TypeError("stage_tests must be bool")

        self.__stage_tests = value
    stage_tests = property(_get_stage_tests, _set_stage_tests)

    def _get_stage_promote(self):
        return self.__stage_promote
    def _set_stage_promote(self, value):
        if value is not None and  not isinstance(value, bool):
            raise TypeError("stage_promote must be bool")

        self.__stage_promote = value
    stage_promote = property(_get_stage_promote, _set_stage_promote)


    @staticmethod
    def from_dict(d):
        v = {}
        if "stage_deploy" in d:
            v["stage_deploy"] = bool.from_dict(d["stage_deploy"]) if hasattr(bool, 'from_dict') else d["stage_deploy"]
        if "stage_tests" in d:
            v["stage_tests"] = bool.from_dict(d["stage_tests"]) if hasattr(bool, 'from_dict') else d["stage_tests"]
        if "stage_promote" in d:
            v["stage_promote"] = bool.from_dict(d["stage_promote"]) if hasattr(bool, 'from_dict') else d["stage_promote"]
        return pipeline_stages(**v)


    def as_dict(self):
        d = {}
        if self.__stage_deploy is not None:
            d['stage_deploy'] = self.__stage_deploy.as_dict() if hasattr(self.__stage_deploy, 'as_dict') else self.__stage_deploy
        if self.__stage_tests is not None:
            d['stage_tests'] = self.__stage_tests.as_dict() if hasattr(self.__stage_tests, 'as_dict') else self.__stage_tests
        if self.__stage_promote is not None:
            d['stage_promote'] = self.__stage_promote.as_dict() if hasattr(self.__stage_promote, 'as_dict') else self.__stage_promote
        return d

    def __repr__(self):
        return "<Class pipeline_stages. stage_deploy: {}, stage_tests: {}, stage_promote: {}>".format(limitedRepr(self.__stage_deploy[:20] if isinstance(self.__stage_deploy, bytes) else self.__stage_deploy), limitedRepr(self.__stage_tests[:20] if isinstance(self.__stage_tests, bytes) else self.__stage_tests), limitedRepr(self.__stage_promote[:20] if isinstance(self.__stage_promote, bytes) else self.__stage_promote))

class scm:



    _types_map = {
        'type': {'type': str, 'subtype': None},
        'url': {'type': str, 'subtype': None},
        'ref': {'type': str, 'subtype': None},
        'branch': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'type': { 'required': False,},
        'url': { 'required': False,},
        'ref': { 'required': False,},
        'branch': { 'required': False,},
    }

    def __init__(self
            , type=None
            , url=None
            , ref=None
            , branch='master'
            ):
        self.__type = type
        self.__url = url
        self.__ref = ref
        self.__branch = branch
        pass

    def _get_type(self):
        return self.__type
    def _set_type(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("type must be str")

        self.__type = value
    type = property(_get_type, _set_type)

    def _get_url(self):
        return self.__url
    def _set_url(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("url must be str")

        self.__url = value
    url = property(_get_url, _set_url)

    def _get_ref(self):
        return self.__ref
    def _set_ref(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("ref must be str")

        self.__ref = value
    ref = property(_get_ref, _set_ref)

    def _get_branch(self):
        return self.__branch
    def _set_branch(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("branch must be str")

        self.__branch = value
    branch = property(_get_branch, _set_branch)


    @staticmethod
    def from_dict(d):
        v = {}
        if "type" in d:
            v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
        if "url" in d:
            v["url"] = str.from_dict(d["url"]) if hasattr(str, 'from_dict') else d["url"]
        if "ref" in d:
            v["ref"] = str.from_dict(d["ref"]) if hasattr(str, 'from_dict') else d["ref"]
        if "branch" in d:
            v["branch"] = str.from_dict(d["branch"]) if hasattr(str, 'from_dict') else d["branch"]
        return scm(**v)


    def as_dict(self):
        d = {}
        if self.__type is not None:
            d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
        if self.__url is not None:
            d['url'] = self.__url.as_dict() if hasattr(self.__url, 'as_dict') else self.__url
        if self.__ref is not None:
            d['ref'] = self.__ref.as_dict() if hasattr(self.__ref, 'as_dict') else self.__ref
        if self.__branch is not None:
            d['branch'] = self.__branch.as_dict() if hasattr(self.__branch, 'as_dict') else self.__branch
        return d

    def __repr__(self):
        return "<Class scm. type: {}, url: {}, ref: {}, branch: {}>".format(limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type), limitedRepr(self.__url[:20] if isinstance(self.__url, bytes) else self.__url), limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__branch[:20] if isinstance(self.__branch, bytes) else self.__branch))

class job:
    """
    A CI job source of an event
    """



    _types_map = {
        'name': {'type': str, 'subtype': None},
        'id': {'type': str, 'subtype': None},
        'date': {'type': str, 'subtype': None},
        'url': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'name': { 'required': False,},
        'id': { 'required': False,},
        'date': { 'required': False,},
        'url': { 'required': False,},
    }

    def __init__(self
            , name=None
            , id=None
            , date=None
            , url=None
            ):
        """
        :param name: The job Name as known by the CI server
        :param date: The date of a job
        """
        self.__name = name
        self.__id = id
        self.__date = date
        self.__url = url
        pass

    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value
    name = property(_get_name, _set_name)
    """
    The job Name as known by the CI server
    """

    def _get_id(self):
        return self.__id
    def _set_id(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("id must be str")

        self.__id = value
    id = property(_get_id, _set_id)

    def _get_date(self):
        return self.__date
    def _set_date(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("date must be str")

        self.__date = value
    date = property(_get_date, _set_date)
    """
    The date of a job
    """

    def _get_url(self):
        return self.__id
    def _set_url(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("url must be str")

        self.__url = value
    url = property(_get_url, _set_url)

    @staticmethod
    def from_dict(d):
        v = {}
        if "name" in d:
            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
        if "id" in d:
            v["id"] = str.from_dict(d["id"]) if hasattr(str, 'from_dict') else d["id"]
        if "date" in d:
            v["date"] = str.from_dict(d["date"]) if hasattr(str, 'from_dict') else d["date"]
        if "url" in d:
            v["url"] = str.from_dict(d["url"]) if hasattr(str, 'from_dict') else d["url"]
        return job(**v)


    def as_dict(self):
        d = {}
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__id is not None:
            d['id'] = self.__id.as_dict() if hasattr(self.__id, 'as_dict') else self.__id
        if self.__date is not None:
            d['date'] = self.__date.as_dict() if hasattr(self.__date, 'as_dict') else self.__date
        if self.__url is not None:
            d['url'] = self.__url.as_dict() if hasattr(self.__url, 'as_dict') else self.__url
        return d

    def __repr__(self):
        return "<Class job. name: {}, id: {}, date: {}, url: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__id[:20] if isinstance(self.__id, bytes) else self.__id), limitedRepr(self.__date[:20] if isinstance(self.__date, bytes) else self.__date), limitedRepr(self.__url[:20] if isinstance(self.__url, bytes) else self.__url))

class event:
    """
    An event that impact schema data
    """



    _types_map = {
        'date': {'type': str, 'subtype': None},
        'type': {'type': str, 'subtype': None},
        'details': {'type': str, 'subtype': None},
        'job': {'type': job, 'subtype': None},
        'sign': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'date': { 'required': True,},
        'type': { 'required': True,},
        'details': { 'required': True,},
        'job': { 'required': False,},
        'sign': { 'required': False,},
    }

    def __init__(self
            , date=None
            , type=None
            , details=None
            , job=None
            , sign=None
            ):
        """
        :param date: A date element in an event
        :param type: The type of the event
        :param details: The full description of the event
        :param sign: The signature of the event
        """
        self.__date = date
        self.__type = type
        self.__details = details
        self.__job = job
        self.__sign = sign
        pass

    def _get_date(self):
        return self.__date
    def _set_date(self, value):
        if  not isinstance(value, str):
            raise TypeError("date must be str")

        self.__date = value
    date = property(_get_date, _set_date)
    """
    A date element in an event
    """

    def _get_type(self):
        return self.__type
    def _set_type(self, value):
        if  not isinstance(value, str):
            raise TypeError("type must be str")

        self.__type = value
    type = property(_get_type, _set_type)
    """
    The type of the event
    """

    def _get_details(self):
        return self.__details
    def _set_details(self, value):
        if  not isinstance(value, str):
            raise TypeError("details must be str")

        self.__details = value
    details = property(_get_details, _set_details)
    """
    The full description of the event
    """

    def _get_job(self):
        return self.__job
    def _set_job(self, value):
        if value is not None and  not isinstance(value, job):
            raise TypeError("job must be job")

        self.__job = value
    job = property(_get_job, _set_job)

    def _get_sign(self):
        return self.__sign
    def _set_sign(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("sign must be str")

        self.__sign = value
    sign = property(_get_sign, _set_sign)
    """
    The signature of the event
    """


    @staticmethod
    def from_dict(d):
        v = {}
        if "date" in d:
            v["date"] = str.from_dict(d["date"]) if hasattr(str, 'from_dict') else d["date"]
        if "type" in d:
            v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
        if "details" in d:
            v["details"] = str.from_dict(d["details"]) if hasattr(str, 'from_dict') else d["details"]
        if "job" in d:
            v["job"] = job.from_dict(d["job"]) if hasattr(job, 'from_dict') else d["job"]
        if "sign" in d:
            v["sign"] = str.from_dict(d["sign"]) if hasattr(str, 'from_dict') else d["sign"]
        return event(**v)


    def as_dict(self):
        d = {}
        if self.__date is not None:
            d['date'] = self.__date.as_dict() if hasattr(self.__date, 'as_dict') else self.__date
        if self.__type is not None:
            d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
        if self.__details is not None:
            d['details'] = self.__details.as_dict() if hasattr(self.__details, 'as_dict') else self.__details
        if self.__job is not None:
            d['job'] = self.__job.as_dict() if hasattr(self.__job, 'as_dict') else self.__job
        if self.__sign is not None:
            d['sign'] = self.__sign.as_dict() if hasattr(self.__sign, 'as_dict') else self.__sign
        return d

    def __repr__(self):
        return "<Class event. date: {}, type: {}, details: {}, job: {}, sign: {}>".format(limitedRepr(self.__date[:20] if isinstance(self.__date, bytes) else self.__date), limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type), limitedRepr(self.__details[:20] if isinstance(self.__details, bytes) else self.__details), limitedRepr(self.__job[:20] if isinstance(self.__job, bytes) else self.__job), limitedRepr(self.__sign[:20] if isinstance(self.__sign, bytes) else self.__sign))

class repositories:



    _types_map = {
        'docker': {'type': str, 'subtype': None},
        'helm': {'type': str, 'subtype': None},
        'yum': {'type': str, 'subtype': None},
        'maven': {'type': str, 'subtype': None},
        'raw': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'docker': { 'required': False,},
        'helm': { 'required': False,},
        'yum': { 'required': False,},
        'maven': { 'required': False,},
        'raw': { 'required': False,},
    }

    def __init__(self
            , docker=None
            , helm=None
            , yum=None
            , maven=None
            , raw=None
            ):
        self.__docker = docker
        self.__helm = helm
        self.__yum = yum
        self.__maven = maven
        self.__raw = raw
        pass

    def _get_docker(self):
        return self.__docker
    def _set_docker(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("docker must be str")

        self.__docker = value
    docker = property(_get_docker, _set_docker)

    def _get_helm(self):
        return self.__helm
    def _set_helm(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("helm must be str")

        self.__helm = value
    helm = property(_get_helm, _set_helm)

    def _get_yum(self):
        return self.__yum
    def _set_yum(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("yum must be str")

        self.__yum = value
    yum = property(_get_yum, _set_yum)

    def _get_maven(self):
        return self.__maven
    def _set_maven(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("maven must be str")

        self.__maven = value
    maven = property(_get_maven, _set_maven)

    def _get_raw(self):
        return self.__raw
    def _set_raw(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("raw must be str")

        self.__raw = value
    raw = property(_get_raw, _set_raw)


    @staticmethod
    def from_dict(d):
        v = {}
        if "docker" in d:
            v["docker"] = str.from_dict(d["docker"]) if hasattr(str, 'from_dict') else d["docker"]
        if "helm" in d:
            v["helm"] = str.from_dict(d["helm"]) if hasattr(str, 'from_dict') else d["helm"]
        if "yum" in d:
            v["yum"] = str.from_dict(d["yum"]) if hasattr(str, 'from_dict') else d["yum"]
        if "maven" in d:
            v["maven"] = str.from_dict(d["maven"]) if hasattr(str, 'from_dict') else d["maven"]
        if "raw" in d:
            v["raw"] = str.from_dict(d["raw"]) if hasattr(str, 'from_dict') else d["raw"]
        return repositories(**v)


    def as_dict(self):
        d = {}
        if self.__docker is not None:
            d['docker'] = self.__docker.as_dict() if hasattr(self.__docker, 'as_dict') else self.__docker
        if self.__helm is not None:
            d['helm'] = self.__helm.as_dict() if hasattr(self.__helm, 'as_dict') else self.__helm
        if self.__yum is not None:
            d['yum'] = self.__yum.as_dict() if hasattr(self.__yum, 'as_dict') else self.__yum
        if self.__maven is not None:
            d['maven'] = self.__maven.as_dict() if hasattr(self.__maven, 'as_dict') else self.__maven
        if self.__raw is not None:
            d['raw'] = self.__raw.as_dict() if hasattr(self.__raw, 'as_dict') else self.__raw
        return d

    def __repr__(self):
        return "<Class repositories. docker: {}, helm: {}, yum: {}, maven: {}, raw: {}>".format(limitedRepr(self.__docker[:20] if isinstance(self.__docker, bytes) else self.__docker), limitedRepr(self.__helm[:20] if isinstance(self.__helm, bytes) else self.__helm), limitedRepr(self.__yum[:20] if isinstance(self.__yum, bytes) else self.__yum), limitedRepr(self.__maven[:20] if isinstance(self.__maven, bytes) else self.__maven), limitedRepr(self.__raw[:20] if isinstance(self.__raw, bytes) else self.__raw))

class packages:
    """
    List of binary packages
    """
    class _docker:
            """
            An OCI image
            """



            _types_map = {
                'repository': {'type': str, 'subtype': None},
                'name': {'type': str, 'subtype': None},
                'tag': {'type': str, 'subtype': None},
                'scope': {'type': str, 'subtype': None},
                'id': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'repository': { 'required': False,},
                'name': { 'required': True,},
                'tag': { 'required': True,},
                'scope': { 'required': False,},
                'id': { 'required': False,},
            }

            def __init__(self
                    , repository='{{repositories.docker}}'
                    , name=None
                    , tag=None
                    , scope=None
                    , id=None
                    ):
                self.__repository = repository
                self.__name = name
                self.__tag = tag
                self.__scope = scope
                self.__id = id
                pass

            def _get_repository(self):
                return self.__repository
            def _set_repository(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("repository must be str")

                self.__repository = value
            repository = property(_get_repository, _set_repository)

            def _get_name(self):
                return self.__name
            def _set_name(self, value):
                if  not isinstance(value, str):
                    raise TypeError("name must be str")

                self.__name = value
            name = property(_get_name, _set_name)

            def _get_tag(self):
                return self.__tag
            def _set_tag(self, value):
                if  not isinstance(value, str):
                    raise TypeError("tag must be str")

                self.__tag = value
            tag = property(_get_tag, _set_tag)

            def _get_scope(self):
                return self.__scope
            def _set_scope(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("scope must be str")

                self.__scope = value
            scope = property(_get_scope, _set_scope)

            def _get_id(self):
                return self.__id
            def _set_id(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("id must be str")

                self.__id = value
            id = property(_get_id, _set_id)


            @staticmethod
            def from_dict(d):
                v = {}
                if "repository" in d:
                    v["repository"] = str.from_dict(d["repository"]) if hasattr(str, 'from_dict') else d["repository"]
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "tag" in d:
                    v["tag"] = str.from_dict(d["tag"]) if hasattr(str, 'from_dict') else d["tag"]
                if "scope" in d:
                    v["scope"] = str.from_dict(d["scope"]) if hasattr(str, 'from_dict') else d["scope"]
                if "id" in d:
                    v["id"] = str.from_dict(d["id"]) if hasattr(str, 'from_dict') else d["id"]
                return packages._docker(**v)


            def as_dict(self):
                d = {}
                if self.__repository is not None:
                    d['repository'] = self.__repository.as_dict() if hasattr(self.__repository, 'as_dict') else self.__repository
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__tag is not None:
                    d['tag'] = self.__tag.as_dict() if hasattr(self.__tag, 'as_dict') else self.__tag
                if self.__scope is not None:
                    d['scope'] = self.__scope.as_dict() if hasattr(self.__scope, 'as_dict') else self.__scope
                if self.__id is not None:
                    d['id'] = self.__id.as_dict() if hasattr(self.__id, 'as_dict') else self.__id
                return d

            def __repr__(self):
                return "<Class _docker. repository: {}, name: {}, tag: {}, scope: {}, id: {}>".format(limitedRepr(self.__repository[:20] if isinstance(self.__repository, bytes) else self.__repository), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__tag[:20] if isinstance(self.__tag, bytes) else self.__tag), limitedRepr(self.__scope[:20] if isinstance(self.__scope, bytes) else self.__scope), limitedRepr(self.__id[:20] if isinstance(self.__id, bytes) else self.__id))

    class _helm:
            """
            An Helm chart
            """



            _types_map = {
                'repository': {'type': str, 'subtype': None},
                'name': {'type': str, 'subtype': None},
                'version': {'type': str, 'subtype': None},
                'doc': {'type': str, 'subtype': None},
                'scope': {'type': str, 'subtype': None},
                'path': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'repository': { 'required': False,},
                'name': { 'required': True,},
                'version': { 'required': True,},
                'doc': { 'required': False,},
                'scope': { 'required': True,},
                'path': { 'required': False,},
            }

            def __init__(self
                    , repository='{{repositories.helm}}'
                    , name=None
                    , version=None
                    , doc=None
                    , scope=None
                    , path=None
                    ):
                self.__repository = repository
                self.__name = name
                self.__version = version
                self.__doc = doc
                self.__scope = scope
                self.__path = path
                pass

            def _get_repository(self):
                return self.__repository
            def _set_repository(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("repository must be str")

                self.__repository = value
            repository = property(_get_repository, _set_repository)

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

            def _get_doc(self):
                return self.__doc
            def _set_doc(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("doc must be str")

                self.__doc = value
            doc = property(_get_doc, _set_doc)

            def _get_scope(self):
                return self.__scope
            def _set_scope(self, value):
                if  not isinstance(value, str):
                    raise TypeError("scope must be str")

                self.__scope = value
            scope = property(_get_scope, _set_scope)

            def _get_path(self):
                return self.__path
            def _set_path(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("path must be str")

                self.__path = value
            path = property(_get_path, _set_path)


            @staticmethod
            def from_dict(d):
                v = {}
                if "repository" in d:
                    v["repository"] = str.from_dict(d["repository"]) if hasattr(str, 'from_dict') else d["repository"]
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "version" in d:
                    v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                if "doc" in d:
                    v["doc"] = str.from_dict(d["doc"]) if hasattr(str, 'from_dict') else d["doc"]
                if "scope" in d:
                    v["scope"] = str.from_dict(d["scope"]) if hasattr(str, 'from_dict') else d["scope"]
                if "path" in d:
                    v["path"] = str.from_dict(d["path"]) if hasattr(str, 'from_dict') else d["path"]
                return packages._helm(**v)


            def as_dict(self):
                d = {}
                if self.__repository is not None:
                    d['repository'] = self.__repository.as_dict() if hasattr(self.__repository, 'as_dict') else self.__repository
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__version is not None:
                    d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                if self.__doc is not None:
                    d['doc'] = self.__doc.as_dict() if hasattr(self.__doc, 'as_dict') else self.__doc
                if self.__scope is not None:
                    d['scope'] = self.__scope.as_dict() if hasattr(self.__scope, 'as_dict') else self.__scope
                if self.__path is not None:
                    d['path'] = self.__path.as_dict() if hasattr(self.__path, 'as_dict') else self.__path
                return d

            def __repr__(self):
                return "<Class _helm. repository: {}, name: {}, version: {}, doc: {}, scope: {}, path: {}>".format(limitedRepr(self.__repository[:20] if isinstance(self.__repository, bytes) else self.__repository), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__doc[:20] if isinstance(self.__doc, bytes) else self.__doc), limitedRepr(self.__scope[:20] if isinstance(self.__scope, bytes) else self.__scope), limitedRepr(self.__path[:20] if isinstance(self.__path, bytes) else self.__path))

    class _yum:
            """
            A rpm
            """



            _types_map = {
                'repository': {'type': str, 'subtype': None},
                'name': {'type': str, 'subtype': None},
                'version': {'type': str, 'subtype': None},
                'scope': {'type': str, 'subtype': None},
                'arch': {'type': str, 'subtype': None},
                'path': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'repository': { 'required': False,},
                'name': { 'required': True,},
                'version': { 'required': True,},
                'scope': { 'required': True,},
                'arch': { 'required': False,},
                'path': { 'required': False,},
            }

            def __init__(self
                    , repository='{{repositories.yum}}'
                    , name=None
                    , version=None
                    , scope=None
                    , arch='noarch'
                    , path=None
                    ):
                self.__repository = repository
                self.__name = name
                self.__version = version
                self.__scope = scope
                self.__arch = arch
                self.__path = path
                pass

            def _get_repository(self):
                return self.__repository
            def _set_repository(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("repository must be str")

                self.__repository = value
            repository = property(_get_repository, _set_repository)

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

            def _get_scope(self):
                return self.__scope
            def _set_scope(self, value):
                if  not isinstance(value, str):
                    raise TypeError("scope must be str")

                self.__scope = value
            scope = property(_get_scope, _set_scope)

            def _get_arch(self):
                return self.__arch
            def _set_arch(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("arch must be str")

                self.__arch = value
            arch = property(_get_arch, _set_arch)

            def _get_path(self):
                return self.__path
            def _set_path(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("path must be str")

                self.__path = value
            path = property(_get_path, _set_path)


            @staticmethod
            def from_dict(d):
                v = {}
                if "repository" in d:
                    v["repository"] = str.from_dict(d["repository"]) if hasattr(str, 'from_dict') else d["repository"]
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "version" in d:
                    v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                if "scope" in d:
                    v["scope"] = str.from_dict(d["scope"]) if hasattr(str, 'from_dict') else d["scope"]
                if "arch" in d:
                    v["arch"] = str.from_dict(d["arch"]) if hasattr(str, 'from_dict') else d["arch"]
                if "path" in d:
                    v["path"] = str.from_dict(d["path"]) if hasattr(str, 'from_dict') else d["path"]
                return packages._yum(**v)


            def as_dict(self):
                d = {}
                if self.__repository is not None:
                    d['repository'] = self.__repository.as_dict() if hasattr(self.__repository, 'as_dict') else self.__repository
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__version is not None:
                    d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                if self.__scope is not None:
                    d['scope'] = self.__scope.as_dict() if hasattr(self.__scope, 'as_dict') else self.__scope
                if self.__arch is not None:
                    d['arch'] = self.__arch.as_dict() if hasattr(self.__arch, 'as_dict') else self.__arch
                if self.__path is not None:
                    d['path'] = self.__path.as_dict() if hasattr(self.__path, 'as_dict') else self.__path
                return d

            def __repr__(self):
                return "<Class _yum. repository: {}, name: {}, version: {}, scope: {}, arch: {}, path: {}>".format(limitedRepr(self.__repository[:20] if isinstance(self.__repository, bytes) else self.__repository), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__scope[:20] if isinstance(self.__scope, bytes) else self.__scope), limitedRepr(self.__arch[:20] if isinstance(self.__arch, bytes) else self.__arch), limitedRepr(self.__path[:20] if isinstance(self.__path, bytes) else self.__path))

    class _maven:
            """
            An artifact
            """



            _types_map = {
                'repository': {'type': str, 'subtype': None},
                'name': {'type': str, 'subtype': None},
                'group': {'type': str, 'subtype': None},
                'classifier': {'type': str, 'subtype': None},
                'type': {'type': str, 'subtype': None},
                'version': {'type': str, 'subtype': None},
                'scope': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'repository': { 'required': False,},
                'name': { 'required': True,},
                'group': { 'required': True,},
                'classifier': { 'required': False,},
                'type': { 'required': False,},
                'version': { 'required': True,},
                'scope': { 'required': False,},
            }

            def __init__(self
                    , repository='{{repositories.maven}}'
                    , name=None
                    , group=None
                    , classifier=None
                    , type=None
                    , version=None
                    , scope=None
                    ):
                self.__repository = repository
                self.__name = name
                self.__group = group
                self.__classifier = classifier
                self.__type = type
                self.__version = version
                self.__scope = scope
                pass

            def _get_repository(self):
                return self.__repository
            def _set_repository(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("repository must be str")

                self.__repository = value
            repository = property(_get_repository, _set_repository)

            def _get_name(self):
                return self.__name
            def _set_name(self, value):
                if  not isinstance(value, str):
                    raise TypeError("name must be str")

                self.__name = value
            name = property(_get_name, _set_name)

            def _get_group(self):
                return self.__group
            def _set_group(self, value):
                if  not isinstance(value, str):
                    raise TypeError("group must be str")

                self.__group = value
            group = property(_get_group, _set_group)

            def _get_classifier(self):
                return self.__classifier
            def _set_classifier(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("classifier must be str")

                self.__classifier = value
            classifier = property(_get_classifier, _set_classifier)

            def _get_type(self):
                return self.__type
            def _set_type(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("type must be str")

                self.__type = value
            type = property(_get_type, _set_type)

            def _get_version(self):
                return self.__version
            def _set_version(self, value):
                if  not isinstance(value, str):
                    raise TypeError("version must be str")

                self.__version = value
            version = property(_get_version, _set_version)

            def _get_scope(self):
                return self.__scope
            def _set_scope(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("scope must be str")

                self.__scope = value
            scope = property(_get_scope, _set_scope)


            @staticmethod
            def from_dict(d):
                v = {}
                if "repository" in d:
                    v["repository"] = str.from_dict(d["repository"]) if hasattr(str, 'from_dict') else d["repository"]
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "group" in d:
                    v["group"] = str.from_dict(d["group"]) if hasattr(str, 'from_dict') else d["group"]
                if "classifier" in d:
                    v["classifier"] = str.from_dict(d["classifier"]) if hasattr(str, 'from_dict') else d["classifier"]
                if "type" in d:
                    v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
                if "version" in d:
                    v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
                if "scope" in d:
                    v["scope"] = str.from_dict(d["scope"]) if hasattr(str, 'from_dict') else d["scope"]
                return packages._maven(**v)


            def as_dict(self):
                d = {}
                if self.__repository is not None:
                    d['repository'] = self.__repository.as_dict() if hasattr(self.__repository, 'as_dict') else self.__repository
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__group is not None:
                    d['group'] = self.__group.as_dict() if hasattr(self.__group, 'as_dict') else self.__group
                if self.__classifier is not None:
                    d['classifier'] = self.__classifier.as_dict() if hasattr(self.__classifier, 'as_dict') else self.__classifier
                if self.__type is not None:
                    d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
                if self.__version is not None:
                    d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
                if self.__scope is not None:
                    d['scope'] = self.__scope.as_dict() if hasattr(self.__scope, 'as_dict') else self.__scope
                return d

            def __repr__(self):
                return "<Class _maven. repository: {}, name: {}, group: {}, classifier: {}, type: {}, version: {}, scope: {}>".format(limitedRepr(self.__repository[:20] if isinstance(self.__repository, bytes) else self.__repository), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__group[:20] if isinstance(self.__group, bytes) else self.__group), limitedRepr(self.__classifier[:20] if isinstance(self.__classifier, bytes) else self.__classifier), limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__scope[:20] if isinstance(self.__scope, bytes) else self.__scope))

    class _raw:
            """
            An artifact
            """



            _types_map = {
                'repository': {'type': str, 'subtype': None},
                'type': {'type': str, 'subtype': None},
                'name': {'type': str, 'subtype': None},
                'url': {'type': str, 'subtype': None},
                'scope': {'type': str, 'subtype': None},
                'path': {'type': str, 'subtype': None},
            }
            _formats_map = {
                'url': 'uri',
            }
            _validations_map = {
                'repository': { 'required': False,},
                'type': { 'required': True,},
                'name': { 'required': True,},
                'url': { 'required': False,},
                'scope': { 'required': False,},
                'path': { 'required': False,},
            }

            def __init__(self
                    , repository='{{repositories.raw}}'
                    , type=None
                    , name=None
                    , url=None
                    , scope=None
                    , path=None
                    ):
                self.__repository = repository
                self.__type = type
                self.__name = name
                self.__url = url
                self.__scope = scope
                self.__path = path
                pass

            def _get_repository(self):
                return self.__repository
            def _set_repository(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("repository must be str")

                self.__repository = value
            repository = property(_get_repository, _set_repository)

            def _get_type(self):
                return self.__type
            def _set_type(self, value):
                if  not isinstance(value, str):
                    raise TypeError("type must be str")

                self.__type = value
            type = property(_get_type, _set_type)

            def _get_name(self):
                return self.__name
            def _set_name(self, value):
                if  not isinstance(value, str):
                    raise TypeError("name must be str")

                self.__name = value
            name = property(_get_name, _set_name)

            def _get_url(self):
                return self.__url
            def _set_url(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("url must be str")

                self.__url = value
            url = property(_get_url, _set_url)

            def _get_scope(self):
                return self.__scope
            def _set_scope(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("scope must be str")

                self.__scope = value
            scope = property(_get_scope, _set_scope)

            def _get_path(self):
                return self.__path
            def _set_path(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("path must be str")

                self.__path = value
            path = property(_get_path, _set_path)


            @staticmethod
            def from_dict(d):
                v = {}
                if "repository" in d:
                    v["repository"] = str.from_dict(d["repository"]) if hasattr(str, 'from_dict') else d["repository"]
                if "type" in d:
                    v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "url" in d:
                    v["url"] = str.from_dict(d["url"]) if hasattr(str, 'from_dict') else d["url"]
                if "scope" in d:
                    v["scope"] = str.from_dict(d["scope"]) if hasattr(str, 'from_dict') else d["scope"]
                if "path" in d:
                    v["path"] = str.from_dict(d["path"]) if hasattr(str, 'from_dict') else d["path"]
                return packages._raw(**v)


            def as_dict(self):
                d = {}
                if self.__repository is not None:
                    d['repository'] = self.__repository.as_dict() if hasattr(self.__repository, 'as_dict') else self.__repository
                if self.__type is not None:
                    d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__url is not None:
                    d['url'] = self.__url.as_dict() if hasattr(self.__url, 'as_dict') else self.__url
                if self.__scope is not None:
                    d['scope'] = self.__scope.as_dict() if hasattr(self.__scope, 'as_dict') else self.__scope
                if self.__path is not None:
                    d['path'] = self.__path.as_dict() if hasattr(self.__path, 'as_dict') else self.__path
                return d

            def __repr__(self):
                return "<Class _raw. repository: {}, type: {}, name: {}, url: {}, scope: {}, path: {}>".format(limitedRepr(self.__repository[:20] if isinstance(self.__repository, bytes) else self.__repository), limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__url[:20] if isinstance(self.__url, bytes) else self.__url), limitedRepr(self.__scope[:20] if isinstance(self.__scope, bytes) else self.__scope), limitedRepr(self.__path[:20] if isinstance(self.__path, bytes) else self.__path))




    _types_map = {
        'docker': {'type': list, 'subtype': _docker},
        'helm': {'type': list, 'subtype': _helm},
        'yum': {'type': list, 'subtype': _yum},
        'maven': {'type': list, 'subtype': _maven},
        'raw': {'type': list, 'subtype': _raw},
    }
    _formats_map = {
    }
    _validations_map = {
        'docker': { 'required': False,},
        'helm': { 'required': False,},
        'yum': { 'required': False,},
        'maven': { 'required': False,},
        'raw': { 'required': False,},
    }

    def __init__(self
            , docker=None
            , helm=None
            , yum=None
            , maven=None
            , raw=None
            ):
        """
        :param docker: A list of OCI images
        :param helm: A list of Helm charts
        :param yum: A list of rpm packages
        :param maven: A list of Maven artifacts
        :param raw: A list of raw artifacts
        """
        self.__docker = docker
        self.__helm = helm
        self.__yum = yum
        self.__maven = maven
        self.__raw = raw
        pass

    def _get_docker(self):
        return self.__docker
    def _set_docker(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("docker must be list")
        if value is not None and  not all(isinstance(i, packages._docker) for i in value):
            raise TypeError("docker list values must be packages._docker")

        self.__docker = value
    docker = property(_get_docker, _set_docker)
    """
    A list of OCI images
    """

    def _get_helm(self):
        return self.__helm
    def _set_helm(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("helm must be list")
        if value is not None and  not all(isinstance(i, packages._helm) for i in value):
            raise TypeError("helm list values must be packages._helm")

        self.__helm = value
    helm = property(_get_helm, _set_helm)
    """
    A list of Helm charts
    """

    def _get_yum(self):
        return self.__yum
    def _set_yum(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("yum must be list")
        if value is not None and  not all(isinstance(i, packages._yum) for i in value):
            raise TypeError("yum list values must be packages._yum")

        self.__yum = value
    yum = property(_get_yum, _set_yum)
    """
    A list of rpm packages
    """

    def _get_maven(self):
        return self.__maven
    def _set_maven(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("maven must be list")
        if value is not None and  not all(isinstance(i, packages._maven) for i in value):
            raise TypeError("maven list values must be packages._maven")

        self.__maven = value
    maven = property(_get_maven, _set_maven)
    """
    A list of Maven artifacts
    """

    def _get_raw(self):
        return self.__raw
    def _set_raw(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("raw must be list")
        if value is not None and  not all(isinstance(i, packages._raw) for i in value):
            raise TypeError("raw list values must be packages._raw")

        self.__raw = value
    raw = property(_get_raw, _set_raw)
    """
    A list of raw artifacts
    """


    @staticmethod
    def from_dict(d):
        v = {}
        if "docker" in d:
            v["docker"] = [packages._docker.from_dict(p) if hasattr(packages._docker, 'from_dict') else p for p in d["docker"]]
        if "helm" in d:
            v["helm"] = [packages._helm.from_dict(p) if hasattr(packages._helm, 'from_dict') else p for p in d["helm"]]
        if "yum" in d:
            v["yum"] = [packages._yum.from_dict(p) if hasattr(packages._yum, 'from_dict') else p for p in d["yum"]]
        if "maven" in d:
            v["maven"] = [packages._maven.from_dict(p) if hasattr(packages._maven, 'from_dict') else p for p in d["maven"]]
        if "raw" in d:
            v["raw"] = [packages._raw.from_dict(p) if hasattr(packages._raw, 'from_dict') else p for p in d["raw"]]
        return packages(**v)


    def as_dict(self):
        d = {}
        if self.__docker is not None:
            d['docker'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__docker]
        if self.__helm is not None:
            d['helm'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__helm]
        if self.__yum is not None:
            d['yum'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__yum]
        if self.__maven is not None:
            d['maven'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__maven]
        if self.__raw is not None:
            d['raw'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__raw]
        return d

    def __repr__(self):
        return "<Class packages. docker: {}, helm: {}, yum: {}, maven: {}, raw: {}>".format(limitedRepr(self.__docker[:20] if isinstance(self.__docker, bytes) else self.__docker), limitedRepr(self.__helm[:20] if isinstance(self.__helm, bytes) else self.__helm), limitedRepr(self.__yum[:20] if isinstance(self.__yum, bytes) else self.__yum), limitedRepr(self.__maven[:20] if isinstance(self.__maven, bytes) else self.__maven), limitedRepr(self.__raw[:20] if isinstance(self.__raw, bytes) else self.__raw))

class tool:
    """
    Tool used for tests
    """



    _types_map = {
        'name': {'type': str, 'subtype': None},
        'version': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'name': { 'required': True,},
        'version': { 'required': True,},
    }

    def __init__(self
            , name=None
            , version=None
            ):
        """
        :param name: Name of the test tool.
        """
        self.__name = name
        self.__version = version
        pass

    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if  not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value
    name = property(_get_name, _set_name)
    """
    Name of the test tool.
    """

    def _get_version(self):
        return self.__version
    def _set_version(self, value):
        if  not isinstance(value, str):
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
        return tool(**v)


    def as_dict(self):
        d = {}
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__version is not None:
            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
        return d

    def __repr__(self):
        return "<Class tool. name: {}, version: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version))

class deliverable:
    """
    Contain all deliverable-related informations
    """
    class _softwarecenter:
            """
            Contain link for the software center
            """



            _types_map = {
                'internal': {'type': str, 'subtype': None},
                'customers': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'internal': { 'required': False,},
                'customers': { 'required': False,},
            }

            def __init__(self
                    , internal=None
                    , customers=None
                    ):
                self.__internal = internal
                self.__customers = customers
                pass

            def _get_internal(self):
                return self.__internal
            def _set_internal(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("internal must be str")

                self.__internal = value
            internal = property(_get_internal, _set_internal)

            def _get_customers(self):
                return self.__customers
            def _set_customers(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("customers must be str")

                self.__customers = value
            customers = property(_get_customers, _set_customers)


            @staticmethod
            def from_dict(d):
                v = {}
                if "internal" in d:
                    v["internal"] = str.from_dict(d["internal"]) if hasattr(str, 'from_dict') else d["internal"]
                if "customers" in d:
                    v["customers"] = str.from_dict(d["customers"]) if hasattr(str, 'from_dict') else d["customers"]
                return deliverable._softwarecenter(**v)


            def as_dict(self):
                d = {}
                if self.__internal is not None:
                    d['internal'] = self.__internal.as_dict() if hasattr(self.__internal, 'as_dict') else self.__internal
                if self.__customers is not None:
                    d['customers'] = self.__customers.as_dict() if hasattr(self.__customers, 'as_dict') else self.__customers
                return d

            def __repr__(self):
                return "<Class _softwarecenter. internal: {}, customers: {}>".format(limitedRepr(self.__internal[:20] if isinstance(self.__internal, bytes) else self.__internal), limitedRepr(self.__customers[:20] if isinstance(self.__customers, bytes) else self.__customers))

    class _media:
            """
            A Product media
            """



            _types_map = {
                'name': {'type': str, 'subtype': None},
                'servers': {'type': list, 'subtype': str},
                'type': {'type': str, 'subtype': None},
                'dateCreation': {'type': str, 'subtype': None},
                'dateModification': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'name': { 'required': True,},
                'servers': { 'required': False,},
                'type': { 'required': True,},
                'dateCreation': { 'required': False,},
                'dateModification': { 'required': False,},
            }

            def __init__(self
                    , name=None
                    , servers=None
                    , type=None
                    , dateCreation=None
                    , dateModification=None
                    ):
                """
                :param servers: list of servers
                """
                self.__name = name
                self.__servers = servers
                self.__type = type
                self.__dateCreation = dateCreation
                self.__dateModification = dateModification
                pass

            def _get_name(self):
                return self.__name
            def _set_name(self, value):
                if  not isinstance(value, str):
                    raise TypeError("name must be str")

                self.__name = value
            name = property(_get_name, _set_name)

            def _get_servers(self):
                return self.__servers
            def _set_servers(self, value):
                if value is not None and  not isinstance(value, list):
                    raise TypeError("servers must be list")
                if value is not None and  not all(isinstance(i, str) for i in value):
                    raise TypeError("servers list values must be str")

                self.__servers = value
            servers = property(_get_servers, _set_servers)
            """
            list of servers
            """

            def _get_type(self):
                return self.__type
            def _set_type(self, value):
                if  not isinstance(value, str):
                    raise TypeError("type must be str")

                self.__type = value
            type = property(_get_type, _set_type)

            def _get_dateCreation(self):
                return self.__dateCreation
            def _set_dateCreation(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("dateCreation must be str")

                self.__dateCreation = value
            dateCreation = property(_get_dateCreation, _set_dateCreation)

            def _get_dateModification(self):
                return self.__dateModification
            def _set_dateModification(self, value):
                if value is not None and  not isinstance(value, str):
                    raise TypeError("dateModification must be str")

                self.__dateModification = value
            dateModification = property(_get_dateModification, _set_dateModification)


            @staticmethod
            def from_dict(d):
                v = {}
                if "name" in d:
                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                if "servers" in d:
                    v["servers"] = [str.from_dict(p) if hasattr(str, 'from_dict') else p for p in d["servers"]]
                if "type" in d:
                    v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
                if "dateCreation" in d:
                    v["dateCreation"] = str.from_dict(d["dateCreation"]) if hasattr(str, 'from_dict') else d["dateCreation"]
                if "dateModification" in d:
                    v["dateModification"] = str.from_dict(d["dateModification"]) if hasattr(str, 'from_dict') else d["dateModification"]
                return deliverable._media(**v)


            def as_dict(self):
                d = {}
                if self.__name is not None:
                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                if self.__servers is not None:
                    d['servers'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__servers]
                if self.__type is not None:
                    d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
                if self.__dateCreation is not None:
                    d['dateCreation'] = self.__dateCreation.as_dict() if hasattr(self.__dateCreation, 'as_dict') else self.__dateCreation
                if self.__dateModification is not None:
                    d['dateModification'] = self.__dateModification.as_dict() if hasattr(self.__dateModification, 'as_dict') else self.__dateModification
                return d

            def __repr__(self):
                return "<Class _media. name: {}, servers: {}, type: {}, dateCreation: {}, dateModification: {}>".format(limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__servers[:20] if isinstance(self.__servers, bytes) else self.__servers), limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type), limitedRepr(self.__dateCreation[:20] if isinstance(self.__dateCreation, bytes) else self.__dateCreation), limitedRepr(self.__dateModification[:20] if isinstance(self.__dateModification, bytes) else self.__dateModification))




    _types_map = {
        'version': {'type': str, 'subtype': None},
        'sku': {'type': str, 'subtype': None},
        'intent': {'type': str, 'subtype': None},
        'softwarecenter': {'type': _softwarecenter, 'subtype': None},
        'servers': {'type': dict, 'subtype': None},
        'media': {'type': list, 'subtype': _media},
    }
    _formats_map = {
    }
    _validations_map = {
        'version': { 'required': False,},
        'sku': { 'required': False,},
        'intent': { 'required': False,},
        'softwarecenter': { 'required': False,},
        'servers': { 'required': False,},
        'media': { 'required': False,},
    }

    def __init__(self
            , version=None
            , sku=None
            , intent=None
            , softwarecenter=None
            , servers=None
            , media=None
            ):
        """
        :param softwarecenter: Contain link for the software center
        :param servers: list of servers of release
        :param media: List media linked to the Product
        """
        self.__version = version
        self.__sku = sku
        self.__intent = intent
        self.__softwarecenter = softwarecenter
        self.__servers = servers
        self.__media = media
        pass

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

    def _get_intent(self):
        return self.__intent
    def _set_intent(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("intent must be str")

        self.__intent = value
    intent = property(_get_intent, _set_intent)

    def _get_softwarecenter(self):
        return self.__softwarecenter
    def _set_softwarecenter(self, value):
        if value is not None and  not isinstance(value, deliverable._softwarecenter):
            raise TypeError("softwarecenter must be deliverable._softwarecenter")

        self.__softwarecenter = value
    softwarecenter = property(_get_softwarecenter, _set_softwarecenter)
    """
    Contain link for the software center
    """

    def _get_servers(self):
        return self.__servers
    def _set_servers(self, value):
        if value is not None and  not isinstance(value, dict):
            raise TypeError("servers must be dict")

        self.__servers = value
    servers = property(_get_servers, _set_servers)
    """
    list of servers of release
    """

    def _get_media(self):
        return self.__media
    def _set_media(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("media must be list")
        if value is not None and  not all(isinstance(i, deliverable._media) for i in value):
            raise TypeError("media list values must be deliverable._media")

        self.__media = value
    media = property(_get_media, _set_media)
    """
    List media linked to the Product
    """


    @staticmethod
    def from_dict(d):
        v = {}
        if "version" in d:
            v["version"] = str.from_dict(d["version"]) if hasattr(str, 'from_dict') else d["version"]
        if "sku" in d:
            v["sku"] = str.from_dict(d["sku"]) if hasattr(str, 'from_dict') else d["sku"]
        if "intent" in d:
            v["intent"] = str.from_dict(d["intent"]) if hasattr(str, 'from_dict') else d["intent"]
        if "softwarecenter" in d:
            v["softwarecenter"] = deliverable._softwarecenter.from_dict(d["softwarecenter"]) if hasattr(deliverable._softwarecenter, 'from_dict') else d["softwarecenter"]
        if "servers" in d:
            v["servers"] = dict.from_dict(d["servers"]) if hasattr(dict, 'from_dict') else d["servers"]
        if "media" in d:
            v["media"] = [deliverable._media.from_dict(p) if hasattr(deliverable._media, 'from_dict') else p for p in d["media"]]
        return deliverable(**v)


    def as_dict(self):
        d = {}
        if self.__version is not None:
            d['version'] = self.__version.as_dict() if hasattr(self.__version, 'as_dict') else self.__version
        if self.__sku is not None:
            d['sku'] = self.__sku.as_dict() if hasattr(self.__sku, 'as_dict') else self.__sku
        if self.__intent is not None:
            d['intent'] = self.__intent.as_dict() if hasattr(self.__intent, 'as_dict') else self.__intent
        if self.__softwarecenter is not None:
            d['softwarecenter'] = self.__softwarecenter.as_dict() if hasattr(self.__softwarecenter, 'as_dict') else self.__softwarecenter
        if self.__servers is not None:
            d['servers'] = self.__servers.as_dict() if hasattr(self.__servers, 'as_dict') else self.__servers
        if self.__media is not None:
            d['media'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__media]
        return d

    def __repr__(self):
        return "<Class deliverable. version: {}, sku: {}, intent: {}, softwarecenter: {}, servers: {}, media: {}>".format(limitedRepr(self.__version[:20] if isinstance(self.__version, bytes) else self.__version), limitedRepr(self.__sku[:20] if isinstance(self.__sku, bytes) else self.__sku), limitedRepr(self.__intent[:20] if isinstance(self.__intent, bytes) else self.__intent), limitedRepr(self.__softwarecenter[:20] if isinstance(self.__softwarecenter, bytes) else self.__softwarecenter), limitedRepr(self.__servers[:20] if isinstance(self.__servers, bytes) else self.__servers), limitedRepr(self.__media[:20] if isinstance(self.__media, bytes) else self.__media))

