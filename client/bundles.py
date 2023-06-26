import json

from enum import Enum


class Bundle(str, Enum):
    CLIENT = 'client'
    C_DRIVER = 'c-driver'
    CPP_DRIVER = 'cpp-driver'
    TOOLS = 'tools'

    @staticmethod
    def default():
        return Bundle.CLIENT
