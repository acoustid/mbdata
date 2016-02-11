import sys

# Override this if you want mbdata models to be based on your own base class
Base = None

# Override this if you want mbdata to create its own base class, but linked to your metadata object
metadata = None

# Override this if you want customize the schema names that mbdata uses
schemas = {}

_is_frozen = False
_unset = object()


def configure(base_class=_unset, metadata=_unset, schema=_unset, schemas=_unset):
    if _is_frozen:
        raise RuntimeError("mbdata.models was already imported, you can't configure it anymore")
    if base_class is not _unset:
        sys.modules[__name__].Base = base_class
    if metadata is not _unset:
        sys.modules[__name__].metadata = metadata
    if schemas is not _unset:
        sys.modules[__name__].schemas = schemas
    elif schema is not _unset:
        sys.modules[__name__].schemas = {
            'musicbrainz': schema,
            'cover_art_archive': schema,
            'wikidocs': schema,
            'statistics': schema,
            'documentation': schema,
        }


def freeze():
    global _is_frozen
    _is_frozen = True
