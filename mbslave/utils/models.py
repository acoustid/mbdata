from mbdata import models
from sqlalchemy import inspect
from sqlalchemy.orm.session import object_session


ENTITY_TYPES = {
    'artist': models.Artist,
    'label': models.Label,
    'place': models.Place,
    'release_group': models.ReleaseGroup,
    'release': models.Release,
    'url': models.URL,
    'work': models.Work,
}


def get_entity_type_model(type):
    return ENTITY_TYPES[type]


def get_link_model(entity0, entity1):
    names = sorted([entity0.__name__, entity1.__name__])
    assert all(hasattr(models, name) for name in names)
    return getattr(models, 'Link{0}{1}'.format(*names))


def get_link_target(link, source):
    model = inspect(link).mapper.class_
    source_model = inspect(source).mapper.class_

    if source_model != model.entity0.property.mapper.class_:
        return link.entity0

    if source_model != model.entity1.property.mapper.class_:
        return link.entity1

    if source.id != link.entity0_id:
        return link.entity0

    if source.id != link.entity1_id:
        return link.entity1


def query_links(obj, target_model):
    session = object_session(obj)
    model = get_link_model(inspect(obj).mapper.class_, target_model)
    query = session.query(model)

    if isinstance(obj, model.entity0.property.mapper.class_):
        query = query.filter_by(entity0=obj)

    if isinstance(obj, model.entity1.property.mapper.class_):
        query = query.filter_by(entity1=obj)

    return query

