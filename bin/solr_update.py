#!/usr/bin/env python

import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from solr import Solr

import settings
from mbdata.search import update_index


parser = argparse.ArgumentParser()
args = parser.parse_args()

engine = create_engine(settings.DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
db = Session()

solr = Solr(settings.SOLR_URI)
update_index(db, solr)

