from __future__ import print_function
import os
import re
import sys
import itertools
import tempfile
import six
from six import StringIO
from lxml import etree as ET
from lxml.builder import E
from sqlalchemy import sql, Column, Integer, String, MetaData
from sqlalchemy.orm import Load, relationship
from sqlalchemy.orm.properties import RelationshipProperty, ColumnProperty
from sqlalchemy.orm.interfaces import ONETOMANY, MANYTOONE
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

from mbdata.models import Area, Artist, Label, Recording, Release, ReleaseGroup, Work, Place


BATCH_SIZE = 10000
UPDATE_BATCH_SIZE = 1000
SAMPLE_SIZE = 2


metadata = MetaData(schema='mbdata')
Base = declarative_base(metadata=metadata)  # type: Any


class SearchQueue(Base):
    __tablename__ = 'search_queue'
    seq = Column(Integer, primary_key=True)
    kind = Column(String, nullable=False)
    id = Column(Integer, nullable=False)


class Schema(object):

    def __init__(self, entities):
        self.entities = entities
        self.entities_by_id = dict((e.name, e) for e in entities)

    def __getitem__(self, name):
        return self.entities_by_id[name]


class Entity(object):

    def __init__(self, name, model, fields):
        self.name = name
        self.model = model
        self.fields = fields
        for field in self.fields:
            field.bind(self)


class Field(object):

    def __init__(self, name, key, type='text'):
        self.name = name
        self.key = key
        self.type = type

    def bind(self, entity):
        self.entity = entity


class CustomArea(Area):
    redirect_gids = relationship("AreaGIDRedirect")
    aliases = relationship("AreaAlias")


class CustomPlace(Place):
    redirect_gids = relationship("PlaceGIDRedirect")
    aliases = relationship("PlaceAlias")


class CustomArtist(Artist):
    redirect_gids = relationship("ArtistGIDRedirect")
    aliases = relationship("ArtistAlias")


class CustomLabel(Label):
    redirect_gids = relationship("LabelGIDRedirect")
    aliases = relationship("LabelAlias")


class CustomRecording(Recording):
    redirect_gids = relationship("RecordingGIDRedirect")
    tracks = relationship("Track")


class CustomRelease(Release):
    redirect_gids = relationship("ReleaseGIDRedirect")


class CustomReleaseGroup(ReleaseGroup):
    redirect_gids = relationship("ReleaseGroupGIDRedirect")
    releases = relationship("Release")


class CustomWork(Work):
    redirect_gids = relationship("WorkGIDRedirect")
    aliases = relationship("WorkAlias")
    artist_links = relationship("LinkArtistWork")


schema = Schema([
    Entity('area', CustomArea, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'type.name'),
        Field('code', 'iso_3166_1_codes.code'),
        Field('code', 'iso_3166_2_codes.code'),
        Field('code', 'iso_3166_3_codes.code'),
        Field('alias', 'aliases.name'),
    ]),
    Entity('place', CustomPlace, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'type.name'),
        Field('alias', 'aliases.name'),
    ]),
    Entity('artist', CustomArtist, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('sort_name', 'sort_name'),
        Field('gender', 'gender.name'),
        Field('type', 'type.name'),
        Field('area', 'area.name'),
        Field('ipi', 'ipis.ipi'),
        Field('isni', 'isnis.isni'),
        Field('alias', 'aliases.name'),
    ]),
    Entity('label', CustomLabel, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('code', 'label_code'),
        Field('type', 'type.name'),
        Field('area', 'area.name'),
        Field('ipi', 'ipis.ipi'),
        Field('isni', 'isnis.isni'),
        Field('alias', 'aliases.name'),
    ]),
    Entity('recording', CustomRecording, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('artist', 'artist_credit.name'),
        Field('artist', 'artist_credit.artists.artist.name'),
        Field('artist_mbid', 'artist_credit.artists.artist.gid', type='string'),
        Field('length', 'length'),
        Field('video', 'video'),
        Field('isrc', 'isrcs.isrc'),
        Field('alias', 'tracks.name'),
    ]),
    Entity('release', CustomRelease, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'release_group.type.name'),
        Field('status', 'status.name'),
        Field('packaging', 'packaging.name'),
        Field('artist', 'artist_credit.name'),
        Field('artist', 'artist_credit.artists.artist.name'),
        Field('artist_mbid', 'artist_credit.artists.artist.gid', type='string'),
        Field('barcode', 'barcode'),
        Field('catno', 'labels.catalog_number'),
        Field('label', 'labels.label.name'),
        Field('alias', 'release_group.name'),
        Field('country', 'country_dates.country.area.name'),
    ]),
    Entity('release_group', CustomReleaseGroup, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'type.name'),
        Field('type', 'secondary_types.secondary_type.name'),
        Field('artist', 'artist_credit.name'),
        Field('artist', 'artist_credit.artists.artist.name'),
        Field('artist_mbid', 'artist_credit.artists.artist.gid', type='string'),
        Field('alias', 'releases.name'),
    ]),
    Entity('work', CustomWork, [
        Field('mbid', 'gid', type='string'),
        Field('mbid', 'redirect_gids.gid', type='string'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'type.name'),
        Field('artist', 'artist_links.entity0.name'),
        Field('alias', 'aliases.name'),
        Field('iswc', 'iswcs.iswc'),
    ]),
])


