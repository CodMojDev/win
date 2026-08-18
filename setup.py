#
# The setup file for Win package
#

import os, sys

if os.name != 'nt':
    raise RuntimeError('The package is only for Windows NT.')

if sys.version_info < (3, 10):
    raise RuntimeError('This package requires Python 3.10 or higher')

if sys.version_info >= (3, 15):
    raise RuntimeError('This package requires Python 3.14 or lower to 3.10, >=3.15 is not compatible with it')

from setuptools import setup, find_packages

setup(
    name='win',
    version='1.0.0',
    package_dir={'': '.'},
    packages=find_packages(),
    package_data={
        'win': [
            'abs/controls/data/*.bmp',
            'abs/data/*.*',
            'com/data/*.*',
            'com/icl/iclstorage/*.*'
        ]
    },
    include_package_data=True
)