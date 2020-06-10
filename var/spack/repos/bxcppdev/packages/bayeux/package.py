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

class Bayeux(CMakePackage):
    """ Core Persistency, Geometry and Data Processing C++ Library
        for Particle and Nuclear Physics Experiments. """

    homepage = "https://github.com/BxCppDev/Bayeux"
    url      = "https://github.com/BxCppDev/Bayeux/archive/3.4.1.tar.gz"

    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.4.1', sha256='94785ec23c77e5b4785d39cb6a6f94fa9f0229989778bdf688ef43b7a4fead8a')
    version('develop', git='https://github.com/BxCppDev/Bayeux.git', branch='develop')

    _cxxstd_values = ('11', '14', '17')
    variant('cxxstd',
            default=_cxxstd_values[0],
            values=_cxxstd_values,
            multi=False,
            description='Use the specified C++ standard when building.')
    variant('docs', default=False)
    variant('system-doxygen', default=False)
    variant('qt', default=False)
    variant('bxdecay0', default=False)
    variant('geant4', default=False)

    depends_on('cmake@3.10.2:', type='build')
    depends_on('boost@1.69.0:')
    depends_on('gsl@2.4:')
    depends_on('camp@0.8.4:')
    # for std in _cxxstd_values:
    #     depends_on('xerces-c@3.0.0:   cxxstd=' + std, when='cxxstd=' + std)
    depends_on('xerces-c@3.0.0:')
    depends_on('clhep@2.1.3.1:')
    depends_on('root@6.12.04:6.16.00')
    depends_on('bxdecay0@1.0.0:', when='@develop,3.4.2: +bxdecay0')
    depends_on('gnuplot@4.0:')
    depends_on('doxygen@1.8:', when='+docs ~system-doxygen')
    depends_on('qt@5.2.0:', when='+qt')
    depends_on('geant4@9.6.4', when='+geant4')

    
    def cmake_args(self):
        spec = self.spec
        args = ['-DCMAKE_CXX_STANDARD={0}'.format(self.spec.variants['cxxstd'].value)]
        args.append("-DBAYEUX_WITH_DEVELOPER_TOOLS=ON")

        if "+bxdecay0" in spec:
            args.append("-DBAYEUX_WITH_BXDECAY0=ON")
            args.append('-DBxDecay0_DIR={0}'.format(spec['bxdecay0'].prefix))
        else:
            args.append("-DBAYEUX_WITH_BXDECAY0=OFF")

        if "+qt" in spec:
            args.append("-DBAYEUX_WITH_QT_GUI=ON")
        else:
            args.append("-DBAYEUX_WITH_QT_GUI=OFF")

        if "+docs" in spec:
            args.append("-DBAYEUX_WITH_DOCS=ON")
            args.append("-DBAYEUX_WITH_DOCS_OCD=ON")
        else:
            args.append("-DBAYEUX_WITH_DOCS=OFF")
         
        if "+geant4" in spec:
            args.append("-DBAYEUX_WITH_GEANT4_MODULE=ON")
        else:
            args.append("-DBAYEUX_WITH_GEANT4_MODULE=OFF")
            
        return args

# ----------------------------------------------------------------------------
