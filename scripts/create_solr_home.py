#!/usr/bin/env python

import os
import argparse

from mbdata.search import create_solr_home

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', required=True)
args = parser.parse_args()

# TODO allow custom core name
# TODO allow creating just a core in an existing Solr home

create_solr_home(args.directory)
print(open(os.path.join(args.directory, 'README.txt')).read())