def _is_field_multi(model, selector):
    if '.' in selector:
        attr, sub_selector = selector.split('.', 1)
    else:
        attr, sub_selector = selector, None

    prop = getattr(model, attr).property
    if isinstance(prop, RelationshipProperty):
        assert sub_selector is not None
        if prop.direction == ONETOMANY:
            return True
        if prop.direction == MANYTOONE:
            return _is_field_multi(prop.mapper.class_, sub_selector)
    else:
        assert sub_selector is None
        return False


def is_field_multi(field):
    return _is_field_multi(field.entity.model, field.key)


def get_field_value(obj, selector):
    if obj is None:
        return

    if '.' in selector:
        attr, sub_selector = selector.split('.', 1)
    else:
        attr, sub_selector = selector, None

    prop = getattr(obj.__class__, attr).property
    if isinstance(prop, RelationshipProperty):
        assert sub_selector is not None
        if prop.direction == ONETOMANY:
            for sub_obj in getattr(obj, attr):
                for value in get_field_value(sub_obj, sub_selector):
                    yield value
        if prop.direction == MANYTOONE:
            for value in get_field_value(getattr(obj, attr), sub_selector):
                yield value
    else:
        assert sub_selector is None
        yield getattr(obj, attr)


def to_set(value):
    if isinstance(value, set):
        return value
    return set([value])


def iter_data_entity(db, entity, condition=None, batches=True):
    query = db.query(entity.model)
    if condition is not None:
        query = query.filter(condition)

    for field in entity.fields:
        load = Load(entity.model)
        model = field.entity.model
        for attr in field.key.split('.'):
            prop = getattr(model, attr).property
            if isinstance(prop, RelationshipProperty):
                if prop.direction == ONETOMANY:
                    load = load.subqueryload(attr)
                elif prop.direction == MANYTOONE:
                    load = load.joinedload(attr)
                else:
                    load = load.defaultload(attr)
                model = prop.mapper.class_
        query = query.options(load)

    queries = []
    if batches:
        min_id = query.with_entities(sql.func.min(entity.model.id)).scalar()
        max_id = query.with_entities(sql.func.max(entity.model.id)).scalar()
        for i in range(min_id, max_id + 1, BATCH_SIZE):
            queries.append(query.filter(entity.model.id.between(i, i + BATCH_SIZE - 1)))
    else:
        queries.append(query)

    for query in queries:
        for item in query.order_by(entity.model.id):
            data = set([
                ('id', '{0}:{1}'.format(entity.name, item.id)),
                ('kind', entity.name),
            ])
            for field in entity.fields:
                for value in get_field_value(item, field.key):
                    if value is not None and value != '':
                        data.add((field.name, value))
            yield item.id, data


def iter_data_all(db, sample=False):
    for entity in schema.entities:
        stream = iter_data_entity(db, entity)
        if sample:
            stream = itertools.islice(stream, SAMPLE_SIZE)
        for id, data in stream:
            yield id, data


