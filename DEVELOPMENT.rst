#################
Development Guide
#################

Development Setup
=================

Run build environment in Docker (optional):

    docker build -t mbdata-dev -f Dockerfile.dev .
    docker run -ti --rm -v $PWD:/mbdata mbdata-dev

Clone the repository and setup virtualenv::

    git clone git@github.com:lalinsky/mbdata.git
    cd mbdata/
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python setup.py develop

Updating SQL files and models
=============================

Run these scripts to update SQL files and rebuild SQLAlchemy models from them::

    ./scripts/update_sql.sh
    ./scripts/update_models.sh

Release a new version
=====================

1. Change the version number in ``mbdata/__init__.py``.

2. Add notes to ``CHANGELOG.rst``

3. Tag the repository::

    git tag -s vX.Y.Z

4. Upload the package to PyPI::

    rm -rf dist/
    python setup.py sdist
    twine upload dist/mbdata-*.tar.gz
