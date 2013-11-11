###############################################################################
##
##  Copyright 2013 (C) Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from setuptools import setup, find_packages

LONGSDESC = """
Taschenmesser is a toolbelt containing builders for SCons. It helps you getting stuff done.

It contains builders for:

  - SVG optimization (Scour-based)
  - SVG2PNG conversion (Inkscape-based)
  - Amazon Web Service (S3 Delta Uploads etc)
  - Google Closure (JavaScript optimization)
  - File utils (GZip etc)

License: Apache 2.0

Fork me on GitHub: https://github.com/oberstet/taschenmesser
"""

setup (
   name = 'taschenmesser',
   version = '0.0.4',
   description = 'Taschenmesser, a toolbelt with plugins for SCons',
   long_description = LONGSDESC,
   license = 'Apache License 2.0',
   author = 'Tavendo GmbH',
   author_email = 'contact@tavendo.de',
   url = 'http://www.tavendo.de',
   platforms = ('Any'),
   install_requires = ['setuptools'],
   extras_require = {
      'aws': ["boto"],
      'svg': ["scour>=0.27"]
   },
   packages = find_packages(),
   #include_package_data = True,
   zip_safe = False,
   entry_points = {},
   ## http://pypi.python.org/pypi?%3Aaction=list_classifiers
   ##
   classifiers = ["License :: OSI Approved :: Apache Software License",
                  "Development Status :: 3 - Alpha",
                  "Environment :: Console",
                  "Framework :: Twisted",
                  "Intended Audience :: Developers",
                  "Intended Audience :: System Administrators",
                  "Operating System :: OS Independent",
                  "Programming Language :: Python",
                  "Topic :: Database",
                  "Topic :: Internet",
                  "Topic :: Software Development",
                  "Topic :: Software Development :: Build Tools",
                  "Topic :: Software Development :: Testing",
                  "Topic :: System :: Systems Administration",
                  "Topic :: Utilities"],
   keywords = 'scons svg s3 aws'
)
