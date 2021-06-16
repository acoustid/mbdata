#!/usr/bin/env bash

set -ex

PYTHON_VERSION=$1
ENV_NAME=$(echo $PYTHON_VERSION | sed s/\.//)

export PIP_CACHE_DIR=`pwd`/pip-cache

tox --recreate -e $ENV_NAME
