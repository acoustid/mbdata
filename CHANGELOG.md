Version 2016.07.17
==================

- Updated to MusicBrainz database schema 23.
- Python 3 support.

Version 2016.02.11
==================

- New function `mbdata.config.configure()` that makes sure that the models have not been imported yet.
- Support for schema re-mapping in `mbdata.config`.
- Enum types are now correctly assigned to the schema. Previously they were schema-less.
- New module `mbdata.sample_data` with a tiny sample of the MusicBrainz database useful for testing.

Version 2015.06.20
==================

- Added `mbdata.config` for configuring the SQLAlchemy base/metadata to be used in the models.

Version 2015.01.10
==================

- Initial release.
