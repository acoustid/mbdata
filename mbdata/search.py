import itertools
from lxml import etree
from lxml.builder import E
from sqlalchemy import sql
from sqlalchemy.orm import Load, relationship
from sqlalchemy.orm.properties import RelationshipProperty
from sqlalchemy.orm.interfaces import ONETOMANY, MANYTOONE

from mbdata.models import Artist, Label, Recording, Release, ReleaseGroup, Work


BATCH_SIZE = 100
SAMPLE_SIZE = 2


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

    def __init__(self, name, key, model=None):
        self.name = name
        self.key = key
        self.model = model

    def bind(self, entity):
        self.entity = entity


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
    Entity('artist', CustomArtist, [
        Field('mbid', 'gid'),
        Field('mbid', 'redirect_gids.gid'),
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
        Field('mbid', 'gid'),
        Field('mbid', 'redirect_gids.gid'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('sort_name', 'sort_name'),
        Field('code', 'label_code'),
        Field('type', 'type.name'),
        Field('area', 'area.name'),
        Field('ipi', 'ipis.ipi'),
        Field('isni', 'isnis.isni'),
        Field('alias', 'aliases.name'),
    ]),
    Entity('recording', CustomRecording, [
        Field('mbid', 'gid'),
        Field('mbid', 'redirect_gids.gid'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('artist', 'artist_credit.name'),
        Field('artist', 'artist_credit.artists.artist.name'),
        Field('artist_mbid', 'artist_credit.artists.artist.gid'),
        Field('length', 'length'),
        Field('video', 'video'),
        Field('alias', 'tracks.name'),
    ]),
    Entity('release', CustomRelease, [
        Field('mbid', 'gid'),
        Field('mbid', 'redirect_gids.gid'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'release_group.type.name'),
        Field('status', 'status.name'),
        Field('packaging', 'packaging.name'),
        Field('artist', 'artist_credit.name'),
        Field('artist', 'artist_credit.artists.artist.name'),
        Field('artist_mbid', 'artist_credit.artists.artist.gid'),
        Field('barcode', 'barcode'),
        Field('catno', 'labels.catalog_number'),
        Field('label', 'labels.label.name'),
        Field('alias', 'release_group.name'),
    ]),
    Entity('release_group', CustomReleaseGroup, [
        Field('mbid', 'gid'),
        Field('mbid', 'redirect_gids.gid'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'type.name'),
        Field('type', 'secondary_types.secondary_type.name'),
        Field('artist', 'artist_credit.name'),
        Field('artist', 'artist_credit.artists.artist.name'),
        Field('artist_mbid', 'artist_credit.artists.artist.gid'),
        Field('alias', 'releases.name'),
    ]),
    Entity('work', CustomWork, [
        Field('mbid', 'gid'),
        Field('mbid', 'redirect_gids.gid'),
        Field('comment', 'comment'),
        Field('name', 'name'),
        Field('type', 'type.name'),
        Field('artist', 'artist_links.artist.name'),
        Field('alias', 'aliases.name'),
    ]),
])


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


def iter_data_entity(db, entity, condition=None):
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

    min_id = query.with_entities(sql.func.min(entity.model.id)).scalar()
    max_id = query.with_entities(sql.func.max(entity.model.id)).scalar()

    query = query.order_by(entity.model.id)

    for i in xrange(min_id, max_id + 1, BATCH_SIZE):
        sliced_query = query.filter(entity.model.id.between(i, i + BATCH_SIZE - 1))
        for item in sliced_query:
            data = set([
                ('id', '{0}:{1}'.format(entity.name, item.id)),
                ('kind', entity.name),
            ])
            for field in entity.fields:
                for value in get_field_value(item, field.key):
                    if value is not None and value != '':
                        data.add((field.name, value))
            yield data


def iter_data_all(db, sample=False):
    for entity in schema.entities:
        stream = iter_data_entity(db, entity)
        if sample:
            stream = itertools.islice(stream, SAMPLE_SIZE)
        for data in stream:
            yield data


def export_docs(stream):
    for data in stream:
        yield E.doc(*[E.field(unicode(value), name=name) for (name, value) in data])


if __name__ == '__main__':
    from settings import DATABASE_URI

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(DATABASE_URI, echo=True)
    Session = sessionmaker(bind=engine)
    db = Session()

    stream = iter_data_all(db, sample=True)
    for doc in export_docs(stream):
        print etree.tostring(doc, pretty_print=True)

