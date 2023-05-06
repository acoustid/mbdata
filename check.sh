#!/usr/bin/env bash

set -eux

# poetry run isort --check mbdata/
# poetry run black --check mbdata/

poetry run flake8 mbdata
poetry run pytest -v
