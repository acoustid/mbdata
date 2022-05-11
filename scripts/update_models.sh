#!/usr/bin/env bash

python -m mbdata.tools.genmodels \
    mbdata/sql/CreateTypes.sql \
    mbdata/sql/CreateTables.sql \
    mbdata/sql/caa/CreateTables.sql \
    mbdata/sql/wikidocs/CreateTables.sql \
    mbdata/sql/documentation/CreateTables.sql \
    mbdata/sql/statistics/CreateTables.sql \
    >mbdata/models.py
