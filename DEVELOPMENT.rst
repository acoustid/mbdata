#################
Development Guide
#################

Updating SQL files and models
=============================

Run these scripts to update SQL files and rebuild SQLAlchemy models from them::

    ./scripts/update_sql.sh
    ./scripts/update_models.sh

Release a new version
=====================

1. Change the version number in ``mbdata/__init__.py``.
2. Add notes to ``CHANGELOG.rst``
3. Upload to PyPI::
    rm -rf dist/
    python setup.py sdist
    twine upload dist/mbdata-*.tar.gz
