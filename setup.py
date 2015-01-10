#!/usr/bin/env python

from setuptools import setup

setup(name='mbdata',
      version='2015.01.10',
      description='MusicBrainz Database Tools',
      author='Lukas Lalinsky',
      author_email='lukas@oxygene.sk',
      url='https://bitbucket.org/lalinsky/mbdata',
      license='MIT',
      platforms='ALL',

      include_package_data=True,
      zip_safe=False,

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
      ],
)
