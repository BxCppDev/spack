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
#     spack install camp
#
# You can edit this file again by typing:
#
#     spack edit camp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class Camp(CMakePackage):
    """CAMP is a multi-purpose C++ reflection library."""

    homepage = "https://github.com/IRCAD-IHU/camp"
    url      = "https://github.com/IRCAD-IHU/camp/archive/0.8.4.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.8.4', sha256='4063f29c63ed0505f4045b0c8855c48c31233f392a441441c17a08579fc69c73')

    patch('camp-0.8.4-fix-missing_boost_enable_if.patch',
          level=1,
          when='@0.8.4',
          sha256='f5162c3baea254dbafc18a142216c874a301a6e443e4ac68fdaf2818fcf366f4')
    
    depends_on('boost@1.69.0')

    

    
    # def cmake_args(self):
    #     # Arguments other than CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
    #     args = []
    #     return args
