#!/usr/bin/env python

import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from solr import Solr

import settings
from mbdata.search import create_index


parser = argparse.ArgumentParser()
parser.add_argument('--sample', dest='sample', action='store_true')
parser.add_argument('--full', dest='sample', action='store_false')
args = parser.parse_args()

engine = create_engine(settings.DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
db = Session()

solr = Solr(settings.SOLR_URI)

create_index(db, solr, sample=args.sample)

