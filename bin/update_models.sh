#!/usr/bin/env bash

python -m mbdata.tools.genmodels \
    ../mbslave/sql/CreateTables.sql \
    ../mbslave/sql/caa/CreateTables.sql \
    ../mbslave/sql/wikidocs/CreateTables.sql \
    ../mbslave/sql/documentation/CreateTables.sql \
    ../mbslave/sql/statistics/CreateTables.sql \
    >mbdata/models.py

