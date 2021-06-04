## =========================================================
## Copyright 2019 Dietrich Bollmann
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##      http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------

"""setup.py:

Setup file for the newskylabs.temple.python package and tools.

"""

import setuptools 
import codecs
import os

## =========================================================
## Setup utilities
## ---------------------------------------------------------

def read_file(*parts):
    """
    Read a file and return its content
    """
    package_dir = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(package_dir, *parts), 'r') as fh:
        return fh.read()

def find_packages(namespace):
    """
    Return a list of all Python packages defined in the 'namespace'
    directory
    """
    return [
        '{}.{}'.format(namespace, package) 
        for package in setuptools.PackageFinder.find(where=namespace)
    ]

## =========================================================
## Setup
## ---------------------------------------------------------

namespace    = 'newskylabs'
subnamespace = 'temple'

# Load the package metadata 
exec(read_file(namespace, subnamespace, '__about__.py'))

# Read the long description
long_description = read_file('README.md')

# Find the list of packages
packages = find_packages(namespace)

# DEBUG
print('DEBUG packages:', packages)

# Setup package
setuptools.setup(
    name=__package_name__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=__author__,
    author_email=__email__,
    license=__license__,
    url=__url__,
    packages=packages,
    entry_points={
        'console_scripts': [
            'temple = newskylabs.temple.__main__:cli',
        ]
    },
    package_data={
        'newskylabs.temple': ['scripts/default_settings.yaml'],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    platforms=['Posix', 'Unix', 'Linux', 'MacOS X', 'Windows'],
    install_requires=[
        'newskylabs-utilities @ git+https://github.com/newskylabs/newskylabs-utilities#egg=newskylabs-utilities-0.0.1.dev1',
    ],
)

## =========================================================
## =========================================================

## fin.
