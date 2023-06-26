from enum import Enum


class VersionTypes(str, Enum):
    PACKAGE = 'package'
    DATE = 'date'

class Bundles(str, Enum):
    CLIENT = 'client'
    C_DRIVER = 'c-driver'
    CPP_DRIVER = 'cpp-driver'
    TOOLS = 'tools'

    def get_version_type(self):
        if self == Bundles.CLIENT:
            return VersionTypes.DATE
        return VersionTypes.PACKAGE

    @staticmethod
    def default():
        return Bundles.CLIENT
