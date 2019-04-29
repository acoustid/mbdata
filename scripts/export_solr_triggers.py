#!/usr/bin/env python

import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from mbdata.search import export_triggers


parser = argparse.ArgumentParser()
args = parser.parse_args()

engine = create_engine(settings.DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
db = Session()

export_triggers(db)

