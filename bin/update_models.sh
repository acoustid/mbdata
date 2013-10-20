#!/usr/bin/env bash

python -m mbdata.tools.genmodels \
    ../mbserver/admin/sql/CreateTables.sql \
    ../mbserver/admin/sql/caa/CreateTables.sql \
    ../mbserver/admin/sql/wikidocs/CreateTables.sql \
    ../mbserver/admin/sql/documentation/CreateTables.sql \
    ../mbserver/admin/sql/statistics/CreateTables.sql \
    >mbdata/models.py

