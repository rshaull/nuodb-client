from enum import Enum
from dataclasses import dataclass


class Bundles(str, Enum):
    CPP_DRIVER = 'cpp-driver'
    TOOLS = 'tools'
