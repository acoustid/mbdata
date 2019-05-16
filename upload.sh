#!/usr/bin/env bash

set -ex

rm -rf dist/
python setup.py sdist
twine upload dist/mbdata-*.tar.gz
