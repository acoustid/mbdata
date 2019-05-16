#!/usr/bin/env bash

set -ex

export PIP_CACHE_DIR=`pwd`/pip-cache

perl -pi -e 's/(skip_missing_interpreters) = true/\1 = false/' tox.ini
tox --recreate