def export_docs(stream):
    for id, data in stream:
        try:
            yield id, E.doc(*[E.field(re.sub('[\x00-\x08\x0b\x0c\x0e-\x1f]', '', six.text_type(value)), name=name) for (name, value) in data])
        except ValueError:
            print(id, data)
            raise


def generate_trigger_func(kind, table, op, select):
    ddl = []
    ddl.append("CREATE OR REPLACE FUNCTION mbdata.tr_search_{kind}_{op}_{table}() RETURNS trigger AS $$")
    ddl.append("BEGIN")
    if ' ' not in select:
        ddl.append("    INSERT INTO mbdata.search_queue (kind, id) VALUES ('{kind}', {select});")
    else:
        ddl.append("    INSERT INTO mbdata.search_queue (kind, id) SELECT '{kind}', * FROM {select} AS tmp;")
    ddl.append("    RETURN {{var}};")
    ddl.append("END;")
    ddl.append("$$ LANGUAGE plpgsql;")

    var = 'OLD' if op == 'del' else 'NEW'
    return "\n".join(ddl).format(kind=kind, table=table, op=op, select=select).format(var=var)


def generate_trigger(kind, schema, table, op, when=None):
    ddl = []
    ddl.append("CREATE TRIGGER mbdata_tr_search_{kind}_{op}_{table}")
    if op == 'ins':
        ddl.append("    AFTER INSERT ON {schema}.{table} FOR EACH ROW")
    elif op == 'upd':
        ddl.append("    AFTER UPDATE ON {schema}.{table} FOR EACH ROW")
    elif op == 'del':
        ddl.append("    BEFORE DELETE ON {schema}.{table} FOR EACH ROW")
    if when:
        ddl.append("    WHEN ({cond})")
        cond = ' OR\n          '.join(when)
    else:
        cond = None
    ddl.append("    EXECUTE PROCEDURE mbdata.tr_search_{kind}_{op}_{table}();")

    return "\n".join(ddl).format(schema=schema, kind=kind, table=table, op=op, cond=cond)


def export_update_triggers(db):
    for entity in schema.entities:
        columns = {}
        selects = {}
        collections = {}

        for field in entity.fields:
            path = (field.entity.model.__mapper__,)
            selects[path] = '{id}'
            collections[path] = True
            for attr in field.key.split('.'):
                prop = path[-1].get_property(attr)
                if isinstance(prop, RelationshipProperty):
                    new_path = path + (prop.mapper,)
                    if prop.direction == ONETOMANY:
                        collections[new_path] = True
                        for column in prop.remote_side:
                            select = '(SELECT {column} FROM {schema}.{table} WHERE {primary_key} IN {{id}})'.format(
                                schema=column.table.schema,
                                table=column.table.name,
                                column=column.name,
                                primary_key=prop.mapper.primary_key[0].name)
                            selects[new_path] = selects[path].replace('{id}', select)
                    elif prop.direction == MANYTOONE:
                        for column in prop.local_columns:
                            select = '(SELECT {primary_key} FROM {schema}.{table} WHERE {column} IN {{id}})'.format(
                                schema=column.table.schema,
                                table=column.table.name,
                                column=column.name,
                                primary_key=path[-1].primary_key[0].name)
                            selects[new_path] = selects[path].replace('{id}', select)
                            columns.setdefault(path, {})[column] = True
                    path = new_path
                elif isinstance(prop, ColumnProperty):
                    for column in prop.columns:
                        columns.setdefault(path, {})[column] = True

        for path, select in selects.items():
            pk = path[-1].primary_key[0].name
            select = re.sub(r'\(SELECT (?P<col>\S+) FROM \S+ WHERE (?P<pk>{pk}) IN {{id}}\)'.format(pk=pk), r'{var}.\1', select)
            select = re.sub(r'\(SELECT (?P<col>\S+) FROM \S+ WHERE (?P=col) IN ', r'(', select)
            select = re.sub(r'\({id}\)', r'{id}', select)
            select = re.sub(r' IN {id}', r' = {id}', select)
            select = re.sub(r' IN {var}', r' = {var}', select)
            select = select.replace('{id}', '{{var}}.{0}'.format(pk))
            selects[path] = select

        for path in collections:
            table = path[-1].mapped_table
            yield generate_trigger_func(entity.name, table.name, 'ins', selects[path])
            yield generate_trigger(entity.name, table.schema, table.name, 'ins')
            yield generate_trigger_func(entity.name, table.name, 'del', selects[path])
            yield generate_trigger(entity.name, table.schema, table.name, 'del')

        # TODO use six.iteritems, is it a performance impact to simply use columns.items() instead?
        for path, cols in six.iteritems(columns):
            cols_conds = ['NEW.{col} IS DISTINCT FROM OLD.{col}'.format(col=col.name) for col in cols]
            table = path[-1].mapped_table
            yield generate_trigger_func(entity.name, table.name, 'upd', selects[path])
            yield generate_trigger(entity.name, table.schema, table.name, 'upd', cols_conds)


