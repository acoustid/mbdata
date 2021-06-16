#!/usr/bin/env bash

set -ex

PYTHON_VERSION=$1

MAIN_ENV_NAME=$(echo $PYTHON_VERSION | sed s/\\.//)
FLAKE8_ENV_NAME=$MAIN_ENV_NAME-flake8

export PIP_CACHE_DIR=`pwd`/pip-cache

tox --recreate -e $MAIN_ENV_NAME,$FLAKE8_ENV_NAME
