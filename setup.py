#!/usr/bin/env python

import io
import re
from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as file:
    long_description = file.read()

with io.open("mbdata/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(name='mbdata',
      version=version,
      description='MusicBrainz Database Tools',
      long_description=long_description,
      author='Lukas Lalinsky',
      author_email='lalinsky@gmail.com',
      url='https://github.com/lalinsky/mbdata',
      license='MIT',
      platforms='ALL',

      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'six',
          'contextlib2; python_version < "3.2"',
          'typing; python_version < "3"',
      ],
      extra_require={
          'mbslave': ['psycopg2'],
          'sqlalchemy': ['sqlalchemy'],
      },

      packages=find_packages(),

      entry_points={
          'console_scripts': [
              'mbslave=mbdata.replication:main',
          ],
      },

      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
      ],
)
