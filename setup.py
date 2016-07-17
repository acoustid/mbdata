#!/usr/bin/env python

from setuptools import setup

setup(name='mbdata',
      version='2016.07.17',
      description='MusicBrainz Database Tools',
      author='Lukas Lalinsky',
      author_email='lukas@oxygene.sk',
      url='https://bitbucket.org/lalinsky/mbdata',
      license='MIT',
      platforms='ALL',

      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'six',
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

      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
      ],
)
