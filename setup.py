#!/usr/bin/env python

from setuptools import setup

setup(name='mbdata',
      version='1.0',
      description='MusicBrainz Database Tools',
      author='Lukas Lalinsky',
      author_email='lukas@oxygene.sk',
      url='https://bitbucket.org/lalinsky/mbdata',
      packages=[
          'mbdata',
          'mbdata.api',
          'mbdata.tools',
          'mbdata.web',
      ],
     )
