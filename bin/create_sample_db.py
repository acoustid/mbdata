#!/usr/bin/env python

import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import mbdata.config
mbdata.config.configure(schema=None)

from mbdata.sample_data import create_sample_data
from mbdata.models import ArtistCredit, Base


parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

engine = create_engine('sqlite:///' + args.file)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
create_sample_data(session)

