from enum import Enum


class Bundles(dict, Enum):
    CLI_TOOLS = {'name': 'cli-tools', 'title': 'CLI tools'}
    DRIVERS = {'name': 'drivers', 'title': 'Drivers'}

    def __str__(self):
        return self['name']
