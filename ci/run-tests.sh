#!/usr/bin/env bash

set -ex

export PIP_CACHE_DIR=`pwd`/pip-cache

ls -l
tox --recreate
