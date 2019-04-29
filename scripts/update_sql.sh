#!/bin/sh

cd $(dirname $0)/../mbdata

rm -rf sql

#rm -rf /tmp/mbserver-clone
#mkdir /tmp/mbserver-clone

#curl -L -o /tmp/mbserver-clone/master.tar.gz https://github.com/metabrainz/musicbrainz-server/archive/master.tar.gz 
tar -x -f /tmp/mbserver-clone/master.tar.gz --strip-components=2 --wildcards 'musicbrainz-server-master/admin/sql/*'
#rm -rf /tmp/mbserver-clone
