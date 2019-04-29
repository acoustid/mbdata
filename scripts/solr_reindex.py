#!/usr/bin/env python

import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pysolr import Solr

import settings
from mbdata.search import create_index, create_index_xml


parser = argparse.ArgumentParser()
parser.add_argument('--dump')
parser.add_argument('--sample', dest='sample', action='store_true')
parser.add_argument('--full', dest='sample', action='store_false')
args = parser.parse_args()

engine = create_engine(settings.DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
db = Session()

if args.dump:
    create_index_xml(db, args.dump, sample=args.sample)
else:
    solr = Solr(settings.SOLR_URI)
    create_index(db, solr, sample=args.sample)

