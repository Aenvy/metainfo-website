# Metainfo base class
# description: Base class for auto-generated jsonschema classes
# author: Nicolas Drufin <nicolas.drufin@hpe.com>
import re
from datetime import datetime
try:
    from ansible.module_utils.schema.__init__ import __version__
    from ansible.module_utils.schema.definitions import event
except ImportError:
    from module_utils.schema.__init__ import __version__
    from module_utils.schema.definitions import event


class MetainfoBase:
    def __init__(self, *args, **kwargs):
        """
        Abstract constructor
        """
        # setup default schema if not exist
        if hasattr(self, "schema") and not self.schema:
            name = self.__class__.__name__
            splitted = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', name)).lower().split()
            self.schema = "{}/{}.json".format(__version__, ".".join(splitted))
        # setup default history if not event
        if hasattr(self, "history") and not self.history:
            create_event = event(
                date=datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
                type="Create",
                details="Created by python schema library v%s" % __version__
            )
            self.history = [create_event]

    def __eq__(self, other):
        return (
            self.ident.groupId == other.ident.groupId and
            self.ident.artifactId == other.ident.artifactId and
            self.ident.version == other.ident.version
        )

    def __hash__(self):
        return hash(self.ident.as_dict().values())

    def get_schema_name(self):
        """
        Return schema name if exist
        """
        if hasattr(self, "schema") and "/" in self.schema:
            return self.schema.split("/")[1]

    def get_schema_version(self):
        """
        Return schema name if exist
        """
        if hasattr(self, "schema") and "/" in self.schema:
            return self.schema.split("/")[0]

    def as_dict(self):
        return {}
