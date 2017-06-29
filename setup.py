# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import
from numpy.distutils.core import setup, Extension

setup(
    name='_cea',
    ext_modules=[Extension(name='_cea', sources=["src/cea2.f"])]
    )