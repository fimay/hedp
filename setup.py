#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright CNRS 2012,
# Roman Yurchak (LULI)
# This software is governed by the CeCILL-B license under French law and
# abiding by the rules of distribution of free software.

import sys
import os.path
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
#from distutils.core import setup
#from distutils.extension import Extension
import numpy as np
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True


# Optional path to find the the GNU scientific library (GSL)

INCLUDE_GSL = None #  "/usr/include"
LIB_GSL = None #  "/usr/lib64"


if sys.platform != 'win32':
    compile_args =  dict( extra_compile_args=['-O2', '-march=core2', '-mtune=native'],
                 extra_link_args=['-O2', '-march=core2', '-mtune=native'])
else:
    compile_args = {}


ext_modules=[
    Extension("hedp.lib.integrators",
             ["hedp/lib/integrators.pyx"],
             **compile_args),
    Extension("hedp.lib.selectors",
             ["hedp/lib/selectors.pyx"],
             **compile_args),
]

include_dirs= [ np.get_include() ]

if INCLUDE_GSL:
    ext_modules.append(
             Extension("hedp.lib.multigroup",
                 ["hedp/lib/multigroup.pyx"],
                 libraries=['gsl', 'gslcblas'],
                 library_dirs=[LIB_GSL],
                 **compile_args
             ))
    include_dirs.append(INCLUDE_GSL)

setup(name='hedp',
      version='0.1.0',
      description='Toolkit for HEDP experiments analysis and postprocessing of related radiative-hydrodynamic simulations',
      author='Roman Yurchak',
      author_email='rth@crans.org',
      packages=find_packages(),
      cmdclass= {'build_ext': build_ext},
      ext_modules= ext_modules,
      include_dirs=include_dirs,
      package_data={'hedp': [os.path.join('tests','data','io', '*'),
                             os.path.join('tests','data','opacity','*'),
                             os.path.join('data','db', '*')] },
      test_suite="hedp.tests.run"
     )

