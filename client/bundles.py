from enum import Enum


class Bundles(str, Enum):
    CLIENT = 'client'
    CPP_DRIVER = 'cpp-driver'
    TOOLS = 'tools'

    @staticmethod
    def default():
        return Bundles.CLIENT
