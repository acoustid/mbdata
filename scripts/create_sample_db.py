#!/usr/bin/env python

from __future__ import print_function
import os
import sys

import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import mbdata.config
mbdata.config.configure(schema=None)
mbdata.config.freeze()

from mbdata.sample_data import create_sample_data  # noqa: E402
from mbdata.models import Base  # noqa: E402


parser = argparse.ArgumentParser(add_help=True,
                                 description='Create a small sample database.')
parser.add_argument('file', help='path of the db-file')
parser.add_argument('--overwrite', '-o', action='store_true',
                    default=False, help='silently overwrite db-file')
args = parser.parse_args()

if os.path.isfile(args.file):
    if args.overwrite:
        os.remove(args.file)
    else:
        print("Error: Database file already exists. You may want to use the '-o' flag.", file=sys.stderr)
        sys.exit(1)

engine = create_engine('sqlite:///' + args.file)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
create_sample_data(session)
