#!/usr/bin/env bash

python -m mbdb.tools.genmodels ../mbserver/admin/sql/CreateTables.sql >mbdb/models.py

