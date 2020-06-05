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
#     spack install hepmc3
#
# You can edit this file again by typing:
#
#     spack edit hepmc3
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class Hepmc3(CMakePackage):
    """HepMC event record"""

    homepage = "https://gitlab.cern.ch/hepmc/HepMC3"
    url      = "https://gitlab.cern.ch/hepmc/HepMC3/-/archive/3.2.0/HepMC3-3.2.0.tar.gz"

    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.2.0', sha256='f132387763d170f25a7cc9f0bd586b83373c09acf0c3daa5504063ba460f89fc')

    # depends_on('foo')

    def cmake_args(self):
        args = [ "-DHEPMC3_ENABLE_PYTHON=OFF" , # Fails
                 "-DHEPMC3_ENABLE_ROOTIO=OFF" ,
                 "-DHEPMC3_ENABLE_SEARCH=OFF" ,
                 "-DHEPMC3_ENABLE_TEST=OFF" ,
                 "-DHEPMC3_BUILD_DOCS=OFF" ,
                 "-DHEPMC3_BUILD_EXAMPLES=OFF" ]
        return args

# ----------------------------------------------------------------------------
    
