#!/usr/bin/env python

import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mbdata.api.tests.sample_data import create_sample_data
from mbdata.models import ArtistCredit, Base
from mbdata.utils import patch_model_schemas, NO_SCHEMAS


parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

patch_model_schemas(NO_SCHEMAS)

engine = create_engine('sqlite:///' + args.file)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
create_sample_data(session)

