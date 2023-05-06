\set ON_ERROR_STOP 1
BEGIN;
CREATE INDEX release_idx_musicbrainz_collate ON release (name COLLATE musicbrainz.musicbrainz);
CREATE INDEX release_group_idx_musicbrainz_collate ON release_group (name COLLATE musicbrainz.musicbrainz);
CREATE INDEX artist_idx_musicbrainz_collate ON artist (name COLLATE musicbrainz.musicbrainz);
CREATE INDEX artist_credit_idx_musicbrainz_collate ON artist_credit (name COLLATE musicbrainz.musicbrainz);
CREATE INDEX artist_credit_name_idx_musicbrainz_collate ON artist_credit_name (name COLLATE musicbrainz.musicbrainz);
CREATE INDEX label_idx_musicbrainz_collate ON label (name COLLATE musicbrainz.musicbrainz);
CREATE INDEX recording_idx_musicbrainz_collate ON recording (name COLLATE musicbrainz.musicbrainz);
CREATE INDEX work_idx_musicbrainz_collate ON work (name COLLATE musicbrainz.musicbrainz);
COMMIT;
