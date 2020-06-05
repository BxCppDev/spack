# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install bxdecay0
#
# You can edit this file again by typing:
#
#     spack edit bxdecay0
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class Bxdecay0(CMakePackage):
    """C++ port of the legacy Decay0 FORTRAN library and extensions."""

    homepage = "https://github.com/BxCppDev/bxdecay0"
    url      = "https://github.com/BxCppDev/bxdecay0/archive/1.0.1.tar.gz"

    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.0.1', sha256='fc5afdce221babc0b49b30cbc123cd8d3feac16ac22bef2c3cda00abe693e550')
    version('develop', git='https://github.com/BxCppDev/bxdecay0.git', branch='develop')

    depends_on('gsl@2.4')
    depends_on('cmake', type='build')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args

# ----------------------------------------------------------------------------
