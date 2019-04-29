\set ON_ERROR_STOP 1
BEGIN;
-- musicbrainz_collate indexes for unicode sorting
CREATE INDEX release_idx_musicbrainz_collate ON release (musicbrainz_collate(name));
CREATE INDEX release_group_idx_musicbrainz_collate ON release_group (musicbrainz_collate(name));
CREATE INDEX artist_idx_musicbrainz_collate ON artist (musicbrainz_collate(name));
CREATE INDEX artist_credit_idx_musicbrainz_collate ON artist_credit (musicbrainz_collate(name));
CREATE INDEX artist_credit_name_idx_musicbrainz_collate ON artist_credit_name (musicbrainz_collate(name));
CREATE INDEX label_idx_musicbrainz_collate ON label (musicbrainz_collate(name));
CREATE INDEX track_idx_musicbrainz_collate ON track (musicbrainz_collate(name));
CREATE INDEX recording_idx_musicbrainz_collate ON recording (musicbrainz_collate(name));
CREATE INDEX work_idx_musicbrainz_collate ON work (musicbrainz_collate(name));
COMMIT;
