#!/usr/bin/env python

from setuptools import setup

setup(name='mbdata',
      version='1.0',
      description='MusicBrainz Database Tools',
      author='Lukas Lalinsky',
      author_email='lukas@oxygene.sk',
      url='https://bitbucket.org/lalinsky/mbdata',
      include_package_data=True,
      zip_safe=False,
      packages=[
          'mbdata',
          'mbdata.api',
          'mbdata.api.blueprints',
          'mbdata.tests',
          'mbdata.tests.api',
          'mbdata.tools',
          'mbdata.utils',
      ],
      namespace_packages=['mbdata'],
     )