def export_triggers(db):
    print('\\set ON_ERROR_STOP')
    print()

    print('BEGIN;')
    print()

    print('CREATE SCHEMA mbdata;')
    print()

    print('CREATE TABLE mbdata.search_queue (seq SERIAL PRIMARY KEY, kind TEXT NOT NULL, id INTEGER NOT NULL);')
    print()

    for s in export_update_triggers(db):
        print(s)
        print()

    print('COMMIT;')


def iter_updates(db, kind, ids):
    entity = schema[kind]
    condition = entity.model.id.in_(ids)
    missing_ids = set(ids)
    stream = iter_data_entity(db, entity, condition, batches=False)
    for id, doc in export_docs(stream):
        missing_ids.remove(id)
        yield E.add(doc)
    if missing_ids:
        yield E.delete(*map(E.id, ['%s:%s' % (kind, id) for id in missing_ids]))


def iter_all(db, sample=False):
    for id, doc in export_docs(iter_data_all(db, sample=sample)):
        yield E.add(doc)


def save_update_xml(xml, stream):
    num_docs = 0
    xml.write('<update>\n')
    for elem in stream:
        xml.write(ET.tostring(elem))
        xml.write('\n')
        num_docs += 1
    xml.write('</update>\n')
    xml.flush()
    return num_docs


def update_index(db, solr):
    with db.begin_nested():
        items = {}
        for item in db.query(SearchQueue).limit(UPDATE_BATCH_SIZE):
            items.setdefault(item.kind, set()).add(item.id)
            db.delete(item)
        xml = StringIO()
        streams = []
        # TODO use six.iteritems, is it a performance impact to simply use columns.items() instead?
        for kind, ids in six.iteritems(items):
            streams.append(iter_updates(db, kind, ids))
        num_docs = save_update_xml(xml, itertools.chain.from_iterable(streams))
        if num_docs:
            solr._update(xml.getvalue())
            print('Updated {0} documents'.format(num_docs))
        solr.commit()


def create_index_xml(db, path, sample=False):
    stream = iter_all(db, sample=sample)
    with open(path, 'w') as xml:
        save_update_xml(xml, stream)


def create_index(db, solr, sample=False):
    stream = iter_all(db, sample=sample)
    total_num_docs = 0
    while True:
        xml = StringIO()
        num_docs = save_update_xml(xml, itertools.islice(stream, UPDATE_BATCH_SIZE))
        if not num_docs:
            break
        total_num_docs += num_docs
        solr._update(xml.getvalue())
        print('Indexed {0} documents'.format(total_num_docs))
        sys.stdout.flush()
    solr.commit()


def build_solrconfig_xml():
    return E.config(
        E.luceneMatchVersion('4.6'),
        E.dataDir('${solr.data.dir:}'),
        E.directoryFactory({
            'name': 'DirectoryFactory',
            'class': '${solr.directoryFactory:solr.NRTCachingDirectoryFactory}'}),
        E.requestDispatcher(
            E.requestParsers(
                enableRemoteStreaming='true',
                multipartUploadLimitInKB='2048'),
            handleSelect='false'),
        E.requestHandler({'name': '/select', 'class': 'solr.SearchHandler'}),
        E.requestHandler({'name': '/update', 'class': 'solr.UpdateRequestHandler'}),
    )


