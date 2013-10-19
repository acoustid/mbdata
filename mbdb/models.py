# Automatically generated, do not edit

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DateTime, Date, Enum, Interval, Float, CHAR
from sqlalchemy.dialects.postgres import ARRAY, UUID, SMALLINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, composite
from sqlalchemy.ext.hybrid import hybrid_property
from mbdb.types import PartialDate

Base = declarative_base()


class Annotation(Base):
    __tablename__ = u'annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    text = Column(String)
    changelog = Column(String(255))
    created = Column(DateTime(timezone=True))

    editor = relationship(u'Editor', foreign_keys=[editor_id])


class Application(Base):
    __tablename__ = u'application'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    owner_id = Column(u'owner', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    name = Column(String, nullable=False)
    oauth_id = Column(String, nullable=False)
    oauth_secret = Column(String, nullable=False)
    oauth_redirect_uri = Column(String)

    owner = relationship(u'Editor', foreign_keys=[owner_id])


class AreaType(Base):
    __tablename__ = u'area_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Area(Base):
    __tablename__ = u'area'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    sort_name = Column(String, nullable=False)
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.area_type.id'))
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    ended = Column(Boolean, nullable=False)
    comment = Column(String(255), nullable=False)

    type = relationship(u'AreaType', foreign_keys=[type_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class AreaGIDRedirect(Base):
    __tablename__ = u'area_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Area', foreign_keys=[new_id_id])


class AreaAliasType(Base):
    __tablename__ = u'area_alias_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class AreaAlias(Base):
    __tablename__ = u'area_alias'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    name = Column(String, nullable=False)
    locale = Column(String)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.area_alias_type.id'))
    sort_name = Column(String, nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    primary_for_locale = Column(Boolean, nullable=False)
    ended = Column(Boolean, nullable=False)

    area = relationship(u'Area', foreign_keys=[area_id])
    type = relationship(u'AreaAliasType', foreign_keys=[type_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class AreaAnnotation(Base):
    __tablename__ = u'area_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    area = relationship(u'Area', foreign_keys=[area_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class Artist(Base):
    __tablename__ = u'artist'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    sort_name = Column(String, nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.artist_type.id'))
    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'))
    gender_id = Column(u'gender', Integer, ForeignKey(u'musicbrainz.gender.id'))
    comment = Column(String(255), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    ended = Column(Boolean, nullable=False)
    begin_area_id = Column(u'begin_area', Integer, ForeignKey(u'musicbrainz.area.id'))
    end_area_id = Column(u'end_area', Integer, ForeignKey(u'musicbrainz.area.id'))

    type = relationship(u'ArtistType', foreign_keys=[type_id])
    area = relationship(u'Area', foreign_keys=[area_id])
    gender = relationship(u'Gender', foreign_keys=[gender_id])
    begin_area = relationship(u'Area', foreign_keys=[begin_area_id])
    end_area = relationship(u'Area', foreign_keys=[end_area_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class ArtistDeletion(Base):
    __tablename__ = u'artist_deletion'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    last_known_name = Column(String, nullable=False)
    last_known_comment = Column(String, nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=False)


class ArtistAliasType(Base):
    __tablename__ = u'artist_alias_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class ArtistAlias(Base):
    __tablename__ = u'artist_alias'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    name = Column(String, nullable=False)
    locale = Column(String)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.artist_alias_type.id'))
    sort_name = Column(String, nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    primary_for_locale = Column(Boolean, nullable=False)
    ended = Column(Boolean, nullable=False)

    artist = relationship(u'Artist', foreign_keys=[artist_id])
    type = relationship(u'ArtistAliasType', foreign_keys=[type_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class ArtistAnnotation(Base):
    __tablename__ = u'artist_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    artist = relationship(u'Artist', foreign_keys=[artist_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class ArtistIPI(Base):
    __tablename__ = u'artist_ipi'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    ipi = Column(CHAR(11), primary_key=True, nullable=False)
    edits_pending = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True))

    artist = relationship(u'Artist', foreign_keys=[artist_id])


class ArtistISNI(Base):
    __tablename__ = u'artist_isni'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    isni = Column(CHAR(16), primary_key=True, nullable=False)
    edits_pending = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True))

    artist = relationship(u'Artist', foreign_keys=[artist_id])


class ArtistMeta(Base):
    __tablename__ = u'artist_meta'
    __table_args__ = { "schema" : "musicbrainz" }

    id_id = Column(u'id', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT)
    rating_count = Column(Integer)

    id = relationship(u'Artist', foreign_keys=[id_id])


class ArtistTag(Base):
    __tablename__ = u'artist_tag'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    artist = relationship(u'Artist', foreign_keys=[artist_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class ArtistRatingRaw(Base):
    __tablename__ = u'artist_rating_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT, nullable=False)

    artist = relationship(u'Artist', foreign_keys=[artist_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])


class ArtistTagRaw(Base):
    __tablename__ = u'artist_tag_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)

    artist = relationship(u'Artist', foreign_keys=[artist_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class ArtistCredit(Base):
    __tablename__ = u'artist_credit'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    artist_count = Column(SMALLINT, nullable=False)
    ref_count = Column(Integer)
    created = Column(DateTime(timezone=True))


class ArtistCreditName(Base):
    __tablename__ = u'artist_credit_name'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_credit_id = Column(u'artist_credit', Integer, ForeignKey(u'musicbrainz.artist_credit.id'), primary_key=True, nullable=False)
    position = Column(SMALLINT, primary_key=True, nullable=False)
    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    name = Column(String, nullable=False)
    join_phrase = Column(String, nullable=False)

    artist_credit = relationship(u'ArtistCredit', foreign_keys=[artist_credit_id])
    artist = relationship(u'Artist', foreign_keys=[artist_id])


class ArtistGIDRedirect(Base):
    __tablename__ = u'artist_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Artist', foreign_keys=[new_id_id])


class ArtistType(Base):
    __tablename__ = u'artist_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class AutoeditorElection(Base):
    __tablename__ = u'autoeditor_election'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    candidate_id = Column(u'candidate', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    proposer_id = Column(u'proposer', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    seconder_1_id = Column(u'seconder_1', Integer, ForeignKey(u'musicbrainz.editor.id'))
    seconder_2_id = Column(u'seconder_2', Integer, ForeignKey(u'musicbrainz.editor.id'))
    status = Column(Integer, nullable=False)
    yes_votes = Column(Integer, nullable=False)
    no_votes = Column(Integer, nullable=False)
    propose_time = Column(DateTime(timezone=True), nullable=False)
    open_time = Column(DateTime(timezone=True))
    close_time = Column(DateTime(timezone=True))

    candidate = relationship(u'Editor', foreign_keys=[candidate_id])
    proposer = relationship(u'Editor', foreign_keys=[proposer_id])
    seconder_1 = relationship(u'Editor', foreign_keys=[seconder_1_id])
    seconder_2 = relationship(u'Editor', foreign_keys=[seconder_2_id])


class AutoeditorElectionVote(Base):
    __tablename__ = u'autoeditor_election_vote'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    autoeditor_election_id = Column(u'autoeditor_election', Integer, ForeignKey(u'musicbrainz.autoeditor_election.id'), nullable=False)
    voter_id = Column(u'voter', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    vote = Column(Integer, nullable=False)
    vote_time = Column(DateTime(timezone=True), nullable=False)

    autoeditor_election = relationship(u'AutoeditorElection', foreign_keys=[autoeditor_election_id])
    voter = relationship(u'Editor', foreign_keys=[voter_id])


class CDTOC(Base):
    __tablename__ = u'cdtoc'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    discid = Column(CHAR(28), nullable=False)
    freedb_id = Column(CHAR(8), nullable=False)
    track_count = Column(Integer, nullable=False)
    leadout_offset = Column(Integer, nullable=False)
    track_offset = Column(Integer, nullable=False)
    degraded = Column(Boolean, nullable=False)
    created = Column(DateTime(timezone=True))


class CDTOCRaw(Base):
    __tablename__ = u'cdtoc_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release_raw.id'), nullable=False)
    discid = Column(CHAR(28), nullable=False)
    track_count = Column(Integer, nullable=False)
    leadout_offset = Column(Integer, nullable=False)
    track_offset = Column(Integer, nullable=False)

    release = relationship(u'ReleaseRaw', foreign_keys=[release_id])


class CountryArea(Base):
    __tablename__ = u'country_area'
    __table_args__ = { "schema" : "musicbrainz" }

    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'), primary_key=True)

    area = relationship(u'Area', foreign_keys=[area_id])


class Edit(Base):
    __tablename__ = u'edit'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    type = Column(SMALLINT, nullable=False)
    status = Column(SMALLINT, nullable=False)
    data = Column(String, nullable=False)
    yes_votes = Column(Integer, nullable=False)
    no_votes = Column(Integer, nullable=False)
    autoedit = Column(SMALLINT, nullable=False)
    open_time = Column(DateTime(timezone=True))
    close_time = Column(DateTime(timezone=True))
    expire_time = Column(DateTime(timezone=True), nullable=False)
    language = Column(Integer, ForeignKey(u'musicbrainz.language'))
    quality = Column(SMALLINT, nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])


class EditNote(Base):
    __tablename__ = u'edit_note'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), nullable=False)
    text = Column(String, nullable=False)
    post_time = Column(DateTime(timezone=True))

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    edit = relationship(u'Edit', foreign_keys=[edit_id])


class EditArea(Base):
    __tablename__ = u'edit_area'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'), primary_key=True, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    area = relationship(u'Area', foreign_keys=[area_id])


class EditArtist(Base):
    __tablename__ = u'edit_artist'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    status = Column(SMALLINT, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    artist = relationship(u'Artist', foreign_keys=[artist_id])


class EditLabel(Base):
    __tablename__ = u'edit_label'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    status = Column(SMALLINT, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    label = relationship(u'Label', foreign_keys=[label_id])


class EditPlace(Base):
    __tablename__ = u'edit_place'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    place_id = Column(u'place', Integer, ForeignKey(u'musicbrainz.place.id'), primary_key=True, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    place = relationship(u'Place', foreign_keys=[place_id])


class EditRelease(Base):
    __tablename__ = u'edit_release'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    release = relationship(u'Release', foreign_keys=[release_id])


class EditReleaseGroup(Base):
    __tablename__ = u'edit_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    release_group_id = Column(u'release_group', Integer, ForeignKey(u'musicbrainz.release_group.id'), primary_key=True, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    release_group = relationship(u'ReleaseGroup', foreign_keys=[release_group_id])


class EditRecording(Base):
    __tablename__ = u'edit_recording'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    recording_id = Column(u'recording', Integer, ForeignKey(u'musicbrainz.recording.id'), primary_key=True, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    recording = relationship(u'Recording', foreign_keys=[recording_id])


class EditWork(Base):
    __tablename__ = u'edit_work'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), primary_key=True, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    work = relationship(u'Work', foreign_keys=[work_id])


class EditURL(Base):
    __tablename__ = u'edit_url'
    __table_args__ = { "schema" : "musicbrainz" }

    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), primary_key=True, nullable=False)
    url_id = Column(u'url', Integer, ForeignKey(u'musicbrainz.url.id'), primary_key=True, nullable=False)

    edit = relationship(u'Edit', foreign_keys=[edit_id])
    url = relationship(u'URL', foreign_keys=[url_id])


class Editor(Base):
    __tablename__ = u'editor'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    privs = Column(Integer)
    email = Column(String(64))
    website = Column(String(255))
    bio = Column(String)
    member_since = Column(DateTime(timezone=True))
    email_confirm_date = Column(DateTime(timezone=True))
    last_login_date = Column(DateTime(timezone=True))
    edits_accepted = Column(Integer)
    edits_rejected = Column(Integer)
    auto_edits_accepted = Column(Integer)
    edits_failed = Column(Integer)
    last_updated = Column(DateTime(timezone=True))
    birth_date = Column(Date)
    gender_id = Column(u'gender', Integer, ForeignKey(u'musicbrainz.gender.id'))
    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'))
    password = Column(String(128), nullable=False)
    ha1 = Column(CHAR(32), nullable=False)
    deleted = Column(Boolean, nullable=False)

    gender = relationship(u'Gender', foreign_keys=[gender_id])
    area = relationship(u'Area', foreign_keys=[area_id])


class EditorLanguage(Base):
    __tablename__ = u'editor_language'
    __table_args__ = { "schema" : "musicbrainz" }

    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    language_id = Column(u'language', Integer, ForeignKey(u'musicbrainz.language.id'), primary_key=True, nullable=False)
    fluency = Column(Enum(u'basic', u'intermediate', u'advanced', u'native', name=u'FLUENCY'), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    language = relationship(u'Language', foreign_keys=[language_id])


class EditorPreference(Base):
    __tablename__ = u'editor_preference'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    name = Column(String(50), nullable=False)
    value = Column(String(100), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])


class EditorSubscribeArtist(Base):
    __tablename__ = u'editor_subscribe_artist'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    last_edit_sent_id = Column(u'last_edit_sent', Integer, ForeignKey(u'musicbrainz.edit.id'), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    artist = relationship(u'Artist', foreign_keys=[artist_id])
    last_edit_sent = relationship(u'Edit', foreign_keys=[last_edit_sent_id])


class EditorSubscribeArtistDeleted(Base):
    __tablename__ = u'editor_subscribe_artist_deleted'
    __table_args__ = { "schema" : "musicbrainz" }

    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    gid = Column(UUID, ForeignKey(u'musicbrainz.artist_deletion.gid'), primary_key=True, nullable=False)
    deleted_by_id = Column(u'deleted_by', Integer, ForeignKey(u'musicbrainz.edit.id'), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    deleted_by = relationship(u'Edit', foreign_keys=[deleted_by_id])


class EditorSubscribeCollection(Base):
    __tablename__ = u'editor_subscribe_collection'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    collection = Column(Integer, ForeignKey(u'musicbrainz.collection'), nullable=False)
    last_edit_sent = Column(Integer, ForeignKey(u'musicbrainz.edit'), nullable=False)
    available = Column(Boolean, nullable=False)
    last_seen_name = Column(String(255))

    editor = relationship(u'Editor', foreign_keys=[editor_id])


class EditorSubscribeLabel(Base):
    __tablename__ = u'editor_subscribe_label'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    last_edit_sent_id = Column(u'last_edit_sent', Integer, ForeignKey(u'musicbrainz.edit.id'), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    label = relationship(u'Label', foreign_keys=[label_id])
    last_edit_sent = relationship(u'Edit', foreign_keys=[last_edit_sent_id])


class EditorSubscribeLabelDeleted(Base):
    __tablename__ = u'editor_subscribe_label_deleted'
    __table_args__ = { "schema" : "musicbrainz" }

    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    gid = Column(UUID, ForeignKey(u'musicbrainz.label_deletion.gid'), primary_key=True, nullable=False)
    deleted_by_id = Column(u'deleted_by', Integer, ForeignKey(u'musicbrainz.edit.id'), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    deleted_by = relationship(u'Edit', foreign_keys=[deleted_by_id])


class EditorSubscribeEditor(Base):
    __tablename__ = u'editor_subscribe_editor'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    subscribed_editor_id = Column(u'subscribed_editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    last_edit_sent = Column(Integer, ForeignKey(u'musicbrainz.edit'), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    subscribed_editor = relationship(u'Editor', foreign_keys=[subscribed_editor_id])


class Gender(Base):
    __tablename__ = u'gender'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class ISO31661(Base):
    __tablename__ = u'iso_3166_1'
    __table_args__ = { "schema" : "musicbrainz" }

    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    code = Column(CHAR(2), primary_key=True)

    area = relationship(u'Area', foreign_keys=[area_id])


class ISO31662(Base):
    __tablename__ = u'iso_3166_2'
    __table_args__ = { "schema" : "musicbrainz" }

    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    code = Column(String(10), primary_key=True)

    area = relationship(u'Area', foreign_keys=[area_id])


class ISO31663(Base):
    __tablename__ = u'iso_3166_3'
    __table_args__ = { "schema" : "musicbrainz" }

    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    code = Column(CHAR(4), primary_key=True)

    area = relationship(u'Area', foreign_keys=[area_id])


class ISRC(Base):
    __tablename__ = u'isrc'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    recording_id = Column(u'recording', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    isrc = Column(CHAR(12), nullable=False)
    source = Column(SMALLINT)
    edits_pending = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True))

    recording = relationship(u'Recording', foreign_keys=[recording_id])


class ISWC(Base):
    __tablename__ = u'iswc'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True, nullable=False)
    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    iswc = Column(CHAR(15))
    source = Column(SMALLINT)
    edits_pending = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True), nullable=False)

    work = relationship(u'Work', foreign_keys=[work_id])


class LinkAreaArea(Base):
    __tablename__ = u'l_area_area'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'Area', foreign_keys=[entity1_id])

    @hybrid_property
    def area0(self):
        return self.entity0

    @hybrid_property
    def area0_id(self):
        return self.entity0_id

    @hybrid_property
    def area1(self):
        return self.entity1

    @hybrid_property
    def area1_id(self):
        return self.entity1_id


class LinkAreaArtist(Base):
    __tablename__ = u'l_area_artist'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'Artist', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def artist(self):
        return self.entity1

    @hybrid_property
    def artist_id(self):
        return self.entity1_id


class LinkAreaLabel(Base):
    __tablename__ = u'l_area_label'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'Label', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def label(self):
        return self.entity1

    @hybrid_property
    def label_id(self):
        return self.entity1_id


class LinkAreaPlace(Base):
    __tablename__ = u'l_area_place'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'Place', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def place(self):
        return self.entity1

    @hybrid_property
    def place_id(self):
        return self.entity1_id


class LinkAreaRecording(Base):
    __tablename__ = u'l_area_recording'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'Recording', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def recording(self):
        return self.entity1

    @hybrid_property
    def recording_id(self):
        return self.entity1_id


class LinkAreaRelease(Base):
    __tablename__ = u'l_area_release'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'Release', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def release(self):
        return self.entity1

    @hybrid_property
    def release_id(self):
        return self.entity1_id


class LinkAreaReleaseGroup(Base):
    __tablename__ = u'l_area_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'ReleaseGroup', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def release_group(self):
        return self.entity1

    @hybrid_property
    def release_group_id(self):
        return self.entity1_id


class LinkAreaURL(Base):
    __tablename__ = u'l_area_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def url(self):
        return self.entity1

    @hybrid_property
    def url_id(self):
        return self.entity1_id


class LinkAreaWork(Base):
    __tablename__ = u'l_area_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.area.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Area', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def area(self):
        return self.entity0

    @hybrid_property
    def area_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkArtistArtist(Base):
    __tablename__ = u'l_artist_artist'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'Artist', foreign_keys=[entity1_id])

    @hybrid_property
    def artist0(self):
        return self.entity0

    @hybrid_property
    def artist0_id(self):
        return self.entity0_id

    @hybrid_property
    def artist1(self):
        return self.entity1

    @hybrid_property
    def artist1_id(self):
        return self.entity1_id


class LinkArtistLabel(Base):
    __tablename__ = u'l_artist_label'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'Label', foreign_keys=[entity1_id])

    @hybrid_property
    def artist(self):
        return self.entity0

    @hybrid_property
    def artist_id(self):
        return self.entity0_id

    @hybrid_property
    def label(self):
        return self.entity1

    @hybrid_property
    def label_id(self):
        return self.entity1_id


class LinkArtistPlace(Base):
    __tablename__ = u'l_artist_place'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'Place', foreign_keys=[entity1_id])

    @hybrid_property
    def artist(self):
        return self.entity0

    @hybrid_property
    def artist_id(self):
        return self.entity0_id

    @hybrid_property
    def place(self):
        return self.entity1

    @hybrid_property
    def place_id(self):
        return self.entity1_id


class LinkArtistRecording(Base):
    __tablename__ = u'l_artist_recording'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'Recording', foreign_keys=[entity1_id])

    @hybrid_property
    def artist(self):
        return self.entity0

    @hybrid_property
    def artist_id(self):
        return self.entity0_id

    @hybrid_property
    def recording(self):
        return self.entity1

    @hybrid_property
    def recording_id(self):
        return self.entity1_id


class LinkArtistRelease(Base):
    __tablename__ = u'l_artist_release'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'Release', foreign_keys=[entity1_id])

    @hybrid_property
    def artist(self):
        return self.entity0

    @hybrid_property
    def artist_id(self):
        return self.entity0_id

    @hybrid_property
    def release(self):
        return self.entity1

    @hybrid_property
    def release_id(self):
        return self.entity1_id


class LinkArtistReleaseGroup(Base):
    __tablename__ = u'l_artist_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'ReleaseGroup', foreign_keys=[entity1_id])

    @hybrid_property
    def artist(self):
        return self.entity0

    @hybrid_property
    def artist_id(self):
        return self.entity0_id

    @hybrid_property
    def release_group(self):
        return self.entity1

    @hybrid_property
    def release_group_id(self):
        return self.entity1_id


class LinkArtistURL(Base):
    __tablename__ = u'l_artist_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def artist(self):
        return self.entity0

    @hybrid_property
    def artist_id(self):
        return self.entity0_id

    @hybrid_property
    def url(self):
        return self.entity1

    @hybrid_property
    def url_id(self):
        return self.entity1_id


class LinkArtistWork(Base):
    __tablename__ = u'l_artist_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.artist.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Artist', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def artist(self):
        return self.entity0

    @hybrid_property
    def artist_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkLabelLabel(Base):
    __tablename__ = u'l_label_label'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Label', foreign_keys=[entity0_id])
    entity1 = relationship(u'Label', foreign_keys=[entity1_id])

    @hybrid_property
    def label0(self):
        return self.entity0

    @hybrid_property
    def label0_id(self):
        return self.entity0_id

    @hybrid_property
    def label1(self):
        return self.entity1

    @hybrid_property
    def label1_id(self):
        return self.entity1_id


class LinkLabelPlace(Base):
    __tablename__ = u'l_label_place'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Label', foreign_keys=[entity0_id])
    entity1 = relationship(u'Place', foreign_keys=[entity1_id])

    @hybrid_property
    def label(self):
        return self.entity0

    @hybrid_property
    def label_id(self):
        return self.entity0_id

    @hybrid_property
    def place(self):
        return self.entity1

    @hybrid_property
    def place_id(self):
        return self.entity1_id


class LinkLabelRecording(Base):
    __tablename__ = u'l_label_recording'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Label', foreign_keys=[entity0_id])
    entity1 = relationship(u'Recording', foreign_keys=[entity1_id])

    @hybrid_property
    def label(self):
        return self.entity0

    @hybrid_property
    def label_id(self):
        return self.entity0_id

    @hybrid_property
    def recording(self):
        return self.entity1

    @hybrid_property
    def recording_id(self):
        return self.entity1_id


class LinkLabelRelease(Base):
    __tablename__ = u'l_label_release'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Label', foreign_keys=[entity0_id])
    entity1 = relationship(u'Release', foreign_keys=[entity1_id])

    @hybrid_property
    def label(self):
        return self.entity0

    @hybrid_property
    def label_id(self):
        return self.entity0_id

    @hybrid_property
    def release(self):
        return self.entity1

    @hybrid_property
    def release_id(self):
        return self.entity1_id


class LinkLabelReleaseGroup(Base):
    __tablename__ = u'l_label_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Label', foreign_keys=[entity0_id])
    entity1 = relationship(u'ReleaseGroup', foreign_keys=[entity1_id])

    @hybrid_property
    def label(self):
        return self.entity0

    @hybrid_property
    def label_id(self):
        return self.entity0_id

    @hybrid_property
    def release_group(self):
        return self.entity1

    @hybrid_property
    def release_group_id(self):
        return self.entity1_id


class LinkLabelURL(Base):
    __tablename__ = u'l_label_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Label', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def label(self):
        return self.entity0

    @hybrid_property
    def label_id(self):
        return self.entity0_id

    @hybrid_property
    def url(self):
        return self.entity1

    @hybrid_property
    def url_id(self):
        return self.entity1_id


class LinkLabelWork(Base):
    __tablename__ = u'l_label_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Label', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def label(self):
        return self.entity0

    @hybrid_property
    def label_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkPlacePlace(Base):
    __tablename__ = u'l_place_place'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Place', foreign_keys=[entity0_id])
    entity1 = relationship(u'Place', foreign_keys=[entity1_id])

    @hybrid_property
    def place0(self):
        return self.entity0

    @hybrid_property
    def place0_id(self):
        return self.entity0_id

    @hybrid_property
    def place1(self):
        return self.entity1

    @hybrid_property
    def place1_id(self):
        return self.entity1_id


class LinkPlaceRecording(Base):
    __tablename__ = u'l_place_recording'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Place', foreign_keys=[entity0_id])
    entity1 = relationship(u'Recording', foreign_keys=[entity1_id])

    @hybrid_property
    def place(self):
        return self.entity0

    @hybrid_property
    def place_id(self):
        return self.entity0_id

    @hybrid_property
    def recording(self):
        return self.entity1

    @hybrid_property
    def recording_id(self):
        return self.entity1_id


class LinkPlaceRelease(Base):
    __tablename__ = u'l_place_release'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Place', foreign_keys=[entity0_id])
    entity1 = relationship(u'Release', foreign_keys=[entity1_id])

    @hybrid_property
    def place(self):
        return self.entity0

    @hybrid_property
    def place_id(self):
        return self.entity0_id

    @hybrid_property
    def release(self):
        return self.entity1

    @hybrid_property
    def release_id(self):
        return self.entity1_id


class LinkPlaceReleaseGroup(Base):
    __tablename__ = u'l_place_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Place', foreign_keys=[entity0_id])
    entity1 = relationship(u'ReleaseGroup', foreign_keys=[entity1_id])

    @hybrid_property
    def place(self):
        return self.entity0

    @hybrid_property
    def place_id(self):
        return self.entity0_id

    @hybrid_property
    def release_group(self):
        return self.entity1

    @hybrid_property
    def release_group_id(self):
        return self.entity1_id


class LinkPlaceURL(Base):
    __tablename__ = u'l_place_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Place', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def place(self):
        return self.entity0

    @hybrid_property
    def place_id(self):
        return self.entity0_id

    @hybrid_property
    def url(self):
        return self.entity1

    @hybrid_property
    def url_id(self):
        return self.entity1_id


class LinkPlaceWork(Base):
    __tablename__ = u'l_place_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Place', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def place(self):
        return self.entity0

    @hybrid_property
    def place_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkRecordingRecording(Base):
    __tablename__ = u'l_recording_recording'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Recording', foreign_keys=[entity0_id])
    entity1 = relationship(u'Recording', foreign_keys=[entity1_id])

    @hybrid_property
    def recording0(self):
        return self.entity0

    @hybrid_property
    def recording0_id(self):
        return self.entity0_id

    @hybrid_property
    def recording1(self):
        return self.entity1

    @hybrid_property
    def recording1_id(self):
        return self.entity1_id


class LinkRecordingRelease(Base):
    __tablename__ = u'l_recording_release'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Recording', foreign_keys=[entity0_id])
    entity1 = relationship(u'Release', foreign_keys=[entity1_id])

    @hybrid_property
    def recording(self):
        return self.entity0

    @hybrid_property
    def recording_id(self):
        return self.entity0_id

    @hybrid_property
    def release(self):
        return self.entity1

    @hybrid_property
    def release_id(self):
        return self.entity1_id


class LinkRecordingReleaseGroup(Base):
    __tablename__ = u'l_recording_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Recording', foreign_keys=[entity0_id])
    entity1 = relationship(u'ReleaseGroup', foreign_keys=[entity1_id])

    @hybrid_property
    def recording(self):
        return self.entity0

    @hybrid_property
    def recording_id(self):
        return self.entity0_id

    @hybrid_property
    def release_group(self):
        return self.entity1

    @hybrid_property
    def release_group_id(self):
        return self.entity1_id


class LinkRecordingURL(Base):
    __tablename__ = u'l_recording_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Recording', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def recording(self):
        return self.entity0

    @hybrid_property
    def recording_id(self):
        return self.entity0_id

    @hybrid_property
    def url(self):
        return self.entity1

    @hybrid_property
    def url_id(self):
        return self.entity1_id


class LinkRecordingWork(Base):
    __tablename__ = u'l_recording_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Recording', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def recording(self):
        return self.entity0

    @hybrid_property
    def recording_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkReleaseRelease(Base):
    __tablename__ = u'l_release_release'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Release', foreign_keys=[entity0_id])
    entity1 = relationship(u'Release', foreign_keys=[entity1_id])

    @hybrid_property
    def release0(self):
        return self.entity0

    @hybrid_property
    def release0_id(self):
        return self.entity0_id

    @hybrid_property
    def release1(self):
        return self.entity1

    @hybrid_property
    def release1_id(self):
        return self.entity1_id


class LinkReleaseReleaseGroup(Base):
    __tablename__ = u'l_release_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Release', foreign_keys=[entity0_id])
    entity1 = relationship(u'ReleaseGroup', foreign_keys=[entity1_id])

    @hybrid_property
    def release(self):
        return self.entity0

    @hybrid_property
    def release_id(self):
        return self.entity0_id

    @hybrid_property
    def release_group(self):
        return self.entity1

    @hybrid_property
    def release_group_id(self):
        return self.entity1_id


class LinkReleaseURL(Base):
    __tablename__ = u'l_release_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Release', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def release(self):
        return self.entity0

    @hybrid_property
    def release_id(self):
        return self.entity0_id

    @hybrid_property
    def url(self):
        return self.entity1

    @hybrid_property
    def url_id(self):
        return self.entity1_id


class LinkReleaseWork(Base):
    __tablename__ = u'l_release_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Release', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def release(self):
        return self.entity0

    @hybrid_property
    def release_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkReleaseGroupReleaseGroup(Base):
    __tablename__ = u'l_release_group_release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'ReleaseGroup', foreign_keys=[entity0_id])
    entity1 = relationship(u'ReleaseGroup', foreign_keys=[entity1_id])

    @hybrid_property
    def release_group0(self):
        return self.entity0

    @hybrid_property
    def release_group0_id(self):
        return self.entity0_id

    @hybrid_property
    def release_group1(self):
        return self.entity1

    @hybrid_property
    def release_group1_id(self):
        return self.entity1_id


class LinkReleaseGroupURL(Base):
    __tablename__ = u'l_release_group_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'ReleaseGroup', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def release_group(self):
        return self.entity0

    @hybrid_property
    def release_group_id(self):
        return self.entity0_id

    @hybrid_property
    def url(self):
        return self.entity1

    @hybrid_property
    def url_id(self):
        return self.entity1_id


class LinkReleaseGroupWork(Base):
    __tablename__ = u'l_release_group_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'ReleaseGroup', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def release_group(self):
        return self.entity0

    @hybrid_property
    def release_group_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkURLURL(Base):
    __tablename__ = u'l_url_url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'URL', foreign_keys=[entity0_id])
    entity1 = relationship(u'URL', foreign_keys=[entity1_id])

    @hybrid_property
    def url0(self):
        return self.entity0

    @hybrid_property
    def url0_id(self):
        return self.entity0_id

    @hybrid_property
    def url1(self):
        return self.entity1

    @hybrid_property
    def url1_id(self):
        return self.entity1_id


class LinkURLWork(Base):
    __tablename__ = u'l_url_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'URL', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def url(self):
        return self.entity0

    @hybrid_property
    def url_id(self):
        return self.entity0_id

    @hybrid_property
    def work(self):
        return self.entity1

    @hybrid_property
    def work_id(self):
        return self.entity1_id


class LinkWorkWork(Base):
    __tablename__ = u'l_work_work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), nullable=False)
    entity0_id = Column(u'entity0', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    entity1_id = Column(u'entity1', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    entity0 = relationship(u'Work', foreign_keys=[entity0_id])
    entity1 = relationship(u'Work', foreign_keys=[entity1_id])

    @hybrid_property
    def work0(self):
        return self.entity0

    @hybrid_property
    def work0_id(self):
        return self.entity0_id

    @hybrid_property
    def work1(self):
        return self.entity1

    @hybrid_property
    def work1_id(self):
        return self.entity1_id


class Label(Base):
    __tablename__ = u'label'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    sort_name = Column(String, nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    label_code = Column(Integer)
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.label_type.id'))
    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'))
    comment = Column(String(255), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    ended = Column(Boolean, nullable=False)

    type = relationship(u'LabelType', foreign_keys=[type_id])
    area = relationship(u'Area', foreign_keys=[area_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class LabelDeletion(Base):
    __tablename__ = u'label_deletion'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    last_known_name = Column(String, nullable=False)
    last_known_comment = Column(String, nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=False)


class LabelRatingRaw(Base):
    __tablename__ = u'label_rating_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT, nullable=False)

    label = relationship(u'Label', foreign_keys=[label_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])


class LabelTagRaw(Base):
    __tablename__ = u'label_tag_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)

    label = relationship(u'Label', foreign_keys=[label_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class LabelAliasType(Base):
    __tablename__ = u'label_alias_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class LabelAlias(Base):
    __tablename__ = u'label_alias'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    name = Column(String, nullable=False)
    locale = Column(String)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.label_alias_type.id'))
    sort_name = Column(String, nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    primary_for_locale = Column(Boolean, nullable=False)
    ended = Column(Boolean, nullable=False)

    label = relationship(u'Label', foreign_keys=[label_id])
    type = relationship(u'LabelAliasType', foreign_keys=[type_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class LabelAnnotation(Base):
    __tablename__ = u'label_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    label = relationship(u'Label', foreign_keys=[label_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class LabelIPI(Base):
    __tablename__ = u'label_ipi'
    __table_args__ = { "schema" : "musicbrainz" }

    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    ipi = Column(CHAR(11), primary_key=True, nullable=False)
    edits_pending = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True))

    label = relationship(u'Label', foreign_keys=[label_id])


class LabelISNI(Base):
    __tablename__ = u'label_isni'
    __table_args__ = { "schema" : "musicbrainz" }

    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    isni = Column(CHAR(16), primary_key=True, nullable=False)
    edits_pending = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True))

    label = relationship(u'Label', foreign_keys=[label_id])


class LabelMeta(Base):
    __tablename__ = u'label_meta'
    __table_args__ = { "schema" : "musicbrainz" }

    id_id = Column(u'id', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT)
    rating_count = Column(Integer)

    id = relationship(u'Label', foreign_keys=[id_id])


class LabelGIDRedirect(Base):
    __tablename__ = u'label_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.label.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Label', foreign_keys=[new_id_id])


class LabelTag(Base):
    __tablename__ = u'label_tag'
    __table_args__ = { "schema" : "musicbrainz" }

    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    label = relationship(u'Label', foreign_keys=[label_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class LabelType(Base):
    __tablename__ = u'label_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Language(Base):
    __tablename__ = u'language'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    iso_code_2t = Column(CHAR(3))
    iso_code_2b = Column(CHAR(3))
    iso_code_1 = Column(CHAR(2))
    name = Column(String(100), nullable=False)
    frequency = Column(Integer, nullable=False)
    iso_code_3 = Column(CHAR(3))


class Link(Base):
    __tablename__ = u'link'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    link_type_id = Column(u'link_type', Integer, ForeignKey(u'musicbrainz.link_type.id'), nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    attribute_count = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True))
    ended = Column(Boolean, nullable=False)

    link_type = relationship(u'LinkType', foreign_keys=[link_type_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class LinkAttribute(Base):
    __tablename__ = u'link_attribute'
    __table_args__ = { "schema" : "musicbrainz" }

    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), primary_key=True, nullable=False)
    attribute_type_id = Column(u'attribute_type', Integer, ForeignKey(u'musicbrainz.link_attribute_type.id'), primary_key=True, nullable=False)
    created = Column(DateTime(timezone=True))

    link = relationship(u'Link', foreign_keys=[link_id])
    attribute_type = relationship(u'LinkAttributeType', foreign_keys=[attribute_type_id])


class LinkAttributeType(Base):
    __tablename__ = u'link_attribute_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    parent_id = Column(u'parent', Integer, ForeignKey(u'musicbrainz.link_attribute_type.id'))
    root_id = Column(u'root', Integer, ForeignKey(u'musicbrainz.link_attribute_type.id'), nullable=False)
    child_order = Column(Integer, nullable=False)
    gid = Column(UUID, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String)
    last_updated = Column(DateTime(timezone=True))

    parent = relationship(u'LinkAttributeType', foreign_keys=[parent_id])
    root = relationship(u'LinkAttributeType', foreign_keys=[root_id])


class LinkCreditableAttributeType(Base):
    __tablename__ = u'link_creditable_attribute_type'
    __table_args__ = { "schema" : "musicbrainz" }

    attribute_type_id = Column(u'attribute_type', Integer, ForeignKey(u'musicbrainz.link_attribute_type.id'), primary_key=True, nullable=False)

    attribute_type = relationship(u'LinkAttributeType', foreign_keys=[attribute_type_id])


class LinkAttributeCredit(Base):
    __tablename__ = u'link_attribute_credit'
    __table_args__ = { "schema" : "musicbrainz" }

    link_id = Column(u'link', Integer, ForeignKey(u'musicbrainz.link.id'), primary_key=True, nullable=False)
    attribute_type = Column(Integer, ForeignKey(u'musicbrainz.link_creditable_attribute_type.attribute_type'), primary_key=True, nullable=False)
    credited_as = Column(String, nullable=False)

    link = relationship(u'Link', foreign_keys=[link_id])


class LinkType(Base):
    __tablename__ = u'link_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    parent_id = Column(u'parent', Integer, ForeignKey(u'musicbrainz.link_type.id'))
    child_order = Column(Integer, nullable=False)
    gid = Column(UUID, nullable=False)
    entity_type0 = Column(String(50), nullable=False)
    entity_type1 = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String)
    link_phrase = Column(String(255), nullable=False)
    reverse_link_phrase = Column(String(255), nullable=False)
    long_link_phrase = Column(String(255), nullable=False)
    priority = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    is_deprecated = Column(Boolean, nullable=False)

    parent = relationship(u'LinkType', foreign_keys=[parent_id])


class LinkTypeAttributeType(Base):
    __tablename__ = u'link_type_attribute_type'
    __table_args__ = { "schema" : "musicbrainz" }

    link_type_id = Column(u'link_type', Integer, ForeignKey(u'musicbrainz.link_type.id'), primary_key=True, nullable=False)
    attribute_type_id = Column(u'attribute_type', Integer, ForeignKey(u'musicbrainz.link_attribute_type.id'), primary_key=True, nullable=False)
    min = Column(SMALLINT)
    max = Column(SMALLINT)
    last_updated = Column(DateTime(timezone=True))

    link_type = relationship(u'LinkType', foreign_keys=[link_type_id])
    attribute_type = relationship(u'LinkAttributeType', foreign_keys=[attribute_type_id])


class EditorCollection(Base):
    __tablename__ = u'editor_collection'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    name = Column(String, nullable=False)
    public = Column(Boolean, nullable=False)
    description = Column(String, nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])


class EditorCollectionRelease(Base):
    __tablename__ = u'editor_collection_release'
    __table_args__ = { "schema" : "musicbrainz" }

    collection_id = Column(u'collection', Integer, ForeignKey(u'musicbrainz.editor_collection.id'), primary_key=True, nullable=False)
    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)

    collection = relationship(u'EditorCollection', foreign_keys=[collection_id])
    release = relationship(u'Release', foreign_keys=[release_id])


class EditorOauthToken(Base):
    __tablename__ = u'editor_oauth_token'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    application_id = Column(u'application', Integer, ForeignKey(u'musicbrainz.application.id'), nullable=False)
    authorization_code = Column(String)
    refresh_token = Column(String)
    access_token = Column(String)
    mac_key = Column(String)
    mac_time_diff = Column(Integer)
    expire_time = Column(DateTime(timezone=True), nullable=False)
    scope = Column(Integer, nullable=False)
    granted = Column(DateTime(timezone=True), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    application = relationship(u'Application', foreign_keys=[application_id])


class EditorWatchPreferences(Base):
    __tablename__ = u'editor_watch_preferences'
    __table_args__ = { "schema" : "musicbrainz" }

    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    notify_via_email = Column(Boolean, nullable=False)
    notification_timeframe = Column(Interval, nullable=False)
    last_checked = Column(DateTime(timezone=True), nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])


class EditorWatchArtist(Base):
    __tablename__ = u'editor_watch_artist'
    __table_args__ = { "schema" : "musicbrainz" }

    artist_id = Column(u'artist', Integer, ForeignKey(u'musicbrainz.artist.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)

    artist = relationship(u'Artist', foreign_keys=[artist_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])


class EditorWatchReleaseGroupType(Base):
    __tablename__ = u'editor_watch_release_group_type'
    __table_args__ = { "schema" : "musicbrainz" }

    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    release_group_type_id = Column(u'release_group_type', Integer, ForeignKey(u'musicbrainz.release_group_primary_type.id'), primary_key=True, nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    release_group_type = relationship(u'ReleaseGroupPrimaryType', foreign_keys=[release_group_type_id])


class EditorWatchReleaseStatus(Base):
    __tablename__ = u'editor_watch_release_status'
    __table_args__ = { "schema" : "musicbrainz" }

    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    release_status_id = Column(u'release_status', Integer, ForeignKey(u'musicbrainz.release_status.id'), primary_key=True, nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    release_status = relationship(u'ReleaseStatus', foreign_keys=[release_status_id])


class Medium(Base):
    __tablename__ = u'medium'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    position = Column(Integer, nullable=False)
    format_id = Column(u'format', Integer, ForeignKey(u'musicbrainz.medium_format.id'))
    name = Column(String(255))
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    track_count = Column(Integer, nullable=False)

    release = relationship(u'Release', foreign_keys=[release_id])
    format = relationship(u'MediumFormat', foreign_keys=[format_id])


class MediumCDTOC(Base):
    __tablename__ = u'medium_cdtoc'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    medium_id = Column(u'medium', Integer, ForeignKey(u'musicbrainz.medium.id'), nullable=False)
    cdtoc_id = Column(u'cdtoc', Integer, ForeignKey(u'musicbrainz.cdtoc.id'), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    medium = relationship(u'Medium', foreign_keys=[medium_id])
    cdtoc = relationship(u'CDTOC', foreign_keys=[cdtoc_id])


class MediumFormat(Base):
    __tablename__ = u'medium_format'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    parent_id = Column(u'parent', Integer, ForeignKey(u'musicbrainz.medium_format.id'))
    child_order = Column(Integer, nullable=False)
    year = Column(SMALLINT)
    has_discids = Column(Boolean, nullable=False)

    parent = relationship(u'MediumFormat', foreign_keys=[parent_id])


class Place(Base):
    __tablename__ = u'place'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.place_type.id'))
    address = Column(String, nullable=False)
    area_id = Column(u'area', Integer, ForeignKey(u'musicbrainz.area.id'))
    coordinates = Column(ARRAY(Float))
    comment = Column(String(255), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    ended = Column(Boolean, nullable=False)

    type = relationship(u'PlaceType', foreign_keys=[type_id])
    area = relationship(u'Area', foreign_keys=[area_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class PlaceAlias(Base):
    __tablename__ = u'place_alias'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    place_id = Column(u'place', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    name = Column(String, nullable=False)
    locale = Column(String)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.place_alias_type.id'))
    sort_name = Column(String, nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    primary_for_locale = Column(Boolean, nullable=False)
    ended = Column(Boolean, nullable=False)

    place = relationship(u'Place', foreign_keys=[place_id])
    type = relationship(u'PlaceAliasType', foreign_keys=[type_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class PlaceAliasType(Base):
    __tablename__ = u'place_alias_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class PlaceAnnotation(Base):
    __tablename__ = u'place_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    place_id = Column(u'place', Integer, ForeignKey(u'musicbrainz.place.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    place = relationship(u'Place', foreign_keys=[place_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class PlaceGIDRedirect(Base):
    __tablename__ = u'place_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.place.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Place', foreign_keys=[new_id_id])


class PlaceTag(Base):
    __tablename__ = u'place_tag'
    __table_args__ = { "schema" : "musicbrainz" }

    place_id = Column(u'place', Integer, ForeignKey(u'musicbrainz.place.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    place = relationship(u'Place', foreign_keys=[place_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class PlaceTagRaw(Base):
    __tablename__ = u'place_tag_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    place_id = Column(u'place', Integer, ForeignKey(u'musicbrainz.place.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)

    place = relationship(u'Place', foreign_keys=[place_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class PlaceType(Base):
    __tablename__ = u'place_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class ReplicationControl(Base):
    __tablename__ = u'replication_control'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    current_schema_sequence = Column(Integer, nullable=False)
    current_replication_sequence = Column(Integer)
    last_replication_date = Column(DateTime(timezone=True))


class Recording(Base):
    __tablename__ = u'recording'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    artist_credit_id = Column(u'artist_credit', Integer, ForeignKey(u'musicbrainz.artist_credit.id'), nullable=False)
    length = Column(Integer)
    comment = Column(String(255), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    video = Column(Boolean, nullable=False)

    artist_credit = relationship(u'ArtistCredit', foreign_keys=[artist_credit_id])


class RecordingRatingRaw(Base):
    __tablename__ = u'recording_rating_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    recording_id = Column(u'recording', Integer, ForeignKey(u'musicbrainz.recording.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT, nullable=False)

    recording = relationship(u'Recording', foreign_keys=[recording_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])


class RecordingTagRaw(Base):
    __tablename__ = u'recording_tag_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    recording_id = Column(u'recording', Integer, ForeignKey(u'musicbrainz.recording.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)

    recording = relationship(u'Recording', foreign_keys=[recording_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class RecordingAnnotation(Base):
    __tablename__ = u'recording_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    recording_id = Column(u'recording', Integer, ForeignKey(u'musicbrainz.recording.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    recording = relationship(u'Recording', foreign_keys=[recording_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class RecordingMeta(Base):
    __tablename__ = u'recording_meta'
    __table_args__ = { "schema" : "musicbrainz" }

    id_id = Column(u'id', Integer, ForeignKey(u'musicbrainz.recording.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT)
    rating_count = Column(Integer)

    id = relationship(u'Recording', foreign_keys=[id_id])


class RecordingGIDRedirect(Base):
    __tablename__ = u'recording_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Recording', foreign_keys=[new_id_id])


class RecordingTag(Base):
    __tablename__ = u'recording_tag'
    __table_args__ = { "schema" : "musicbrainz" }

    recording_id = Column(u'recording', Integer, ForeignKey(u'musicbrainz.recording.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    recording = relationship(u'Recording', foreign_keys=[recording_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class Release(Base):
    __tablename__ = u'release'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    artist_credit_id = Column(u'artist_credit', Integer, ForeignKey(u'musicbrainz.artist_credit.id'), nullable=False)
    release_group_id = Column(u'release_group', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    status_id = Column(u'status', Integer, ForeignKey(u'musicbrainz.release_status.id'))
    packaging_id = Column(u'packaging', Integer, ForeignKey(u'musicbrainz.release_packaging.id'))
    language_id = Column(u'language', Integer, ForeignKey(u'musicbrainz.language.id'))
    script_id = Column(u'script', Integer, ForeignKey(u'musicbrainz.script.id'))
    barcode = Column(String(255))
    comment = Column(String(255), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    quality = Column(SMALLINT, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    artist_credit = relationship(u'ArtistCredit', foreign_keys=[artist_credit_id])
    release_group = relationship(u'ReleaseGroup', foreign_keys=[release_group_id])
    status = relationship(u'ReleaseStatus', foreign_keys=[status_id])
    packaging = relationship(u'ReleasePackaging', foreign_keys=[packaging_id])
    language = relationship(u'Language', foreign_keys=[language_id])
    script = relationship(u'Script', foreign_keys=[script_id])


class ReleaseCountry(Base):
    __tablename__ = u'release_country'
    __table_args__ = { "schema" : "musicbrainz" }

    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)
    country = Column(Integer, ForeignKey(u'musicbrainz.country_area.area'), primary_key=True, nullable=False)
    date_year = Column(SMALLINT)
    date_month = Column(SMALLINT)
    date_day = Column(SMALLINT)

    release = relationship(u'Release', foreign_keys=[release_id])

    date = composite(PartialDate, date_year, date_month, date_day)


class ReleaseUnknownCountry(Base):
    __tablename__ = u'release_unknown_country'
    __table_args__ = { "schema" : "musicbrainz" }

    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)
    date_year = Column(SMALLINT)
    date_month = Column(SMALLINT)
    date_day = Column(SMALLINT)

    release = relationship(u'Release', foreign_keys=[release_id])

    date = composite(PartialDate, date_year, date_month, date_day)


class ReleaseRaw(Base):
    __tablename__ = u'release_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    artist = Column(String(255))
    added = Column(DateTime(timezone=True))
    last_modified = Column(DateTime(timezone=True))
    lookup_count = Column(Integer)
    modify_count = Column(Integer)
    source = Column(Integer)
    barcode = Column(String(255))
    comment = Column(String(255), nullable=False)


class ReleaseTagRaw(Base):
    __tablename__ = u'release_tag_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)

    release = relationship(u'Release', foreign_keys=[release_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class ReleaseAnnotation(Base):
    __tablename__ = u'release_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    release = relationship(u'Release', foreign_keys=[release_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class ReleaseGIDRedirect(Base):
    __tablename__ = u'release_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Release', foreign_keys=[new_id_id])


class ReleaseMeta(Base):
    __tablename__ = u'release_meta'
    __table_args__ = { "schema" : "musicbrainz" }

    id_id = Column(u'id', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)
    date_added = Column(DateTime(timezone=True))
    info_url = Column(String(255))
    amazon_asin = Column(String(10))
    amazon_store = Column(String(20))
    cover_art_presence = Column(Enum(u'absent', u'present', u'darkened', name=u'COVER_ART_PRESENCE'), nullable=False)

    id = relationship(u'Release', foreign_keys=[id_id])


class ReleaseCoverart(Base):
    __tablename__ = u'release_coverart'
    __table_args__ = { "schema" : "musicbrainz" }

    id_id = Column(u'id', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    cover_art_url = Column(String(255))

    id = relationship(u'Release', foreign_keys=[id_id])


class ReleaseLabel(Base):
    __tablename__ = u'release_label'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), nullable=False)
    label_id = Column(u'label', Integer, ForeignKey(u'musicbrainz.label.id'))
    catalog_number = Column(String(255))
    last_updated = Column(DateTime(timezone=True))

    release = relationship(u'Release', foreign_keys=[release_id])
    label = relationship(u'Label', foreign_keys=[label_id])


class ReleasePackaging(Base):
    __tablename__ = u'release_packaging'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class ReleaseStatus(Base):
    __tablename__ = u'release_status'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class ReleaseTag(Base):
    __tablename__ = u'release_tag'
    __table_args__ = { "schema" : "musicbrainz" }

    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    release = relationship(u'Release', foreign_keys=[release_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class ReleaseGroup(Base):
    __tablename__ = u'release_group'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    artist_credit_id = Column(u'artist_credit', Integer, ForeignKey(u'musicbrainz.artist_credit.id'), nullable=False)
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.release_group_primary_type.id'))
    comment = Column(String(255), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    artist_credit = relationship(u'ArtistCredit', foreign_keys=[artist_credit_id])
    type = relationship(u'ReleaseGroupPrimaryType', foreign_keys=[type_id])


class ReleaseGroupRatingRaw(Base):
    __tablename__ = u'release_group_rating_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    release_group_id = Column(u'release_group', Integer, ForeignKey(u'musicbrainz.release_group.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT, nullable=False)

    release_group = relationship(u'ReleaseGroup', foreign_keys=[release_group_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])


class ReleaseGroupTagRaw(Base):
    __tablename__ = u'release_group_tag_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    release_group_id = Column(u'release_group', Integer, ForeignKey(u'musicbrainz.release_group.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)

    release_group = relationship(u'ReleaseGroup', foreign_keys=[release_group_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class ReleaseGroupAnnotation(Base):
    __tablename__ = u'release_group_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    release_group_id = Column(u'release_group', Integer, ForeignKey(u'musicbrainz.release_group.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    release_group = relationship(u'ReleaseGroup', foreign_keys=[release_group_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class ReleaseGroupGIDRedirect(Base):
    __tablename__ = u'release_group_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.release_group.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'ReleaseGroup', foreign_keys=[new_id_id])


class ReleaseGroupMeta(Base):
    __tablename__ = u'release_group_meta'
    __table_args__ = { "schema" : "musicbrainz" }

    id_id = Column(u'id', Integer, ForeignKey(u'musicbrainz.release_group.id'), primary_key=True, nullable=False)
    release_count = Column(Integer, nullable=False)
    first_release_date_year = Column(SMALLINT)
    first_release_date_month = Column(SMALLINT)
    first_release_date_day = Column(SMALLINT)
    rating = Column(SMALLINT)
    rating_count = Column(Integer)

    id = relationship(u'ReleaseGroup', foreign_keys=[id_id])

    first_release_date = composite(PartialDate, first_release_date_year, first_release_date_month, first_release_date_day)


class ReleaseGroupTag(Base):
    __tablename__ = u'release_group_tag'
    __table_args__ = { "schema" : "musicbrainz" }

    release_group_id = Column(u'release_group', Integer, ForeignKey(u'musicbrainz.release_group.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    release_group = relationship(u'ReleaseGroup', foreign_keys=[release_group_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class ReleaseGroupPrimaryType(Base):
    __tablename__ = u'release_group_primary_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class ReleaseGroupSecondaryType(Base):
    __tablename__ = u'release_group_secondary_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


class ReleaseGroupSecondaryTypeJoin(Base):
    __tablename__ = u'release_group_secondary_type_join'
    __table_args__ = { "schema" : "musicbrainz" }

    release_group = Column(Integer, ForeignKey(u'musicbrainz.release_group.id,'), primary_key=True, nullable=False)
    secondary_type_id = Column(u'secondary_type', Integer, ForeignKey(u'musicbrainz.release_group_secondary_type.id'), primary_key=True, nullable=False)
    created = Column(DateTime(timezone=True), nullable=False)

    secondary_type = relationship(u'ReleaseGroupSecondaryType', foreign_keys=[secondary_type_id])


class Script(Base):
    __tablename__ = u'script'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    iso_code = Column(CHAR(4), nullable=False)
    iso_number = Column(CHAR(3), nullable=False)
    name = Column(String(100), nullable=False)
    frequency = Column(Integer, nullable=False)


class ScriptLanguage(Base):
    __tablename__ = u'script_language'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    script_id = Column(u'script', Integer, ForeignKey(u'musicbrainz.script.id'), nullable=False)
    language_id = Column(u'language', Integer, ForeignKey(u'musicbrainz.language.id'), nullable=False)
    frequency = Column(Integer, nullable=False)

    script = relationship(u'Script', foreign_keys=[script_id])
    language = relationship(u'Language', foreign_keys=[language_id])


class Tag(Base):
    __tablename__ = u'tag'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    ref_count = Column(Integer, nullable=False)


class TagRelation(Base):
    __tablename__ = u'tag_relation'
    __table_args__ = { "schema" : "musicbrainz" }

    tag1_id = Column(u'tag1', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    tag2_id = Column(u'tag2', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    weight = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    tag1 = relationship(u'Tag', foreign_keys=[tag1_id])
    tag2 = relationship(u'Tag', foreign_keys=[tag2_id])


class Track(Base):
    __tablename__ = u'track'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    recording_id = Column(u'recording', Integer, ForeignKey(u'musicbrainz.recording.id'), nullable=False)
    medium_id = Column(u'medium', Integer, ForeignKey(u'musicbrainz.medium.id'), nullable=False)
    position = Column(Integer, nullable=False)
    number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    artist_credit_id = Column(u'artist_credit', Integer, ForeignKey(u'musicbrainz.artist_credit.id'), nullable=False)
    length = Column(Integer)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    recording = relationship(u'Recording', foreign_keys=[recording_id])
    medium = relationship(u'Medium', foreign_keys=[medium_id])
    artist_credit = relationship(u'ArtistCredit', foreign_keys=[artist_credit_id])


class TrackGIDRedirect(Base):
    __tablename__ = u'track_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.track.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Track', foreign_keys=[new_id_id])


class TrackRaw(Base):
    __tablename__ = u'track_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    release_id = Column(u'release', Integer, ForeignKey(u'musicbrainz.release_raw.id'), nullable=False)
    title = Column(String(255), nullable=False)
    artist = Column(String(255))
    sequence = Column(Integer, nullable=False)

    release = relationship(u'ReleaseRaw', foreign_keys=[release_id])


class MediumIndex(Base):
    __tablename__ = u'medium_index'
    __table_args__ = { "schema" : "musicbrainz" }

    medium_id = Column(u'medium', Integer, ForeignKey(u'musicbrainz.medium.id'), primary_key=True)
    toc = Column(String)

    medium = relationship(u'Medium', foreign_keys=[medium_id])


class URL(Base):
    __tablename__ = u'url'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    url = Column(String, nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))


class URLGIDRedirect(Base):
    __tablename__ = u'url_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.url.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'URL', foreign_keys=[new_id_id])


class Vote(Base):
    __tablename__ = u'vote'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), nullable=False)
    edit_id = Column(u'edit', Integer, ForeignKey(u'musicbrainz.edit.id'), nullable=False)
    vote = Column(SMALLINT, nullable=False)
    vote_time = Column(DateTime(timezone=True))
    superseded = Column(Boolean, nullable=False)

    editor = relationship(u'Editor', foreign_keys=[editor_id])
    edit = relationship(u'Edit', foreign_keys=[edit_id])


class Work(Base):
    __tablename__ = u'work'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    gid = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.work_type.id'))
    comment = Column(String(255), nullable=False)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    language_id = Column(u'language', Integer, ForeignKey(u'musicbrainz.language.id'))

    type = relationship(u'WorkType', foreign_keys=[type_id])
    language = relationship(u'Language', foreign_keys=[language_id])


class WorkRatingRaw(Base):
    __tablename__ = u'work_rating_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT, nullable=False)

    work = relationship(u'Work', foreign_keys=[work_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])


class WorkTagRaw(Base):
    __tablename__ = u'work_tag_raw'
    __table_args__ = { "schema" : "musicbrainz" }

    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), primary_key=True, nullable=False)
    editor_id = Column(u'editor', Integer, ForeignKey(u'musicbrainz.editor.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)

    work = relationship(u'Work', foreign_keys=[work_id])
    editor = relationship(u'Editor', foreign_keys=[editor_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class WorkAliasType(Base):
    __tablename__ = u'work_alias_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class WorkAlias(Base):
    __tablename__ = u'work_alias'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    name = Column(String, nullable=False)
    locale = Column(String)
    edits_pending = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))
    type_id = Column(u'type', Integer, ForeignKey(u'musicbrainz.work_alias_type.id'))
    sort_name = Column(String, nullable=False)
    begin_date_year = Column(SMALLINT)
    begin_date_month = Column(SMALLINT)
    begin_date_day = Column(SMALLINT)
    end_date_year = Column(SMALLINT)
    end_date_month = Column(SMALLINT)
    end_date_day = Column(SMALLINT)
    primary_for_locale = Column(Boolean, nullable=False)
    ended = Column(Boolean, nullable=False)

    work = relationship(u'Work', foreign_keys=[work_id])
    type = relationship(u'WorkAliasType', foreign_keys=[type_id])

    begin_date = composite(PartialDate, begin_date_year, begin_date_month, begin_date_day)
    end_date = composite(PartialDate, end_date_year, end_date_month, end_date_day)


class WorkAnnotation(Base):
    __tablename__ = u'work_annotation'
    __table_args__ = { "schema" : "musicbrainz" }

    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), primary_key=True, nullable=False)
    annotation_id = Column(u'annotation', Integer, ForeignKey(u'musicbrainz.annotation.id'), primary_key=True, nullable=False)

    work = relationship(u'Work', foreign_keys=[work_id])
    annotation = relationship(u'Annotation', foreign_keys=[annotation_id])


class WorkGIDRedirect(Base):
    __tablename__ = u'work_gid_redirect'
    __table_args__ = { "schema" : "musicbrainz" }

    gid = Column(UUID, primary_key=True, nullable=False)
    new_id_id = Column(u'new_id', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    created = Column(DateTime(timezone=True))

    new_id = relationship(u'Work', foreign_keys=[new_id_id])


class WorkMeta(Base):
    __tablename__ = u'work_meta'
    __table_args__ = { "schema" : "musicbrainz" }

    id_id = Column(u'id', Integer, ForeignKey(u'musicbrainz.work.id'), primary_key=True, nullable=False)
    rating = Column(SMALLINT)
    rating_count = Column(Integer)

    id = relationship(u'Work', foreign_keys=[id_id])


class WorkTag(Base):
    __tablename__ = u'work_tag'
    __table_args__ = { "schema" : "musicbrainz" }

    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), primary_key=True, nullable=False)
    tag_id = Column(u'tag', Integer, ForeignKey(u'musicbrainz.tag.id'), primary_key=True, nullable=False)
    count = Column(Integer, nullable=False)
    last_updated = Column(DateTime(timezone=True))

    work = relationship(u'Work', foreign_keys=[work_id])
    tag = relationship(u'Tag', foreign_keys=[tag_id])


class WorkType(Base):
    __tablename__ = u'work_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class WorkAttributeType(Base):
    __tablename__ = u'work_attribute_type'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    comment = Column(String(255), nullable=False)
    free_text = Column(Boolean, nullable=False)


class WorkAttributeTypeAllowedValue(Base):
    __tablename__ = u'work_attribute_type_allowed_value'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    work_attribute_type_id = Column(u'work_attribute_type', Integer, ForeignKey(u'musicbrainz.work_attribute_type.id'), nullable=False)
    value = Column(String)

    work_attribute_type = relationship(u'WorkAttributeType', foreign_keys=[work_attribute_type_id])


class WorkAttribute(Base):
    __tablename__ = u'work_attribute'
    __table_args__ = { "schema" : "musicbrainz" }

    id = Column(Integer, primary_key=True)
    work_id = Column(u'work', Integer, ForeignKey(u'musicbrainz.work.id'), nullable=False)
    work_attribute_type_id = Column(u'work_attribute_type', Integer, ForeignKey(u'musicbrainz.work_attribute_type.id'), nullable=False)
    work_attribute_type_allowed_value_id = Column(u'work_attribute_type_allowed_value', Integer, ForeignKey(u'musicbrainz.work_attribute_type_allowed_value.id'))
    work_attribute_text = Column(String)

    work = relationship(u'Work', foreign_keys=[work_id])
    work_attribute_type = relationship(u'WorkAttributeType', foreign_keys=[work_attribute_type_id])
    work_attribute_type_allowed_value = relationship(u'WorkAttributeTypeAllowedValue', foreign_keys=[work_attribute_type_allowed_value_id])


