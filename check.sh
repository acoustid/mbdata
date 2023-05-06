#!/usr/bin/env bash

set -eux

# poetry run isort --check mbslave/
# poetry run black --check mbslave/

poetry run flake8 mbslave
poetry run mypy -p mbslave.replication
poetry run pytest -v