def build_schema_xml():
    field_types = {}
    field_multi = {}
    for entity in schema.entities:
        field_names = set()
        for field in entity.fields:
            if field.type not in ('string', 'text'):
                raise ValueError('unknown type {0}'.format(field.type))
            if field.name in field_types and field_types[field.name] != field.type:
                raise ValueError('inconsistent field types for {0}: {1} vs {2}'.format(field.name, field_types[field.name], field.type))
            field_types[field.name] = field.type
            if field.name in field_names or is_field_multi(field):
                field_multi[field.name] = True

    field_elems = [
        E.field(name='id', type='string', indexed='true', stored='true', required='true'),
        E.field(name='kind', type='string', indexed='true', stored='true', required='true'),
    ]
    # TODO use six.iteritems, is it a performance impact to simply use columns.items() instead?
    for name, type in six.iteritems(field_types):
        elem = E.field(name=name, type=type, indexed='true', stored='false')
        if field_multi.get(name):
            elem.attrib['multiValued'] = 'true'
        field_elems.append(elem)

    return E.schema(
        {'name': 'musicbrainz', 'version': '1.1'},
        E.types(
            E.fieldType({
                'name': 'string', 'class': 'solr.StrField',
                'sortMissingLast': 'true', 'omitNorms': 'true'}),
            E.fieldType({
                'name': 'text', 'class': 'solr.TextField',
                'positionIncrementGap': '100'},
                E.analyzer({'type': 'index'},
                    E.tokenizer({'class': 'solr.StandardTokenizerFactory'}),
                    E.filter({'class': 'solr.LowerCaseFilterFactory'}),
                    E.filter({'class': 'solr.ASCIIFoldingFilterFactory'})),
                E.analyzer({'type': 'query'},
                    E.tokenizer({'class': 'solr.StandardTokenizerFactory'}),
                    E.filter({'class': 'solr.LowerCaseFilterFactory'}),
                    E.filter({'class': 'solr.ASCIIFoldingFilterFactory'})),
            ),
        ),
        E.fields(*field_elems),
        E.uniqueKey('id'),
        E.defaultSearchField('name'),
        E.solrQueryParser(defaultOperator='OR'),
    )


def build_solr_xml():
    return E.solr(
        E.cores(
            {'defaultCoreName': 'musicbrainz'},
            E.core({'name': 'musicbrainz', 'instanceDir': 'musicbrainz'}),
        )
    )


def xml_to_file(path, doc):
    with open(path, 'wb') as file:
        file.write(ET.tostring(doc, pretty_print=True, encoding='UTF-8', xml_declaration=True))


def create_solr_core(dir):
    conf_dir = os.path.join(dir, 'conf')
    data_dir = os.path.join(dir, 'data')
    os.makedirs(conf_dir)
    os.makedirs(data_dir)
    xml_to_file(os.path.join(conf_dir, 'schema.xml'), build_schema_xml())
    xml_to_file(os.path.join(conf_dir, 'solrconfig.xml'), build_solrconfig_xml())


def create_solr_home(dir):
    os.makedirs(dir)
    xml_to_file(os.path.join(dir, 'solr.xml'), build_solr_xml())
    with open(os.path.join(dir, 'README.txt'), 'w') as file:
        print('Start the Solr instance:', file=file)
        print('', file=file)
        print(' $ cd /path/to/solr-4.6.1/example/', file=file)
        print(' $ java -Dsolr.solr.home=%s -jar start.jar' % dir, file=file)
    create_solr_core(os.path.join(dir, 'musicbrainz'))


if __name__ == '__main__':
    from settings import DATABASE_URI

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(DATABASE_URI, echo=True)
    Session = sessionmaker(bind=engine)
    db = Session()

    # export_triggers(db)
    update_index(db, None)
    # stream = iter_data_all(db, sample=True)
    # for doc in export_docs(stream):
    #     print ET.tostring(doc, pretty_print=True)

