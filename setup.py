#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name='mbdata',
      version='25.0.0',
      description='MusicBrainz Database Tools',
      long_description=long_description,
      author='Lukas Lalinsky',
      author_email='lukas@oxygene.sk',
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

      packages=[
          'mbdata',
          'mbdata.api',
          'mbdata.api.blueprints',
          'mbdata.api.tests',
          'mbdata.tests',
          'mbdata.tools',
          'mbdata.utils',
      ],
      namespace_packages=['mbdata'],

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
