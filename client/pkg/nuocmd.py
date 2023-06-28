# (C) Copyright NuoDB, Inc. 2023  All Rights Reserved.
#
# Add nuocmd

import os
import shutil

from client.artifact import PyPIMetadata
from client.package import Package
from client.stage import Stage
from client.utils import Globals, getcontents, rmdir, mkdir, pipinstall
from client.bundles import Bundles

from client.pkg.pynuoadmin import PyNuoadminPackage


# nuocmd is installed by pynuoadmin, this is a trivial renaming in the manifest
class NuocmdPackage(PyNuoadminPackage):
    """Add the nuocmd client tool."""

    __PKGNAME = 'nuocmd'

    def __init__(self):
        super(PyNuoadminPackage, self).__init__(self.__PKGNAME)

        self._file = None
        self._ac_file = None

        self.staged = [Stage(self.__PKGNAME,
                             title='nuocmd',
                             requirements='Python 3',
                             bundle=Bundles.TOOLS)]

        self.stage = self.staged[0]


# Create and register this package
NuocmdPackage()
