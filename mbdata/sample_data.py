import datetime
from mbdata.models import Area, AreaType, Artist, ArtistCredit, ArtistCreditName
from mbdata.models import ArtistIPI, ArtistISNI, ArtistMeta, ArtistType, CountryArea
from mbdata.models import Gender, ISO31661, ISO31662, ISWC, Label
from mbdata.models import LabelIPI, LabelISNI, LabelMeta, LabelType, Language
from mbdata.models import Link, LinkAreaArea, LinkArtistRecording, LinkArtistRelease, LinkArtistWork
from mbdata.models import LinkRecordingWork, LinkReleaseURL, LinkType, LinkURLWork, Medium
from mbdata.models import MediumFormat, Place, PlaceType, Recording, RecordingMeta
from mbdata.models import Release, ReleaseCountry, ReleaseGroup, ReleaseGroupMeta, ReleaseGroupPrimaryType
from mbdata.models import ReleaseGroupSecondaryType, ReleaseGroupSecondaryTypeJoin, ReleaseLabel, ReleaseMeta, ReleasePackaging
from mbdata.models import ReleaseStatus, Script, Track, URL, Work
from mbdata.models import WorkMeta, WorkType


def create_sample_data(session):
    iso31661_1 = ISO31661()
    iso31661_1.code = u'DK'
    session.add(iso31661_1)

    areatype_country = AreaType()
    areatype_country.id = 1
    areatype_country.name = u'Country'
    areatype_country.child_order = 1
    areatype_country.description = u'Country is used for areas included (or previously included) in ISO 3166-1, e.g. United States.'
    areatype_country.gid = '06dd0ae4-8c74-30bb-b43d-95dcedf961de'
    session.add(areatype_country)

    area_denmark = Area()
    area_denmark.id = 57
    area_denmark.gid = '4757b525-2a60-324a-b060-578765d2c993'
    area_denmark.name = u'Denmark'
    area_denmark.edits_pending = 0
    area_denmark.last_updated = datetime.datetime(2013, 5, 27, 13, 28, 43, 191347)
    area_denmark.ended = False
    area_denmark.comment = u''
    area_denmark.iso_3166_1_codes = [
        iso31661_1,
    ]
    area_denmark.type = areatype_country
    session.add(area_denmark)

    areatype_city = AreaType()
    areatype_city.id = 3
    areatype_city.name = u'City'
    areatype_city.child_order = 3
    areatype_city.description = u'City is used for settlements of any size, including towns and villages.'
    areatype_city.gid = '6fd8f29a-3d0a-32fc-980d-ea697b69da78'
    session.add(areatype_city)

    area_vordingborg = Area()
    area_vordingborg.id = 106174
    area_vordingborg.gid = '4be4f4c6-60c3-46d4-a8d8-c8cb3537ff73'
    area_vordingborg.name = u'Vordingborg'
    area_vordingborg.edits_pending = 0
    area_vordingborg.last_updated = datetime.datetime(2015, 2, 1, 15, 51, 46, 784835)
    area_vordingborg.ended = False
    area_vordingborg.comment = u''
    area_vordingborg.type = areatype_city
    session.add(area_vordingborg)

    areatype_municipality = AreaType()
    areatype_municipality.id = 4
    areatype_municipality.name = u'Municipality'
    areatype_municipality.child_order = 4
    areatype_municipality.description = u'Municipality is used for small administrative divisions which, for urban municipalities, often contain a single city and a few surrounding villages. Rural municipalities typically group several villages together.'
    areatype_municipality.gid = '17246454-5ac4-36a1-b81a-4753eb2dab20'
    session.add(areatype_municipality)

    area_vordingborg_municipality = Area()
    area_vordingborg_municipality.id = 12847
    area_vordingborg_municipality.gid = 'ca8458e6-a8a2-4e46-a6a0-9aa6509499b1'
    area_vordingborg_municipality.name = u'Vordingborg Municipality'
    area_vordingborg_municipality.edits_pending = 0
    area_vordingborg_municipality.last_updated = datetime.datetime(2013, 11, 4, 18, 34, 16, 567633)
    area_vordingborg_municipality.ended = False
    area_vordingborg_municipality.comment = u''
    area_vordingborg_municipality.type = areatype_municipality
    session.add(area_vordingborg_municipality)

    iso31662_1 = ISO31662()
    iso31662_1.code = u'DK-85'
    session.add(iso31662_1)

    areatype_subdivision = AreaType()
    areatype_subdivision.id = 2
    areatype_subdivision.name = u'Subdivision'
    areatype_subdivision.child_order = 2
    areatype_subdivision.description = u'Subdivision is used for the main administrative divisions of a country, e.g. California, Ontario, Okinawa. These are considered when displaying the parent areas for a given area.'
    areatype_subdivision.gid = 'fd3d44c5-80a1-3842-9745-2c4972d35afa'
    session.add(areatype_subdivision)

    area_region_zealand = Area()
    area_region_zealand.id = 617
    area_region_zealand.gid = '7d490078-4542-411d-aece-709afee04256'
    area_region_zealand.name = u'Region Zealand'
    area_region_zealand.edits_pending = 0
    area_region_zealand.last_updated = datetime.datetime(2013, 10, 17, 21, 58, 27, 443512)
    area_region_zealand.begin_date_year = 2007
    area_region_zealand.begin_date_month = 1
    area_region_zealand.begin_date_day = 1
    area_region_zealand.ended = False
    area_region_zealand.comment = u''
    area_region_zealand.iso_3166_2_codes = [
        iso31662_1,
    ]
    area_region_zealand.type = areatype_subdivision
    session.add(area_region_zealand)

    linktype_part_of = LinkType()
    linktype_part_of.id = 356
    linktype_part_of.child_order = 0
    linktype_part_of.gid = 'de7cc874-8b1b-3a05-8272-f3834c968fb7'
    linktype_part_of.entity_type0 = u'area'
    linktype_part_of.entity_type1 = u'area'
    linktype_part_of.name = u'part of'
    linktype_part_of.description = u'Designates that one area is contained by another.'
    linktype_part_of.link_phrase = u'parts'
    linktype_part_of.reverse_link_phrase = u'part of'
    linktype_part_of.long_link_phrase = u'has part'
    linktype_part_of.priority = 0
    linktype_part_of.last_updated = datetime.datetime(2014, 11, 13, 1, 8, 49, 651356)
    linktype_part_of.is_deprecated = False
    linktype_part_of.has_dates = True
    linktype_part_of.entity0_cardinality = 1
    linktype_part_of.entity1_cardinality = 0
    session.add(linktype_part_of)

    link_1 = Link()
    link_1.id = 118734
    link_1.attribute_count = 0
    link_1.created = datetime.datetime(2013, 5, 17, 20, 5, 50, 534145)
    link_1.ended = False
    link_1.link_type = linktype_part_of
    session.add(link_1)

    linkareaarea_3 = LinkAreaArea()
    linkareaarea_3.id = 377
    linkareaarea_3.edits_pending = 0
    linkareaarea_3.last_updated = datetime.datetime(2013, 5, 19, 0, 59, 5, 652615)
    linkareaarea_3.link_order = 0
    linkareaarea_3.entity0_credit = u''
    linkareaarea_3.entity1_credit = u''
    linkareaarea_3.entity0 = area_denmark
    linkareaarea_3.entity1 = area_region_zealand
    linkareaarea_3.link = link_1
    session.add(linkareaarea_3)

    linkareaarea_2 = LinkAreaArea()
    linkareaarea_2.id = 12609
    linkareaarea_2.edits_pending = 0
    linkareaarea_2.last_updated = datetime.datetime(2013, 7, 16, 9, 24, 41, 4892)
    linkareaarea_2.link_order = 0
    linkareaarea_2.entity0_credit = u''
    linkareaarea_2.entity1_credit = u''
    linkareaarea_2.entity0 = area_region_zealand
    linkareaarea_2.entity1 = area_vordingborg_municipality
    linkareaarea_2.link = link_1
    session.add(linkareaarea_2)

    linkareaarea_1 = LinkAreaArea()
    linkareaarea_1.id = 105997
    linkareaarea_1.edits_pending = 0
    linkareaarea_1.last_updated = datetime.datetime(2015, 2, 1, 15, 51, 46, 784835)
    linkareaarea_1.link_order = 0
    linkareaarea_1.entity0_credit = u''
    linkareaarea_1.entity1_credit = u''
    linkareaarea_1.entity0 = area_vordingborg_municipality
    linkareaarea_1.entity1 = area_vordingborg
    linkareaarea_1.link = link_1
    session.add(linkareaarea_1)

    gender_male = Gender()
    gender_male.id = 1
    gender_male.name = u'Male'
    gender_male.child_order = 1
    gender_male.gid = '36d3d30a-839d-3eda-8cb3-29be4384e4a9'
    session.add(gender_male)

    artistipi_1 = ArtistIPI()
    artistipi_1.ipi = u'00054968649'
    artistipi_1.edits_pending = 0
    artistipi_1.created = datetime.datetime(2013, 10, 2, 16, 0, 12, 326623)
    session.add(artistipi_1)

    artistipi_2 = ArtistIPI()
    artistipi_2.ipi = u'00549686493'
    artistipi_2.edits_pending = 0
    artistipi_2.created = datetime.datetime(2014, 1, 18, 0, 0, 23, 82338)
    session.add(artistipi_2)

    artistisni_1 = ArtistISNI()
    artistisni_1.isni = u'0000000117742762'
    artistisni_1.edits_pending = 0
    artistisni_1.created = datetime.datetime(2013, 8, 4, 1, 48, 1, 946612)
    session.add(artistisni_1)

    artistmeta_1 = ArtistMeta()
    artistmeta_1.rating = 100
    artistmeta_1.rating_count = 1
    session.add(artistmeta_1)

    artisttype_person = ArtistType()
    artisttype_person.id = 1
    artisttype_person.name = u'Person'
    artisttype_person.child_order = 1
    artisttype_person.gid = 'b6e035f4-3ce9-331c-97df-83397230b0df'
    session.add(artisttype_person)

    artist_trentemoller = Artist()
    artist_trentemoller.id = 108703
    artist_trentemoller.gid = '95e9aba6-f85c-48a0-9ec9-395d4f0e3875'
    artist_trentemoller.name = u'Trentem\xf8ller'
    artist_trentemoller.sort_name = u'Trentem\xf8ller'
    artist_trentemoller.begin_date_year = 1972
    artist_trentemoller.begin_date_month = 10
    artist_trentemoller.begin_date_day = 16
    artist_trentemoller.comment = u''
    artist_trentemoller.edits_pending = 0
    artist_trentemoller.last_updated = datetime.datetime(2015, 10, 17, 9, 3, 54, 968064)
    artist_trentemoller.ended = False
    artist_trentemoller.area = area_denmark
    artist_trentemoller.begin_area = area_vordingborg
    artist_trentemoller.gender = gender_male
    artist_trentemoller.ipis = [
        artistipi_1,
        artistipi_2,
    ]
    artist_trentemoller.isnis = [
        artistisni_1,
    ]
    artist_trentemoller.meta = artistmeta_1
    artist_trentemoller.type = artisttype_person
    session.add(artist_trentemoller)

    artistcreditname_trentemoller = ArtistCreditName()
    artistcreditname_trentemoller.position = 0
    artistcreditname_trentemoller.name = u'Trentem\xf8ller'
    artistcreditname_trentemoller.join_phrase = u''
    artistcreditname_trentemoller.artist = artist_trentemoller
    session.add(artistcreditname_trentemoller)

    artistcredit_trentemoller = ArtistCredit()
    artistcredit_trentemoller.id = 108703
    artistcredit_trentemoller.name = u'Trentem\xf8ller'
    artistcredit_trentemoller.artist_count = 1
    artistcredit_trentemoller.ref_count = 995
    artistcredit_trentemoller.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_trentemoller.artists = [
        artistcreditname_trentemoller,
    ]
    session.add(artistcredit_trentemoller)

    iso31661_2 = ISO31661()
    iso31661_2.code = u'GB'
    session.add(iso31661_2)

    area_united_kingdom = Area()
    area_united_kingdom.id = 221
    area_united_kingdom.gid = '8a754a16-0027-3a29-b6d7-2b40ea0481ed'
    area_united_kingdom.name = u'United Kingdom'
    area_united_kingdom.edits_pending = 0
    area_united_kingdom.last_updated = datetime.datetime(2013, 5, 16, 11, 6, 19, 672350)
    area_united_kingdom.ended = False
    area_united_kingdom.comment = u''
    area_united_kingdom.iso_3166_1_codes = [
        iso31661_2,
    ]
    area_united_kingdom.type = areatype_country
    session.add(area_united_kingdom)

    countryarea_1 = CountryArea()
    countryarea_1.area = area_united_kingdom
    session.add(countryarea_1)

    releasecountry_1 = ReleaseCountry()
    releasecountry_1.date_year = 2007
    releasecountry_1.date_month = 3
    releasecountry_1.date_day = 23
    releasecountry_1.country = countryarea_1
    session.add(releasecountry_1)

    labelmeta_1 = LabelMeta()
    session.add(labelmeta_1)

    labeltype_original_production = LabelType()
    labeltype_original_production.id = 4
    labeltype_original_production.name = u'Original Production'
    labeltype_original_production.child_order = 0
    labeltype_original_production.gid = '7aaa37fe-2def-3476-b359-80245850062d'
    session.add(labeltype_original_production)

    labeltype_bootleg_production = LabelType()
    labeltype_bootleg_production.id = 5
    labeltype_bootleg_production.name = u'Bootleg Production'
    labeltype_bootleg_production.child_order = 0
    labeltype_bootleg_production.gid = 'fdac9b96-359b-3488-9322-ad99c2473636'
    session.add(labeltype_bootleg_production)

    labeltype_reissue_production = LabelType()
    labeltype_reissue_production.id = 6
    labeltype_reissue_production.name = u'Reissue Production'
    labeltype_reissue_production.child_order = 0
    labeltype_reissue_production.gid = '88ee6ae7-f413-3490-a1d2-54f6a9f0838c'
    session.add(labeltype_reissue_production)

    labeltype_production = LabelType()
    labeltype_production.id = 3
    labeltype_production.name = u'Production'
    labeltype_production.child_order = 0
    labeltype_production.gid = 'a2426aab-2dd4-339c-b47d-b4923a241678'
    labeltype_production.parent = [
        labeltype_original_production,
        labeltype_bootleg_production,
        labeltype_reissue_production,
    ]
    session.add(labeltype_production)

    label_king_biscuit_recordings = Label()
    label_king_biscuit_recordings.id = 9000
    label_king_biscuit_recordings.gid = 'aefbe2a5-76d6-4c99-a51d-f9214fe1018b'
    label_king_biscuit_recordings.name = u'King Biscuit Recordings'
    label_king_biscuit_recordings.comment = u''
    label_king_biscuit_recordings.edits_pending = 0
    label_king_biscuit_recordings.ended = False
    label_king_biscuit_recordings.area = area_united_kingdom
    label_king_biscuit_recordings.meta = labelmeta_1
    label_king_biscuit_recordings.type = labeltype_production
    session.add(label_king_biscuit_recordings)

    releaselabel_1 = ReleaseLabel()
    releaselabel_1.id = 213807
    releaselabel_1.catalog_number = u'KBCD109'
    releaselabel_1.last_updated = datetime.datetime(2011, 5, 16, 15, 59, 0, 785958)
    releaselabel_1.label = label_king_biscuit_recordings
    session.add(releaselabel_1)

    language_english = Language()
    language_english.id = 120
    language_english.iso_code_2t = u'eng'
    language_english.iso_code_2b = u'eng'
    language_english.iso_code_1 = u'en'
    language_english.name = u'English'
    language_english.frequency = 2
    language_english.iso_code_3 = u'eng'
    session.add(language_english)

    mediumformat_hdcd = MediumFormat()
    mediumformat_hdcd.id = 25
    mediumformat_hdcd.name = u'HDCD'
    mediumformat_hdcd.child_order = 0
    mediumformat_hdcd.has_discids = True
    mediumformat_hdcd.gid = '8759db4e-8451-33c0-8a8f-05e5f95f192e'
    session.add(mediumformat_hdcd)

    mediumformat_cd_r = MediumFormat()
    mediumformat_cd_r.id = 33
    mediumformat_cd_r.name = u'CD-R'
    mediumformat_cd_r.child_order = 1
    mediumformat_cd_r.has_discids = True
    mediumformat_cd_r.gid = '18805d5b-ff3a-3bc0-9b1f-188cc06415c8'
    session.add(mediumformat_cd_r)

    mediumformat_8cm_cd = MediumFormat()
    mediumformat_8cm_cd.id = 34
    mediumformat_8cm_cd.name = u'8cm CD'
    mediumformat_8cm_cd.child_order = 2
    mediumformat_8cm_cd.year = 1982
    mediumformat_8cm_cd.has_discids = True
    mediumformat_8cm_cd.gid = '86071488-c73d-31f9-be48-5795cb490c86'
    session.add(mediumformat_8cm_cd)

    mediumformat_blu_spec_cd = MediumFormat()
    mediumformat_blu_spec_cd.id = 35
    mediumformat_blu_spec_cd.name = u'Blu-spec CD'
    mediumformat_blu_spec_cd.child_order = 3
    mediumformat_blu_spec_cd.has_discids = True
    mediumformat_blu_spec_cd.gid = '038ec24e-5d01-3a8c-817e-c51a515b1875'
    session.add(mediumformat_blu_spec_cd)

    mediumformat_shm_cd = MediumFormat()
    mediumformat_shm_cd.id = 36
    mediumformat_shm_cd.name = u'SHM-CD'
    mediumformat_shm_cd.child_order = 4
    mediumformat_shm_cd.has_discids = True
    mediumformat_shm_cd.gid = '4856b1c6-674d-3f68-a1dd-8ae517e8b566'
    session.add(mediumformat_shm_cd)

    mediumformat_hqcd = MediumFormat()
    mediumformat_hqcd.id = 37
    mediumformat_hqcd.name = u'HQCD'
    mediumformat_hqcd.child_order = 5
    mediumformat_hqcd.has_discids = True
    mediumformat_hqcd.gid = 'fb8e91c7-16e3-3e29-98be-1dda0a473146'
    session.add(mediumformat_hqcd)

    mediumformat_8cm_cd_g = MediumFormat()
    mediumformat_8cm_cd_g.id = 40
    mediumformat_8cm_cd_g.name = u'8cm CD+G'
    mediumformat_8cm_cd_g.child_order = 0
    mediumformat_8cm_cd_g.has_discids = True
    mediumformat_8cm_cd_g.gid = '9f11c690-3b69-3585-9c40-1558d3ecb5ce'
    session.add(mediumformat_8cm_cd_g)

    mediumformat_cd_g = MediumFormat()
    mediumformat_cd_g.id = 39
    mediumformat_cd_g.name = u'CD+G'
    mediumformat_cd_g.child_order = 6
    mediumformat_cd_g.has_discids = True
    mediumformat_cd_g.gid = 'f59d2658-7fa7-377e-b2f1-fda418284d2c'
    mediumformat_cd_g.parent = [
        mediumformat_8cm_cd_g,
    ]
    session.add(mediumformat_cd_g)

    mediumformat_enhanced_cd = MediumFormat()
    mediumformat_enhanced_cd.id = 42
    mediumformat_enhanced_cd.name = u'Enhanced CD'
    mediumformat_enhanced_cd.child_order = 0
    mediumformat_enhanced_cd.has_discids = True
    mediumformat_enhanced_cd.gid = '8a08dc62-1aa2-34de-a904-fa467c53052c'
    session.add(mediumformat_enhanced_cd)

    mediumformat_data_cd = MediumFormat()
    mediumformat_data_cd.id = 43
    mediumformat_data_cd.name = u'Data CD'
    mediumformat_data_cd.child_order = 0
    mediumformat_data_cd.has_discids = False
    mediumformat_data_cd.gid = '37cceb6f-7ca2-321f-b2c5-12312a1a1df1'
    session.add(mediumformat_data_cd)

    mediumformat_dts_cd = MediumFormat()
    mediumformat_dts_cd.id = 44
    mediumformat_dts_cd.name = u'DTS CD'
    mediumformat_dts_cd.child_order = 0
    mediumformat_dts_cd.year = 1997
    mediumformat_dts_cd.has_discids = True
    mediumformat_dts_cd.gid = 'ccacd435-d33f-3104-98c9-cbe04d037c36'
    session.add(mediumformat_dts_cd)

    mediumformat_copy_control_cd = MediumFormat()
    mediumformat_copy_control_cd.id = 61
    mediumformat_copy_control_cd.name = u'Copy Control CD'
    mediumformat_copy_control_cd.child_order = 0
    mediumformat_copy_control_cd.has_discids = True
    mediumformat_copy_control_cd.description = u"Copy Control CD (CCCD) is an umbrella term for CDs released circa 2001-2006 containing software that is ostensibly designed to prevent the CD from being ripped. There are a number of software variants: the most well-known are Macrovision's Cactus Data Shield (CDS) and SunnComm's MediaMax."
    mediumformat_copy_control_cd.gid = '1a648190-5c75-3b74-b8c5-8150c97af0f5'
    session.add(mediumformat_copy_control_cd)

    mediumformat_cd = MediumFormat()
    mediumformat_cd.id = 1
    mediumformat_cd.name = u'CD'
    mediumformat_cd.child_order = 0
    mediumformat_cd.year = 1982
    mediumformat_cd.has_discids = True
    mediumformat_cd.gid = '9712d52a-4509-3d4b-a1a2-67c88c643e31'
    mediumformat_cd.parent = [
        mediumformat_hdcd,
        mediumformat_cd_r,
        mediumformat_8cm_cd,
        mediumformat_blu_spec_cd,
        mediumformat_shm_cd,
        mediumformat_hqcd,
        mediumformat_cd_g,
        mediumformat_enhanced_cd,
        mediumformat_data_cd,
        mediumformat_dts_cd,
        mediumformat_copy_control_cd,
    ]
    session.add(mediumformat_cd)

    recordingmeta_1 = RecordingMeta()
    session.add(recordingmeta_1)

    recording_small_piano_piece = Recording()
    recording_small_piano_piece.id = 7134047
    recording_small_piano_piece.gid = '77ef7468-e8f8-4447-9c7e-52b11272c6cc'
    recording_small_piano_piece.name = u'Small Piano Piece'
    recording_small_piano_piece.length = 176333
    recording_small_piano_piece.comment = u''
    recording_small_piano_piece.edits_pending = 0
    recording_small_piano_piece.video = False
    recording_small_piano_piece.artist_credit = artistcredit_trentemoller
    recording_small_piano_piece.meta = recordingmeta_1
    session.add(recording_small_piano_piece)

    track_small_piano_piece = Track()
    track_small_piano_piece.id = 5918611
    track_small_piano_piece.gid = 'b88995a5-a161-3f0b-80c9-dc94917b363a'
    track_small_piano_piece.position = 1
    track_small_piano_piece.number = u'1'
    track_small_piano_piece.name = u'Small Piano Piece'
    track_small_piano_piece.length = 176333
    track_small_piano_piece.edits_pending = 0
    track_small_piano_piece.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_small_piano_piece.is_data_track = False
    track_small_piano_piece.artist_credit = artistcredit_trentemoller
    track_small_piano_piece.recording = recording_small_piano_piece
    session.add(track_small_piano_piece)

    artistmeta_2 = ArtistMeta()
    session.add(artistmeta_2)

    artist_khan = Artist()
    artist_khan.id = 42684
    artist_khan.gid = 'a50084a5-7009-47a1-81b7-1bb18d09bda4'
    artist_khan.name = u'Khan'
    artist_khan.sort_name = u'Khan'
    artist_khan.comment = u'IDM artist Can Oral'
    artist_khan.edits_pending = 0
    artist_khan.ended = False
    artist_khan.meta = artistmeta_2
    artist_khan.type = artisttype_person
    session.add(artist_khan)

    artistcreditname_khan = ArtistCreditName()
    artistcreditname_khan.position = 0
    artistcreditname_khan.name = u'Khan'
    artistcreditname_khan.join_phrase = u''
    artistcreditname_khan.artist = artist_khan
    session.add(artistcreditname_khan)

    artistcredit_khan = ArtistCredit()
    artistcredit_khan.id = 42684
    artistcredit_khan.name = u'Khan'
    artistcredit_khan.artist_count = 1
    artistcredit_khan.ref_count = 337
    artistcredit_khan.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_khan.artists = [
        artistcreditname_khan,
    ]
    session.add(artistcredit_khan)

    recordingmeta_2 = RecordingMeta()
    session.add(recordingmeta_2)

    recording_fantomes = Recording()
    recording_fantomes.id = 7134048
    recording_fantomes.gid = 'e6d2be9c-06b7-4a64-911d-076ad4e79c6f'
    recording_fantomes.name = u'Fantomes'
    recording_fantomes.length = 262720
    recording_fantomes.comment = u''
    recording_fantomes.edits_pending = 0
    recording_fantomes.video = False
    recording_fantomes.artist_credit = artistcredit_khan
    recording_fantomes.meta = recordingmeta_2
    session.add(recording_fantomes)

    track_fantomes = Track()
    track_fantomes.id = 5918612
    track_fantomes.gid = '6e336acb-deaf-3824-ba89-5b612e2a864c'
    track_fantomes.position = 2
    track_fantomes.number = u'2'
    track_fantomes.name = u'Fantomes'
    track_fantomes.length = 262720
    track_fantomes.edits_pending = 0
    track_fantomes.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_fantomes.is_data_track = False
    track_fantomes.artist_credit = artistcredit_khan
    track_fantomes.recording = recording_fantomes
    session.add(track_fantomes)

    recordingmeta_3 = RecordingMeta()
    session.add(recordingmeta_3)

    recording_the_very_last_resort = Recording()
    recording_the_very_last_resort.id = 7134049
    recording_the_very_last_resort.gid = '1f0a5382-83a4-4570-b24a-897014826867'
    recording_the_very_last_resort.name = u'The Very Last Resort'
    recording_the_very_last_resort.length = 439146
    recording_the_very_last_resort.comment = u''
    recording_the_very_last_resort.edits_pending = 0
    recording_the_very_last_resort.video = False
    recording_the_very_last_resort.artist_credit = artistcredit_trentemoller
    recording_the_very_last_resort.meta = recordingmeta_3
    session.add(recording_the_very_last_resort)

    track_the_very_last_resort = Track()
    track_the_very_last_resort.id = 5918613
    track_the_very_last_resort.gid = '46624227-728d-3e0f-9b49-8447e9f9bc96'
    track_the_very_last_resort.position = 3
    track_the_very_last_resort.number = u'3'
    track_the_very_last_resort.name = u'The Very Last Resort'
    track_the_very_last_resort.length = 439146
    track_the_very_last_resort.edits_pending = 0
    track_the_very_last_resort.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_the_very_last_resort.is_data_track = False
    track_the_very_last_resort.artist_credit = artistcredit_trentemoller
    track_the_very_last_resort.recording = recording_the_very_last_resort
    session.add(track_the_very_last_resort)

    recordingmeta_4 = RecordingMeta()
    session.add(recordingmeta_4)

    recording_miss_you = Recording()
    recording_miss_you.id = 7134050
    recording_miss_you.gid = '98955d91-27fc-4a6c-baf9-8cdb87491814'
    recording_miss_you.name = u'Miss You'
    recording_miss_you.length = 230000
    recording_miss_you.comment = u''
    recording_miss_you.edits_pending = 0
    recording_miss_you.video = False
    recording_miss_you.artist_credit = artistcredit_trentemoller
    recording_miss_you.meta = recordingmeta_4
    session.add(recording_miss_you)

    track_miss_you = Track()
    track_miss_you.id = 5918614
    track_miss_you.gid = '1c6b5b95-cc69-363b-9ddb-62acd8f5ba7e'
    track_miss_you.position = 4
    track_miss_you.number = u'4'
    track_miss_you.name = u'Miss You'
    track_miss_you.length = 230000
    track_miss_you.edits_pending = 0
    track_miss_you.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_miss_you.is_data_track = False
    track_miss_you.artist_credit = artistcredit_trentemoller
    track_miss_you.recording = recording_miss_you
    session.add(track_miss_you)

    iso31661_3 = ISO31661()
    iso31661_3.code = u'CA'
    session.add(iso31661_3)

    area_canada = Area()
    area_canada.id = 38
    area_canada.gid = '71bbafaa-e825-3e15-8ca9-017dcad1748b'
    area_canada.name = u'Canada'
    area_canada.edits_pending = 0
    area_canada.last_updated = datetime.datetime(2013, 5, 27, 13, 15, 52, 179105)
    area_canada.ended = False
    area_canada.comment = u''
    area_canada.iso_3166_1_codes = [
        iso31661_3,
    ]
    area_canada.type = areatype_country
    session.add(area_canada)

    iso31662_2 = ISO31662()
    iso31662_2.code = u'US-NY'
    session.add(iso31662_2)

    area_new_york = Area()
    area_new_york.id = 295
    area_new_york.gid = '75e398a3-5f3f-4224-9cd8-0fe44715bc95'
    area_new_york.name = u'New York'
    area_new_york.edits_pending = 0
    area_new_york.last_updated = datetime.datetime(2013, 5, 17, 20, 23, 26, 631791)
    area_new_york.ended = False
    area_new_york.comment = u''
    area_new_york.iso_3166_2_codes = [
        iso31662_2,
    ]
    area_new_york.type = areatype_subdivision
    session.add(area_new_york)

    iso31661_4 = ISO31661()
    iso31661_4.code = u'US'
    session.add(iso31661_4)

    area_united_states = Area()
    area_united_states.id = 222
    area_united_states.gid = '489ce91b-6658-3307-9877-795b68554c98'
    area_united_states.name = u'United States'
    area_united_states.edits_pending = 0
    area_united_states.last_updated = datetime.datetime(2013, 6, 15, 18, 6, 39, 593230)
    area_united_states.ended = False
    area_united_states.comment = u''
    area_united_states.iso_3166_1_codes = [
        iso31661_4,
    ]
    area_united_states.type = areatype_country
    session.add(area_united_states)

    linkareaarea_4 = LinkAreaArea()
    linkareaarea_4.id = 35
    linkareaarea_4.edits_pending = 0
    linkareaarea_4.last_updated = datetime.datetime(2013, 5, 17, 20, 23, 44, 235720)
    linkareaarea_4.link_order = 0
    linkareaarea_4.entity0_credit = u''
    linkareaarea_4.entity1_credit = u''
    linkareaarea_4.entity0 = area_united_states
    linkareaarea_4.entity1 = area_new_york
    linkareaarea_4.link = link_1
    session.add(linkareaarea_4)

    area_montreal = Area()
    area_montreal.id = 7279
    area_montreal.gid = 'c3cc624e-b963-49cf-ad0b-e318cb341963'
    area_montreal.name = u'Montreal'
    area_montreal.edits_pending = 0
    area_montreal.last_updated = datetime.datetime(2013, 5, 26, 17, 19, 17, 882833)
    area_montreal.ended = False
    area_montreal.comment = u''
    area_montreal.type = areatype_city
    session.add(area_montreal)

    iso31662_3 = ISO31662()
    iso31662_3.code = u'CA-QC'
    session.add(iso31662_3)

    area_quebec = Area()
    area_quebec.id = 322
    area_quebec.gid = 'a510b9b1-404d-4e23-8db8-0f6585909ed8'
    area_quebec.name = u'Quebec'
    area_quebec.edits_pending = 0
    area_quebec.last_updated = datetime.datetime(2013, 5, 17, 21, 30, 9, 455218)
    area_quebec.ended = False
    area_quebec.comment = u''
    area_quebec.iso_3166_2_codes = [
        iso31662_3,
    ]
    area_quebec.type = areatype_subdivision
    session.add(area_quebec)

    linkareaarea_6 = LinkAreaArea()
    linkareaarea_6.id = 63
    linkareaarea_6.edits_pending = 0
    linkareaarea_6.last_updated = datetime.datetime(2013, 5, 17, 21, 30, 18, 168673)
    linkareaarea_6.link_order = 0
    linkareaarea_6.entity0_credit = u''
    linkareaarea_6.entity1_credit = u''
    linkareaarea_6.entity0 = area_canada
    linkareaarea_6.entity1 = area_quebec
    linkareaarea_6.link = link_1
    session.add(linkareaarea_6)

    linkareaarea_5 = LinkAreaArea()
    linkareaarea_5.id = 7045
    linkareaarea_5.edits_pending = 0
    linkareaarea_5.last_updated = datetime.datetime(2013, 5, 26, 17, 19, 37, 773186)
    linkareaarea_5.link_order = 0
    linkareaarea_5.entity0_credit = u''
    linkareaarea_5.entity1_credit = u''
    linkareaarea_5.entity0 = area_quebec
    linkareaarea_5.entity1 = area_montreal
    linkareaarea_5.link = link_1
    session.add(linkareaarea_5)

    gender_female = Gender()
    gender_female.id = 2
    gender_female.name = u'Female'
    gender_female.child_order = 2
    gender_female.gid = '93452b5a-a947-30c8-934f-6a4056b151c2'
    session.add(gender_female)

    artistmeta_3 = ArtistMeta()
    artistmeta_3.rating = 80
    artistmeta_3.rating_count = 2
    session.add(artistmeta_3)

    artist_lhasa = Artist()
    artist_lhasa.id = 308210
    artist_lhasa.gid = '95db1c7c-21b8-4956-82ad-20217cd5d395'
    artist_lhasa.name = u'Lhasa'
    artist_lhasa.sort_name = u'Lhasa'
    artist_lhasa.begin_date_year = 1972
    artist_lhasa.begin_date_month = 9
    artist_lhasa.begin_date_day = 27
    artist_lhasa.end_date_year = 2010
    artist_lhasa.end_date_month = 1
    artist_lhasa.end_date_day = 1
    artist_lhasa.comment = u'American / Canadian singer'
    artist_lhasa.edits_pending = 0
    artist_lhasa.last_updated = datetime.datetime(2014, 4, 28, 7, 0, 26, 824117)
    artist_lhasa.ended = True
    artist_lhasa.area = area_canada
    artist_lhasa.begin_area = area_new_york
    artist_lhasa.end_area = area_montreal
    artist_lhasa.gender = gender_female
    artist_lhasa.meta = artistmeta_3
    artist_lhasa.type = artisttype_person
    session.add(artist_lhasa)

    artistcreditname_lhasa = ArtistCreditName()
    artistcreditname_lhasa.position = 0
    artistcreditname_lhasa.name = u'Lhasa'
    artistcreditname_lhasa.join_phrase = u''
    artistcreditname_lhasa.artist = artist_lhasa
    session.add(artistcreditname_lhasa)

    artistcredit_lhasa = ArtistCredit()
    artistcredit_lhasa.id = 945765
    artistcredit_lhasa.name = u'Lhasa'
    artistcredit_lhasa.artist_count = 1
    artistcredit_lhasa.ref_count = 270
    artistcredit_lhasa.created = datetime.datetime(2012, 2, 17, 10, 38, 33, 908280)
    artistcredit_lhasa.artists = [
        artistcreditname_lhasa,
    ]
    session.add(artistcredit_lhasa)

    recordingmeta_5 = RecordingMeta()
    session.add(recordingmeta_5)

    recording_de_carla_a_pered = Recording()
    recording_de_carla_a_pered.id = 7134051
    recording_de_carla_a_pered.gid = 'c14c0467-edcb-483b-891e-555776fff31c'
    recording_de_carla_a_pered.name = u'De Carla a Pered'
    recording_de_carla_a_pered.length = 207346
    recording_de_carla_a_pered.comment = u''
    recording_de_carla_a_pered.edits_pending = 0
    recording_de_carla_a_pered.last_updated = datetime.datetime(2012, 4, 11, 0, 0, 11, 85366)
    recording_de_carla_a_pered.video = False
    recording_de_carla_a_pered.artist_credit = artistcredit_lhasa
    recording_de_carla_a_pered.meta = recordingmeta_5
    session.add(recording_de_carla_a_pered)

    track_de_carla_a_pered = Track()
    track_de_carla_a_pered.id = 5918615
    track_de_carla_a_pered.gid = 'ff49a567-bde9-37da-b49b-9a37e59e475c'
    track_de_carla_a_pered.position = 5
    track_de_carla_a_pered.number = u'5'
    track_de_carla_a_pered.name = u'De Carla a Pered'
    track_de_carla_a_pered.length = 207346
    track_de_carla_a_pered.edits_pending = 0
    track_de_carla_a_pered.last_updated = datetime.datetime(2012, 4, 11, 0, 0, 11, 85366)
    track_de_carla_a_pered.is_data_track = False
    track_de_carla_a_pered.artist_credit = artistcredit_lhasa
    track_de_carla_a_pered.recording = recording_de_carla_a_pered
    session.add(track_de_carla_a_pered)

    iso31661_5 = ISO31661()
    iso31661_5.code = u'MX'
    session.add(iso31661_5)

    area_mexico = Area()
    area_mexico.id = 138
    area_mexico.gid = '3e08b2cd-69f3-317c-b1e4-e71be581839e'
    area_mexico.name = u'Mexico'
    area_mexico.edits_pending = 0
    area_mexico.last_updated = datetime.datetime(2013, 5, 27, 13, 41, 13, 615269)
    area_mexico.ended = False
    area_mexico.comment = u''
    area_mexico.iso_3166_1_codes = [
        iso31661_5,
    ]
    area_mexico.type = areatype_country
    session.add(area_mexico)

    area_tijuana = Area()
    area_tijuana.id = 10169
    area_tijuana.gid = '0c81089f-621b-4c30-acf3-a5d81f07f84b'
    area_tijuana.name = u'Tijuana'
    area_tijuana.edits_pending = 0
    area_tijuana.last_updated = datetime.datetime(2013, 11, 2, 17, 34, 24, 823163)
    area_tijuana.ended = False
    area_tijuana.comment = u''
    area_tijuana.type = areatype_city
    session.add(area_tijuana)

    iso31662_4 = ISO31662()
    iso31662_4.code = u'MX-BCN'
    session.add(iso31662_4)

    area_baja_california = Area()
    area_baja_california.id = 1496
    area_baja_california.gid = 'a7cf05a3-6ea1-479f-bb61-7b2259872d7b'
    area_baja_california.name = u'Baja California'
    area_baja_california.edits_pending = 0
    area_baja_california.last_updated = datetime.datetime(2013, 6, 5, 6, 35, 35, 57454)
    area_baja_california.ended = False
    area_baja_california.comment = u''
    area_baja_california.iso_3166_2_codes = [
        iso31662_4,
    ]
    area_baja_california.type = areatype_subdivision
    session.add(area_baja_california)

    linkareaarea_8 = LinkAreaArea()
    linkareaarea_8.id = 1256
    linkareaarea_8.edits_pending = 0
    linkareaarea_8.last_updated = datetime.datetime(2013, 5, 20, 0, 7, 49, 858860)
    linkareaarea_8.link_order = 0
    linkareaarea_8.entity0_credit = u''
    linkareaarea_8.entity1_credit = u''
    linkareaarea_8.entity0 = area_mexico
    linkareaarea_8.entity1 = area_baja_california
    linkareaarea_8.link = link_1
    session.add(linkareaarea_8)

    linkareaarea_7 = LinkAreaArea()
    linkareaarea_7.id = 9935
    linkareaarea_7.edits_pending = 0
    linkareaarea_7.last_updated = datetime.datetime(2013, 6, 18, 12, 44, 34, 976794)
    linkareaarea_7.link_order = 0
    linkareaarea_7.entity0_credit = u''
    linkareaarea_7.entity1_credit = u''
    linkareaarea_7.entity0 = area_baja_california
    linkareaarea_7.entity1 = area_tijuana
    linkareaarea_7.link = link_1
    session.add(linkareaarea_7)

    artistipi_3 = ArtistIPI()
    artistipi_3.ipi = u'00489884469'
    artistipi_3.edits_pending = 0
    artistipi_3.created = datetime.datetime(2015, 6, 16, 22, 0, 46, 955695)
    session.add(artistipi_3)

    artistmeta_4 = ArtistMeta()
    session.add(artistmeta_4)

    artist_murcof = Artist()
    artist_murcof.id = 68534
    artist_murcof.gid = 'e8d1f02e-7e77-4415-85b6-dc17e08debbf'
    artist_murcof.name = u'Murcof'
    artist_murcof.sort_name = u'Murcof'
    artist_murcof.begin_date_year = 1970
    artist_murcof.begin_date_month = 7
    artist_murcof.begin_date_day = 26
    artist_murcof.comment = u''
    artist_murcof.edits_pending = 0
    artist_murcof.last_updated = datetime.datetime(2015, 6, 16, 22, 0, 46, 955695)
    artist_murcof.ended = False
    artist_murcof.area = area_mexico
    artist_murcof.begin_area = area_tijuana
    artist_murcof.gender = gender_male
    artist_murcof.ipis = [
        artistipi_3,
    ]
    artist_murcof.meta = artistmeta_4
    artist_murcof.type = artisttype_person
    session.add(artist_murcof)

    artistcreditname_murcof = ArtistCreditName()
    artistcreditname_murcof.position = 0
    artistcreditname_murcof.name = u'Murcof'
    artistcreditname_murcof.join_phrase = u''
    artistcreditname_murcof.artist = artist_murcof
    session.add(artistcreditname_murcof)

    artistcredit_murcof = ArtistCredit()
    artistcredit_murcof.id = 68534
    artistcredit_murcof.name = u'Murcof'
    artistcredit_murcof.artist_count = 1
    artistcredit_murcof.ref_count = 361
    artistcredit_murcof.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_murcof.artists = [
        artistcreditname_murcof,
    ]
    session.add(artistcredit_murcof)

    recordingmeta_6 = RecordingMeta()
    session.add(recordingmeta_6)

    recording_una = Recording()
    recording_una.id = 7134052
    recording_una.gid = '4a9caecb-bb01-4ac0-b9e6-2e7613c0317b'
    recording_una.name = u'Una'
    recording_una.length = 271200
    recording_una.comment = u''
    recording_una.edits_pending = 0
    recording_una.video = False
    recording_una.artist_credit = artistcredit_murcof
    recording_una.meta = recordingmeta_6
    session.add(recording_una)

    track_una = Track()
    track_una.id = 5918616
    track_una.gid = 'de879ef5-c5c5-338a-a863-b3fd79a6b581'
    track_una.position = 6
    track_una.number = u'6'
    track_una.name = u'Una'
    track_una.length = 271200
    track_una.edits_pending = 0
    track_una.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_una.is_data_track = False
    track_una.artist_credit = artistcredit_murcof
    track_una.recording = recording_una
    session.add(track_una)

    recordingmeta_7 = RecordingMeta()
    session.add(recordingmeta_7)

    recording_snowflake = Recording()
    recording_snowflake.id = 7134053
    recording_snowflake.gid = '7fb5de20-ce10-48e6-b61c-0101192c5a51'
    recording_snowflake.name = u'Snowflake'
    recording_snowflake.length = 447026
    recording_snowflake.comment = u''
    recording_snowflake.edits_pending = 0
    recording_snowflake.video = False
    recording_snowflake.artist_credit = artistcredit_trentemoller
    recording_snowflake.meta = recordingmeta_7
    session.add(recording_snowflake)

    track_snowflake = Track()
    track_snowflake.id = 5918617
    track_snowflake.gid = '8d32398e-757e-3d72-93c3-628671da9d38'
    track_snowflake.position = 7
    track_snowflake.number = u'7'
    track_snowflake.name = u'Snowflake'
    track_snowflake.length = 447026
    track_snowflake.edits_pending = 0
    track_snowflake.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_snowflake.is_data_track = False
    track_snowflake.artist_credit = artistcredit_trentemoller
    track_snowflake.recording = recording_snowflake
    session.add(track_snowflake)

    iso31661_6 = ISO31661()
    iso31661_6.code = u'JM'
    session.add(iso31661_6)

    area_jamaica = Area()
    area_jamaica.id = 106
    area_jamaica.gid = '2dd47a64-91d5-3b13-bc94-80043ed063d7'
    area_jamaica.name = u'Jamaica'
    area_jamaica.edits_pending = 0
    area_jamaica.last_updated = datetime.datetime(2013, 5, 27, 12, 32, 31, 72979)
    area_jamaica.ended = False
    area_jamaica.comment = u''
    area_jamaica.iso_3166_1_codes = [
        iso31661_6,
    ]
    area_jamaica.type = areatype_country
    session.add(area_jamaica)

    artistmeta_5 = ArtistMeta()
    session.add(artistmeta_5)

    artisttype_orchestra = ArtistType()
    artisttype_orchestra.id = 5
    artisttype_orchestra.name = u'Orchestra'
    artisttype_orchestra.child_order = 0
    artisttype_orchestra.gid = 'a0b36c92-3eb1-3839-a4f9-4799823f54a5'
    session.add(artisttype_orchestra)

    artisttype_choir = ArtistType()
    artisttype_choir.id = 6
    artisttype_choir.name = u'Choir'
    artisttype_choir.child_order = 0
    artisttype_choir.gid = '6124967d-7e3a-3eba-b642-c9a2ffb44d94'
    session.add(artisttype_choir)

    artisttype_group = ArtistType()
    artisttype_group.id = 2
    artisttype_group.name = u'Group'
    artisttype_group.child_order = 2
    artisttype_group.gid = 'e431f5f6-b5d2-343d-8b36-72607fffb74b'
    artisttype_group.parent = [
        artisttype_orchestra,
        artisttype_choir,
    ]
    session.add(artisttype_group)

    artist_the_crystalites = Artist()
    artist_the_crystalites.id = 134514
    artist_the_crystalites.gid = '41ee41ff-cec6-46a6-8e67-5991a8ebc2ed'
    artist_the_crystalites.name = u'The Crystalites'
    artist_the_crystalites.sort_name = u'Crystalites, The'
    artist_the_crystalites.comment = u'JM reggae group, studio group with prod. Derrick Harriott'
    artist_the_crystalites.edits_pending = 0
    artist_the_crystalites.last_updated = datetime.datetime(2011, 8, 10, 7, 0, 11, 778408)
    artist_the_crystalites.ended = False
    artist_the_crystalites.area = area_jamaica
    artist_the_crystalites.meta = artistmeta_5
    artist_the_crystalites.type = artisttype_group
    session.add(artist_the_crystalites)

    artistcreditname_the_crystalites = ArtistCreditName()
    artistcreditname_the_crystalites.position = 0
    artistcreditname_the_crystalites.name = u'The Crystalites'
    artistcreditname_the_crystalites.join_phrase = u''
    artistcreditname_the_crystalites.artist = artist_the_crystalites
    session.add(artistcreditname_the_crystalites)

    artistcredit_the_crystalites = ArtistCredit()
    artistcredit_the_crystalites.id = 134514
    artistcredit_the_crystalites.name = u'The Crystalites'
    artistcredit_the_crystalites.artist_count = 1
    artistcredit_the_crystalites.ref_count = 94
    artistcredit_the_crystalites.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_the_crystalites.artists = [
        artistcreditname_the_crystalites,
    ]
    session.add(artistcredit_the_crystalites)

    recordingmeta_8 = RecordingMeta()
    session.add(recordingmeta_8)

    recording_concentration_version_3 = Recording()
    recording_concentration_version_3.id = 7134054
    recording_concentration_version_3.gid = 'b52e86aa-4481-432c-a5ac-9f830cfcb2a8'
    recording_concentration_version_3.name = u'Concentration (version 3)'
    recording_concentration_version_3.length = 202746
    recording_concentration_version_3.comment = u''
    recording_concentration_version_3.edits_pending = 0
    recording_concentration_version_3.video = False
    recording_concentration_version_3.artist_credit = artistcredit_the_crystalites
    recording_concentration_version_3.meta = recordingmeta_8
    session.add(recording_concentration_version_3)

    track_concentration_version_3 = Track()
    track_concentration_version_3.id = 5918618
    track_concentration_version_3.gid = 'bd12916b-0e92-3d06-8ac2-bea1a703e789'
    track_concentration_version_3.position = 8
    track_concentration_version_3.number = u'8'
    track_concentration_version_3.name = u'Concentration (version 3)'
    track_concentration_version_3.length = 202746
    track_concentration_version_3.edits_pending = 0
    track_concentration_version_3.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_concentration_version_3.is_data_track = False
    track_concentration_version_3.artist_credit = artistcredit_the_crystalites
    track_concentration_version_3.recording = recording_concentration_version_3
    session.add(track_concentration_version_3)

    recordingmeta_9 = RecordingMeta()
    session.add(recordingmeta_9)

    recording_evil_dub = Recording()
    recording_evil_dub.id = 7134055
    recording_evil_dub.gid = 'f21b457c-464f-4544-9106-870e0b68323b'
    recording_evil_dub.name = u'Evil Dub'
    recording_evil_dub.length = 302813
    recording_evil_dub.comment = u''
    recording_evil_dub.edits_pending = 0
    recording_evil_dub.video = False
    recording_evil_dub.artist_credit = artistcredit_trentemoller
    recording_evil_dub.meta = recordingmeta_9
    session.add(recording_evil_dub)

    track_evil_dub = Track()
    track_evil_dub.id = 5918619
    track_evil_dub.gid = '41256b61-9fa2-33e4-bc64-0dc266ede203'
    track_evil_dub.position = 9
    track_evil_dub.number = u'9'
    track_evil_dub.name = u'Evil Dub'
    track_evil_dub.length = 302813
    track_evil_dub.edits_pending = 0
    track_evil_dub.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_evil_dub.is_data_track = False
    track_evil_dub.artist_credit = artistcredit_trentemoller
    track_evil_dub.recording = recording_evil_dub
    session.add(track_evil_dub)

    iso31662_5 = ISO31662()
    iso31662_5.code = u'GB-COV'
    session.add(iso31662_5)

    area_coventry = Area()
    area_coventry.id = 3917
    area_coventry.gid = 'aab979a4-b106-4baa-a4a3-fc45f775cff9'
    area_coventry.name = u'Coventry'
    area_coventry.edits_pending = 0
    area_coventry.last_updated = datetime.datetime(2013, 6, 5, 10, 26, 16, 645060)
    area_coventry.ended = False
    area_coventry.comment = u''
    area_coventry.iso_3166_2_codes = [
        iso31662_5,
    ]
    area_coventry.type = areatype_subdivision
    session.add(area_coventry)

    area_west_midlands = Area()
    area_west_midlands.id = 4025
    area_west_midlands.gid = '07607044-8140-47ba-bb24-7129babe586b'
    area_west_midlands.name = u'West Midlands'
    area_west_midlands.edits_pending = 0
    area_west_midlands.last_updated = datetime.datetime(2013, 8, 28, 13, 50, 43, 164525)
    area_west_midlands.ended = False
    area_west_midlands.comment = u''
    area_west_midlands.type = areatype_subdivision
    session.add(area_west_midlands)

    iso31662_6 = ISO31662()
    iso31662_6.code = u'GB-ENG'
    session.add(iso31662_6)

    area_england = Area()
    area_england.id = 432
    area_england.gid = '9d5dd675-3cf4-4296-9e39-67865ebee758'
    area_england.name = u'England'
    area_england.edits_pending = 0
    area_england.last_updated = datetime.datetime(2013, 5, 18, 0, 11, 46, 530087)
    area_england.ended = False
    area_england.comment = u''
    area_england.iso_3166_2_codes = [
        iso31662_6,
    ]
    area_england.type = areatype_subdivision
    session.add(area_england)

    linkareaarea_11 = LinkAreaArea()
    linkareaarea_11.id = 173
    linkareaarea_11.edits_pending = 0
    linkareaarea_11.last_updated = datetime.datetime(2013, 5, 18, 0, 12, 5, 966838)
    linkareaarea_11.link_order = 0
    linkareaarea_11.entity0_credit = u''
    linkareaarea_11.entity1_credit = u''
    linkareaarea_11.entity0 = area_united_kingdom
    linkareaarea_11.entity1 = area_england
    linkareaarea_11.link = link_1
    session.add(linkareaarea_11)

    linkareaarea_10 = LinkAreaArea()
    linkareaarea_10.id = 3791
    linkareaarea_10.edits_pending = 0
    linkareaarea_10.last_updated = datetime.datetime(2013, 5, 21, 16, 41, 26, 84075)
    linkareaarea_10.link_order = 0
    linkareaarea_10.entity0_credit = u''
    linkareaarea_10.entity1_credit = u''
    linkareaarea_10.entity0 = area_england
    linkareaarea_10.entity1 = area_west_midlands
    linkareaarea_10.link = link_1
    session.add(linkareaarea_10)

    linkareaarea_9 = LinkAreaArea()
    linkareaarea_9.id = 3683
    linkareaarea_9.edits_pending = 0
    linkareaarea_9.last_updated = datetime.datetime(2013, 5, 21, 16, 40, 51, 794729)
    linkareaarea_9.link_order = 0
    linkareaarea_9.entity0_credit = u''
    linkareaarea_9.entity1_credit = u''
    linkareaarea_9.entity0 = area_west_midlands
    linkareaarea_9.entity1 = area_coventry
    linkareaarea_9.link = link_1
    session.add(linkareaarea_9)

    artistisni_2 = ArtistISNI()
    artistisni_2.isni = u'0000000122859471'
    artistisni_2.edits_pending = 0
    artistisni_2.created = datetime.datetime(2013, 5, 26, 10, 0, 11, 791620)
    session.add(artistisni_2)

    artistmeta_6 = ArtistMeta()
    artistmeta_6.rating = 80
    artistmeta_6.rating_count = 2
    session.add(artistmeta_6)

    artist_the_specials = Artist()
    artist_the_specials.id = 11619
    artist_the_specials.gid = '07eb40a2-2914-439c-a01d-15a685b84ddf'
    artist_the_specials.name = u'The Specials'
    artist_the_specials.sort_name = u'Specials, The'
    artist_the_specials.begin_date_year = 1977
    artist_the_specials.comment = u'ska band'
    artist_the_specials.edits_pending = 0
    artist_the_specials.last_updated = datetime.datetime(2015, 7, 20, 23, 2, 33, 185085)
    artist_the_specials.ended = False
    artist_the_specials.area = area_united_kingdom
    artist_the_specials.begin_area = area_coventry
    artist_the_specials.isnis = [
        artistisni_2,
    ]
    artist_the_specials.meta = artistmeta_6
    artist_the_specials.type = artisttype_group
    session.add(artist_the_specials)

    artistcreditname_the_specials = ArtistCreditName()
    artistcreditname_the_specials.position = 0
    artistcreditname_the_specials.name = u'The Specials'
    artistcreditname_the_specials.join_phrase = u''
    artistcreditname_the_specials.artist = artist_the_specials
    session.add(artistcreditname_the_specials)

    artistcredit_the_specials = ArtistCredit()
    artistcredit_the_specials.id = 11619
    artistcredit_the_specials.name = u'The Specials'
    artistcredit_the_specials.artist_count = 1
    artistcredit_the_specials.ref_count = 2223
    artistcredit_the_specials.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_the_specials.artists = [
        artistcreditname_the_specials,
    ]
    session.add(artistcredit_the_specials)

    recordingmeta_10 = RecordingMeta()
    session.add(recordingmeta_10)

    recording_ghost_town = Recording()
    recording_ghost_town.id = 7134056
    recording_ghost_town.gid = '9a94277f-fc62-4e12-ba14-1354ddb39143'
    recording_ghost_town.name = u'Ghost Town'
    recording_ghost_town.length = 311986
    recording_ghost_town.comment = u''
    recording_ghost_town.edits_pending = 0
    recording_ghost_town.video = False
    recording_ghost_town.artist_credit = artistcredit_the_specials
    recording_ghost_town.meta = recordingmeta_10
    session.add(recording_ghost_town)

    workmeta_1 = WorkMeta()
    session.add(workmeta_1)

    worktype_song = WorkType()
    worktype_song.id = 17
    worktype_song.name = u'Song'
    worktype_song.child_order = 1
    worktype_song.description = u'A song is in its origin (and still in most cases) a composition for voice, with or without instruments, performed by singing. This is the most common form by far in folk and popular music, but also fairly common in a classical context ("art songs").'
    worktype_song.gid = 'f061270a-2fd6-32f1-a641-f0f8676d14e6'
    session.add(worktype_song)

    work_ghost_town = Work()
    work_ghost_town.id = 9452109
    work_ghost_town.gid = '5b71b31e-0dc2-395e-bfa6-8076c9210923'
    work_ghost_town.name = u'Ghost Town'
    work_ghost_town.comment = u''
    work_ghost_town.edits_pending = 0
    work_ghost_town.last_updated = datetime.datetime(2013, 1, 5, 15, 44, 7, 489077)
    work_ghost_town.meta = workmeta_1
    work_ghost_town.type = worktype_song
    session.add(work_ghost_town)

    artistipi_4 = ArtistIPI()
    artistipi_4.ipi = u'00073107302'
    artistipi_4.edits_pending = 0
    artistipi_4.created = datetime.datetime(2012, 6, 10, 1, 0, 13, 716026)
    session.add(artistipi_4)

    artistisni_3 = ArtistISNI()
    artistisni_3.isni = u'0000000034830054'
    artistisni_3.edits_pending = 0
    artistisni_3.created = datetime.datetime(2016, 7, 8, 20, 0, 25, 426938)
    session.add(artistisni_3)

    artistmeta_7 = ArtistMeta()
    session.add(artistmeta_7)

    artist_jerry_dammers = Artist()
    artist_jerry_dammers.id = 120484
    artist_jerry_dammers.gid = 'a582c67f-106c-4e31-85a1-f7513941c1f0'
    artist_jerry_dammers.name = u'Jerry Dammers'
    artist_jerry_dammers.sort_name = u'Dammers, Jerry'
    artist_jerry_dammers.begin_date_year = 1955
    artist_jerry_dammers.begin_date_month = 5
    artist_jerry_dammers.begin_date_day = 22
    artist_jerry_dammers.comment = u''
    artist_jerry_dammers.edits_pending = 0
    artist_jerry_dammers.last_updated = datetime.datetime(2016, 7, 8, 20, 0, 25, 426938)
    artist_jerry_dammers.ended = False
    artist_jerry_dammers.area = area_united_kingdom
    artist_jerry_dammers.gender = gender_male
    artist_jerry_dammers.ipis = [
        artistipi_4,
    ]
    artist_jerry_dammers.isnis = [
        artistisni_3,
    ]
    artist_jerry_dammers.meta = artistmeta_7
    artist_jerry_dammers.type = artisttype_person
    session.add(artist_jerry_dammers)

    linktype_lyricist = LinkType()
    linktype_lyricist.id = 165
    linktype_lyricist.child_order = 1
    linktype_lyricist.gid = '3e48faba-ec01-47fd-8e89-30e81161661c'
    linktype_lyricist.entity_type0 = u'artist'
    linktype_lyricist.entity_type1 = u'work'
    linktype_lyricist.name = u'lyricist'
    linktype_lyricist.description = u'Indicates the lyricist for this work.'
    linktype_lyricist.link_phrase = u'{additional} lyrics'
    linktype_lyricist.reverse_link_phrase = u'{additional} lyricist'
    linktype_lyricist.long_link_phrase = u'{additional:additionally} wrote the lyrics for'
    linktype_lyricist.priority = 0
    linktype_lyricist.last_updated = datetime.datetime(2015, 8, 20, 12, 20, 55, 940196)
    linktype_lyricist.is_deprecated = False
    linktype_lyricist.has_dates = True
    linktype_lyricist.entity0_cardinality = 1
    linktype_lyricist.entity1_cardinality = 0
    session.add(linktype_lyricist)

    link_2 = Link()
    link_2.id = 12776
    link_2.attribute_count = 0
    link_2.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_2.ended = False
    link_2.link_type = linktype_lyricist
    session.add(link_2)

    linkartistwork_1 = LinkArtistWork()
    linkartistwork_1.id = 655061
    linkartistwork_1.edits_pending = 0
    linkartistwork_1.last_updated = datetime.datetime(2013, 1, 19, 15, 12, 8, 731560)
    linkartistwork_1.link_order = 0
    linkartistwork_1.entity0_credit = u''
    linkartistwork_1.entity1_credit = u''
    linkartistwork_1.entity0 = artist_jerry_dammers
    linkartistwork_1.entity1 = work_ghost_town
    linkartistwork_1.link = link_2
    session.add(linkartistwork_1)

    linktype_composer = LinkType()
    linktype_composer.id = 168
    linktype_composer.child_order = 0
    linktype_composer.gid = 'd59d99ea-23d4-4a80-b066-edca32ee158f'
    linktype_composer.entity_type0 = u'artist'
    linktype_composer.entity_type1 = u'work'
    linktype_composer.name = u'composer'
    linktype_composer.description = u'Indicates the composer for this work, i.e. the artist who wrote the music (not necessarily the lyrics).'
    linktype_composer.link_phrase = u'{additional:additionally} composed'
    linktype_composer.reverse_link_phrase = u'{additional} composer'
    linktype_composer.long_link_phrase = u'{additional:additionally} composed'
    linktype_composer.priority = 0
    linktype_composer.last_updated = datetime.datetime(2013, 12, 17, 9, 43, 39, 279845)
    linktype_composer.is_deprecated = False
    linktype_composer.has_dates = True
    linktype_composer.entity0_cardinality = 1
    linktype_composer.entity1_cardinality = 0
    session.add(linktype_composer)

    link_3 = Link()
    link_3.id = 12757
    link_3.attribute_count = 0
    link_3.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_3.ended = False
    link_3.link_type = linktype_composer
    session.add(link_3)

    linkartistwork_2 = LinkArtistWork()
    linkartistwork_2.id = 665687
    linkartistwork_2.edits_pending = 0
    linkartistwork_2.last_updated = datetime.datetime(2013, 1, 19, 15, 12, 8, 731560)
    linkartistwork_2.link_order = 0
    linkartistwork_2.entity0_credit = u''
    linkartistwork_2.entity1_credit = u''
    linkartistwork_2.entity0 = artist_jerry_dammers
    linkartistwork_2.entity1 = work_ghost_town
    linkartistwork_2.link = link_3
    session.add(linkartistwork_2)

    url_1 = URL()
    url_1.id = 2135537
    url_1.gid = '4eecc417-923e-43be-897a-bc5243e1861b'
    url_1.url = u'https://www.wikidata.org/wiki/Q15123297'
    url_1.edits_pending = 0
    url_1.last_updated = datetime.datetime(2016, 7, 9, 16, 0, 2, 213148)
    session.add(url_1)

    linktype_wikidata = LinkType()
    linktype_wikidata.id = 351
    linktype_wikidata.child_order = 0
    linktype_wikidata.gid = '587fdd8f-080e-46a9-97af-6425ebbcb3a2'
    linktype_wikidata.entity_type0 = u'url'
    linktype_wikidata.entity_type1 = u'work'
    linktype_wikidata.name = u'wikidata'
    linktype_wikidata.description = u'Points to the Wikidata page for this work.'
    linktype_wikidata.link_phrase = u'Wikidata page for'
    linktype_wikidata.reverse_link_phrase = u'Wikidata'
    linktype_wikidata.long_link_phrase = u'{entity1} has a Wikidata page at {entity0}'
    linktype_wikidata.priority = 0
    linktype_wikidata.last_updated = datetime.datetime(2015, 11, 5, 15, 40, 23, 984173)
    linktype_wikidata.is_deprecated = False
    linktype_wikidata.has_dates = False
    linktype_wikidata.entity0_cardinality = 0
    linktype_wikidata.entity1_cardinality = 0
    session.add(linktype_wikidata)

    link_4 = Link()
    link_4.id = 117676
    link_4.attribute_count = 0
    link_4.created = datetime.datetime(2013, 5, 9, 9, 38, 52, 992053)
    link_4.ended = False
    link_4.link_type = linktype_wikidata
    session.add(link_4)

    linkurlwork_1 = LinkURLWork()
    linkurlwork_1.id = 57535
    linkurlwork_1.edits_pending = 0
    linkurlwork_1.last_updated = datetime.datetime(2013, 11, 8, 7, 48, 21, 908103)
    linkurlwork_1.link_order = 0
    linkurlwork_1.entity0_credit = u''
    linkurlwork_1.entity1_credit = u''
    linkurlwork_1.entity0 = url_1
    linkurlwork_1.entity1 = work_ghost_town
    linkurlwork_1.link = link_4
    session.add(linkurlwork_1)

    url_2 = URL()
    url_2.id = 2874525
    url_2.gid = '7c7f679e-df95-4eb4-b311-f9c019426b14'
    url_2.url = u'http://www.secondhandsongs.com/work/6505'
    url_2.edits_pending = 0
    url_2.last_updated = datetime.datetime(2015, 1, 4, 19, 40, 18, 215035)
    session.add(url_2)

    linktype_secondhandsongs = LinkType()
    linktype_secondhandsongs.id = 280
    linktype_secondhandsongs.child_order = 0
    linktype_secondhandsongs.gid = 'b80dff64-9560-445a-b824-c8b432d77a52'
    linktype_secondhandsongs.entity_type0 = u'url'
    linktype_secondhandsongs.entity_type1 = u'work'
    linktype_secondhandsongs.name = u'secondhandsongs'
    linktype_secondhandsongs.description = u'This is used to link a work to its corresponding page in SecondHandSongs database.'
    linktype_secondhandsongs.link_phrase = u'SecondHandSongs page for'
    linktype_secondhandsongs.reverse_link_phrase = u'SecondHandSongs'
    linktype_secondhandsongs.long_link_phrase = u'{entity1} has a SecondHandSongs page at {entity0}'
    linktype_secondhandsongs.priority = 0
    linktype_secondhandsongs.last_updated = datetime.datetime(2015, 11, 5, 15, 41, 42, 657295)
    linktype_secondhandsongs.is_deprecated = False
    linktype_secondhandsongs.has_dates = False
    linktype_secondhandsongs.entity0_cardinality = 0
    linktype_secondhandsongs.entity1_cardinality = 0
    session.add(linktype_secondhandsongs)

    link_5 = Link()
    link_5.id = 27375
    link_5.attribute_count = 0
    link_5.created = datetime.datetime(2011, 5, 30, 21, 46, 48, 730067)
    link_5.ended = False
    link_5.link_type = linktype_secondhandsongs
    session.add(link_5)

    linkurlwork_2 = LinkURLWork()
    linkurlwork_2.id = 80844
    linkurlwork_2.edits_pending = 0
    linkurlwork_2.last_updated = datetime.datetime(2015, 1, 4, 19, 40, 18, 215035)
    linkurlwork_2.link_order = 0
    linkurlwork_2.entity0_credit = u''
    linkurlwork_2.entity1_credit = u''
    linkurlwork_2.entity0 = url_2
    linkurlwork_2.entity1 = work_ghost_town
    linkurlwork_2.link = link_5
    session.add(linkurlwork_2)

    linktype_performance = LinkType()
    linktype_performance.id = 278
    linktype_performance.child_order = 0
    linktype_performance.gid = 'a3005666-a872-32c3-ad06-98af558e99b0'
    linktype_performance.entity_type0 = u'recording'
    linktype_performance.entity_type1 = u'work'
    linktype_performance.name = u'performance'
    linktype_performance.description = u'This is used to link works to their recordings.'
    linktype_performance.link_phrase = u'{live} {medley:medley including a} {partial} {instrumental} {cover} recording of'
    linktype_performance.reverse_link_phrase = u'{live} {medley:medleys including} {partial} {instrumental} {cover} recordings'
    linktype_performance.long_link_phrase = u'is a {live} {medley:medley including a} {partial} {instrumental} {cover} recording of'
    linktype_performance.priority = 0
    linktype_performance.last_updated = datetime.datetime(2014, 4, 30, 22, 13, 30, 471336)
    linktype_performance.is_deprecated = False
    linktype_performance.has_dates = True
    linktype_performance.entity0_cardinality = 0
    linktype_performance.entity1_cardinality = 1
    session.add(linktype_performance)

    link_6 = Link()
    link_6.id = 27124
    link_6.attribute_count = 0
    link_6.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_6.ended = False
    link_6.link_type = linktype_performance
    session.add(link_6)

    linkrecordingwork_1 = LinkRecordingWork()
    linkrecordingwork_1.id = 1580416
    linkrecordingwork_1.edits_pending = 0
    linkrecordingwork_1.last_updated = datetime.datetime(2015, 1, 4, 19, 44, 46, 564899)
    linkrecordingwork_1.link_order = 0
    linkrecordingwork_1.entity0_credit = u''
    linkrecordingwork_1.entity1_credit = u''
    linkrecordingwork_1.entity0 = recording_ghost_town
    linkrecordingwork_1.entity1 = work_ghost_town
    linkrecordingwork_1.link = link_6
    session.add(linkrecordingwork_1)

    track_ghost_town = Track()
    track_ghost_town.id = 5918620
    track_ghost_town.gid = 'ea027835-8081-36fc-a8d7-1f9fc9406f65'
    track_ghost_town.position = 10
    track_ghost_town.number = u'10'
    track_ghost_town.name = u'Ghost Town'
    track_ghost_town.length = 311986
    track_ghost_town.edits_pending = 0
    track_ghost_town.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_ghost_town.is_data_track = False
    track_ghost_town.artist_credit = artistcredit_the_specials
    track_ghost_town.recording = recording_ghost_town
    session.add(track_ghost_town)

    artistmeta_8 = ArtistMeta()
    session.add(artistmeta_8)

    artist_businessman = Artist()
    artist_businessman.id = 455235
    artist_businessman.gid = 'ac6eaeb6-a855-41a1-a461-f23dd292513c'
    artist_businessman.name = u'Businessman'
    artist_businessman.sort_name = u'Businessman'
    artist_businessman.comment = u''
    artist_businessman.edits_pending = 0
    artist_businessman.ended = False
    artist_businessman.meta = artistmeta_8
    artist_businessman.type = artisttype_person
    session.add(artist_businessman)

    artistcreditname_businessman = ArtistCreditName()
    artistcreditname_businessman.position = 0
    artistcreditname_businessman.name = u'Businessman'
    artistcreditname_businessman.join_phrase = u''
    artistcreditname_businessman.artist = artist_businessman
    session.add(artistcreditname_businessman)

    artistcredit_businessman = ArtistCredit()
    artistcredit_businessman.id = 455235
    artistcredit_businessman.name = u'Businessman'
    artistcredit_businessman.artist_count = 1
    artistcredit_businessman.ref_count = 6
    artistcredit_businessman.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_businessman.artists = [
        artistcreditname_businessman,
    ]
    session.add(artistcredit_businessman)

    recordingmeta_11 = RecordingMeta()
    session.add(recordingmeta_11)

    recording_dubby_games = Recording()
    recording_dubby_games.id = 7134057
    recording_dubby_games.gid = '94fb758f-5ec5-4c35-91d1-b8f94b877ecb'
    recording_dubby_games.name = u'Dubby Games'
    recording_dubby_games.length = 286213
    recording_dubby_games.comment = u''
    recording_dubby_games.edits_pending = 0
    recording_dubby_games.video = False
    recording_dubby_games.artist_credit = artistcredit_businessman
    recording_dubby_games.meta = recordingmeta_11
    session.add(recording_dubby_games)

    track_dubby_games = Track()
    track_dubby_games.id = 5918621
    track_dubby_games.gid = '3b1d1d75-20da-30c8-aec3-4907497a78fa'
    track_dubby_games.position = 11
    track_dubby_games.number = u'11'
    track_dubby_games.name = u'Dubby Games'
    track_dubby_games.length = 286213
    track_dubby_games.edits_pending = 0
    track_dubby_games.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_dubby_games.is_data_track = False
    track_dubby_games.artist_credit = artistcredit_businessman
    track_dubby_games.recording = recording_dubby_games
    session.add(track_dubby_games)

    recordingmeta_12 = RecordingMeta()
    session.add(recordingmeta_12)

    recording_nightwalker = Recording()
    recording_nightwalker.id = 7134058
    recording_nightwalker.gid = '54b7b412-fc69-4fc7-8c96-17800eda3a98'
    recording_nightwalker.name = u'Nightwalker'
    recording_nightwalker.length = 267186
    recording_nightwalker.comment = u''
    recording_nightwalker.edits_pending = 0
    recording_nightwalker.video = False
    recording_nightwalker.artist_credit = artistcredit_trentemoller
    recording_nightwalker.meta = recordingmeta_12
    session.add(recording_nightwalker)

    track_nightwalker = Track()
    track_nightwalker.id = 5918622
    track_nightwalker.gid = 'fdf48b89-cd36-3256-8d87-489b48e04fdd'
    track_nightwalker.position = 12
    track_nightwalker.number = u'12'
    track_nightwalker.name = u'Nightwalker'
    track_nightwalker.length = 267186
    track_nightwalker.edits_pending = 0
    track_nightwalker.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_nightwalker.is_data_track = False
    track_nightwalker.artist_credit = artistcredit_trentemoller
    track_nightwalker.recording = recording_nightwalker
    session.add(track_nightwalker)

    medium_1 = Medium()
    medium_1.id = 291054
    medium_1.position = 1
    medium_1.name = u''
    medium_1.edits_pending = 0
    medium_1.last_updated = datetime.datetime(2012, 5, 27, 11, 5, 54, 679406)
    medium_1.track_count = 12
    medium_1.format = mediumformat_cd
    medium_1.tracks = [
        track_small_piano_piece,
        track_fantomes,
        track_the_very_last_resort,
        track_miss_you,
        track_de_carla_a_pered,
        track_una,
        track_snowflake,
        track_concentration_version_3,
        track_evil_dub,
        track_ghost_town,
        track_dubby_games,
        track_nightwalker,
    ]
    session.add(medium_1)

    recordingmeta_13 = RecordingMeta()
    session.add(recordingmeta_13)

    recording_moan_feat_ane_trolle = Recording()
    recording_moan_feat_ane_trolle.id = 7134069
    recording_moan_feat_ane_trolle.gid = '6b4bc5f4-ffea-4eb0-971b-cbc130a15519'
    recording_moan_feat_ane_trolle.name = u'Moan (feat. Ane Trolle)'
    recording_moan_feat_ane_trolle.length = 408480
    recording_moan_feat_ane_trolle.comment = u''
    recording_moan_feat_ane_trolle.edits_pending = 0
    recording_moan_feat_ane_trolle.video = False
    recording_moan_feat_ane_trolle.artist_credit = artistcredit_trentemoller
    recording_moan_feat_ane_trolle.meta = recordingmeta_13
    session.add(recording_moan_feat_ane_trolle)

    track_moan_feat_ane_trolle = Track()
    track_moan_feat_ane_trolle.id = 5918643
    track_moan_feat_ane_trolle.gid = '7a8a2335-e701-3fe1-ba15-d8d010b1b7b2'
    track_moan_feat_ane_trolle.position = 1
    track_moan_feat_ane_trolle.number = u'1'
    track_moan_feat_ane_trolle.name = u'Moan (feat. Ane Trolle)'
    track_moan_feat_ane_trolle.length = 408480
    track_moan_feat_ane_trolle.edits_pending = 0
    track_moan_feat_ane_trolle.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_moan_feat_ane_trolle.is_data_track = False
    track_moan_feat_ane_trolle.artist_credit = artistcredit_trentemoller
    track_moan_feat_ane_trolle.recording = recording_moan_feat_ane_trolle
    session.add(track_moan_feat_ane_trolle)

    area_los_angeles = Area()
    area_los_angeles.id = 7703
    area_los_angeles.gid = '1f40c6e1-47ba-4e35-996f-fe6ee5840e62'
    area_los_angeles.name = u'Los Angeles'
    area_los_angeles.edits_pending = 0
    area_los_angeles.last_updated = datetime.datetime(2014, 12, 11, 12, 34, 38, 893537)
    area_los_angeles.ended = False
    area_los_angeles.comment = u''
    area_los_angeles.type = areatype_city
    session.add(area_los_angeles)

    areatype_county = AreaType()
    areatype_county.id = 7
    areatype_county.name = u'County'
    areatype_county.child_order = 7
    areatype_county.description = u'County is used for smaller administrative divisions of a country which are not the main administrative divisions but are also not municipalities, e.g. counties in the USA. These are not considered when displaying the parent areas for a given area.'
    areatype_county.gid = 'bcecec27-8bdb-3e00-8254-d948dda502fa'
    session.add(areatype_county)

    area_los_angeles_county = Area()
    area_los_angeles_county.id = 104685
    area_los_angeles_county.gid = '720f8272-6ba3-48f7-b78e-14cd2641c2cf'
    area_los_angeles_county.name = u'Los Angeles County'
    area_los_angeles_county.edits_pending = 0
    area_los_angeles_county.last_updated = datetime.datetime(2014, 12, 17, 12, 44, 15, 174704)
    area_los_angeles_county.ended = False
    area_los_angeles_county.comment = u''
    area_los_angeles_county.type = areatype_county
    session.add(area_los_angeles_county)

    iso31662_7 = ISO31662()
    iso31662_7.code = u'US-CA'
    session.add(iso31662_7)

    area_california = Area()
    area_california.id = 266
    area_california.gid = 'ae0110b6-13d4-4998-9116-5b926287aa23'
    area_california.name = u'California'
    area_california.edits_pending = 0
    area_california.last_updated = datetime.datetime(2013, 6, 5, 7, 15, 15, 329304)
    area_california.ended = False
    area_california.comment = u''
    area_california.iso_3166_2_codes = [
        iso31662_7,
    ]
    area_california.type = areatype_subdivision
    session.add(area_california)

    linkareaarea_14 = LinkAreaArea()
    linkareaarea_14.id = 6
    linkareaarea_14.edits_pending = 0
    linkareaarea_14.last_updated = datetime.datetime(2013, 5, 17, 20, 8, 33, 220791)
    linkareaarea_14.link_order = 0
    linkareaarea_14.entity0_credit = u''
    linkareaarea_14.entity1_credit = u''
    linkareaarea_14.entity0 = area_united_states
    linkareaarea_14.entity1 = area_california
    linkareaarea_14.link = link_1
    session.add(linkareaarea_14)

    linkareaarea_13 = LinkAreaArea()
    linkareaarea_13.id = 104500
    linkareaarea_13.edits_pending = 0
    linkareaarea_13.last_updated = datetime.datetime(2014, 12, 17, 12, 44, 15, 174704)
    linkareaarea_13.link_order = 0
    linkareaarea_13.entity0_credit = u''
    linkareaarea_13.entity1_credit = u''
    linkareaarea_13.entity0 = area_california
    linkareaarea_13.entity1 = area_los_angeles_county
    linkareaarea_13.link = link_1
    session.add(linkareaarea_13)

    linkareaarea_12 = LinkAreaArea()
    linkareaarea_12.id = 7469
    linkareaarea_12.edits_pending = 0
    linkareaarea_12.last_updated = datetime.datetime(2014, 12, 17, 13, 36, 51, 897737)
    linkareaarea_12.link_order = 0
    linkareaarea_12.entity0_credit = u''
    linkareaarea_12.entity1_credit = u''
    linkareaarea_12.entity0 = area_los_angeles_county
    linkareaarea_12.entity1 = area_los_angeles
    linkareaarea_12.link = link_1
    session.add(linkareaarea_12)

    artistisni_4 = ArtistISNI()
    artistisni_4.isni = u'0000000115160232'
    artistisni_4.edits_pending = 0
    artistisni_4.created = datetime.datetime(2013, 7, 24, 3, 45, 1, 534835)
    session.add(artistisni_4)

    artistmeta_9 = ArtistMeta()
    artistmeta_9.rating = 87
    artistmeta_9.rating_count = 22
    session.add(artistmeta_9)

    artist_the_doors = Artist()
    artist_the_doors.id = 1757
    artist_the_doors.gid = '9efff43b-3b29-4082-824e-bc82f646f93d'
    artist_the_doors.name = u'The Doors'
    artist_the_doors.sort_name = u'Doors, The'
    artist_the_doors.begin_date_year = 1965
    artist_the_doors.end_date_year = 1972
    artist_the_doors.comment = u''
    artist_the_doors.edits_pending = 0
    artist_the_doors.last_updated = datetime.datetime(2013, 7, 24, 3, 45, 1, 534835)
    artist_the_doors.ended = True
    artist_the_doors.area = area_united_states
    artist_the_doors.begin_area = area_los_angeles
    artist_the_doors.isnis = [
        artistisni_4,
    ]
    artist_the_doors.meta = artistmeta_9
    artist_the_doors.type = artisttype_group
    session.add(artist_the_doors)

    artistcreditname_the_doors = ArtistCreditName()
    artistcreditname_the_doors.position = 0
    artistcreditname_the_doors.name = u'The Doors'
    artistcreditname_the_doors.join_phrase = u''
    artistcreditname_the_doors.artist = artist_the_doors
    session.add(artistcreditname_the_doors)

    artistcredit_the_doors = ArtistCredit()
    artistcredit_the_doors.id = 1757
    artistcredit_the_doors.name = u'The Doors'
    artistcredit_the_doors.artist_count = 1
    artistcredit_the_doors.ref_count = 9763
    artistcredit_the_doors.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_the_doors.artists = [
        artistcreditname_the_doors,
    ]
    session.add(artistcredit_the_doors)

    recordingmeta_14 = RecordingMeta()
    session.add(recordingmeta_14)

    recording_break_on_through_dark_ride_dub_mix = Recording()
    recording_break_on_through_dark_ride_dub_mix.id = 7134070
    recording_break_on_through_dark_ride_dub_mix.gid = '910552ed-94ed-48f9-b87f-7133d4e546fa'
    recording_break_on_through_dark_ride_dub_mix.name = u'Break on Through (Dark Ride dub mix)'
    recording_break_on_through_dark_ride_dub_mix.length = 288960
    recording_break_on_through_dark_ride_dub_mix.comment = u''
    recording_break_on_through_dark_ride_dub_mix.edits_pending = 0
    recording_break_on_through_dark_ride_dub_mix.video = False
    recording_break_on_through_dark_ride_dub_mix.artist_credit = artistcredit_the_doors
    recording_break_on_through_dark_ride_dub_mix.meta = recordingmeta_14
    session.add(recording_break_on_through_dark_ride_dub_mix)

    track_break_on_through_dark_ride_dub_mix = Track()
    track_break_on_through_dark_ride_dub_mix.id = 5918644
    track_break_on_through_dark_ride_dub_mix.gid = '28a5b0cb-265e-3ad7-b300-4a39867640a4'
    track_break_on_through_dark_ride_dub_mix.position = 2
    track_break_on_through_dark_ride_dub_mix.number = u'2'
    track_break_on_through_dark_ride_dub_mix.name = u'Break on Through (Dark Ride dub mix)'
    track_break_on_through_dark_ride_dub_mix.length = 288960
    track_break_on_through_dark_ride_dub_mix.edits_pending = 0
    track_break_on_through_dark_ride_dub_mix.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_break_on_through_dark_ride_dub_mix.is_data_track = False
    track_break_on_through_dark_ride_dub_mix.artist_credit = artistcredit_the_doors
    track_break_on_through_dark_ride_dub_mix.recording = recording_break_on_through_dark_ride_dub_mix
    session.add(track_break_on_through_dark_ride_dub_mix)

    iso31662_8 = ISO31662()
    iso31662_8.code = u'GB-GLG'
    session.add(iso31662_8)

    area_glasgow = Area()
    area_glasgow.id = 3855
    area_glasgow.gid = 'c279f805-01f8-46f5-99cf-51f165a1adad'
    area_glasgow.name = u'Glasgow'
    area_glasgow.edits_pending = 0
    area_glasgow.last_updated = datetime.datetime(2013, 5, 24, 0, 2, 38, 336242)
    area_glasgow.ended = False
    area_glasgow.comment = u''
    area_glasgow.iso_3166_2_codes = [
        iso31662_8,
    ]
    area_glasgow.type = areatype_city
    session.add(area_glasgow)

    iso31662_9 = ISO31662()
    iso31662_9.code = u'GB-SCT'
    session.add(iso31662_9)

    area_scotland = Area()
    area_scotland.id = 434
    area_scotland.gid = '6fa1c7da-6689-4cec-85f9-680f853e8a08'
    area_scotland.name = u'Scotland'
    area_scotland.edits_pending = 0
    area_scotland.last_updated = datetime.datetime(2013, 5, 18, 0, 12, 35, 79349)
    area_scotland.ended = False
    area_scotland.comment = u''
    area_scotland.iso_3166_2_codes = [
        iso31662_9,
    ]
    area_scotland.type = areatype_subdivision
    session.add(area_scotland)

    linkareaarea_16 = LinkAreaArea()
    linkareaarea_16.id = 175
    linkareaarea_16.edits_pending = 0
    linkareaarea_16.last_updated = datetime.datetime(2013, 5, 18, 0, 12, 45, 164066)
    linkareaarea_16.link_order = 0
    linkareaarea_16.entity0_credit = u''
    linkareaarea_16.entity1_credit = u''
    linkareaarea_16.entity0 = area_united_kingdom
    linkareaarea_16.entity1 = area_scotland
    linkareaarea_16.link = link_1
    session.add(linkareaarea_16)

    linkareaarea_15 = LinkAreaArea()
    linkareaarea_15.id = 3621
    linkareaarea_15.edits_pending = 0
    linkareaarea_15.last_updated = datetime.datetime(2013, 5, 21, 14, 42, 19, 310319)
    linkareaarea_15.link_order = 0
    linkareaarea_15.entity0_credit = u''
    linkareaarea_15.entity1_credit = u''
    linkareaarea_15.entity0 = area_scotland
    linkareaarea_15.entity1 = area_glasgow
    linkareaarea_15.link = link_1
    session.add(linkareaarea_15)

    artistmeta_10 = ArtistMeta()
    artistmeta_10.rating = 87
    artistmeta_10.rating_count = 11
    session.add(artistmeta_10)

    artist_franz_ferdinand = Artist()
    artist_franz_ferdinand.id = 117968
    artist_franz_ferdinand.gid = 'aa7a2827-f74b-473c-bd79-03d065835cf7'
    artist_franz_ferdinand.name = u'Franz Ferdinand'
    artist_franz_ferdinand.sort_name = u'Franz Ferdinand'
    artist_franz_ferdinand.begin_date_year = 2001
    artist_franz_ferdinand.comment = u''
    artist_franz_ferdinand.edits_pending = 0
    artist_franz_ferdinand.last_updated = datetime.datetime(2015, 6, 17, 23, 3, 9, 772278)
    artist_franz_ferdinand.ended = False
    artist_franz_ferdinand.area = area_united_kingdom
    artist_franz_ferdinand.begin_area = area_glasgow
    artist_franz_ferdinand.meta = artistmeta_10
    artist_franz_ferdinand.type = artisttype_group
    session.add(artist_franz_ferdinand)

    artistcreditname_franz_ferdinand = ArtistCreditName()
    artistcreditname_franz_ferdinand.position = 0
    artistcreditname_franz_ferdinand.name = u'Franz Ferdinand'
    artistcreditname_franz_ferdinand.join_phrase = u''
    artistcreditname_franz_ferdinand.artist = artist_franz_ferdinand
    session.add(artistcreditname_franz_ferdinand)

    artistcredit_franz_ferdinand = ArtistCredit()
    artistcredit_franz_ferdinand.id = 117968
    artistcredit_franz_ferdinand.name = u'Franz Ferdinand'
    artistcredit_franz_ferdinand.artist_count = 1
    artistcredit_franz_ferdinand.ref_count = 2236
    artistcredit_franz_ferdinand.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_franz_ferdinand.artists = [
        artistcreditname_franz_ferdinand,
    ]
    session.add(artistcredit_franz_ferdinand)

    recordingmeta_15 = RecordingMeta()
    session.add(recordingmeta_15)

    recording_the_fallen_justice_remix = Recording()
    recording_the_fallen_justice_remix.id = 7134071
    recording_the_fallen_justice_remix.gid = 'f0e7f5e3-a59f-4f46-b828-e6dcaca5638a'
    recording_the_fallen_justice_remix.name = u'The Fallen (Justice remix)'
    recording_the_fallen_justice_remix.length = 97973
    recording_the_fallen_justice_remix.comment = u''
    recording_the_fallen_justice_remix.edits_pending = 0
    recording_the_fallen_justice_remix.video = False
    recording_the_fallen_justice_remix.artist_credit = artistcredit_franz_ferdinand
    recording_the_fallen_justice_remix.meta = recordingmeta_15
    session.add(recording_the_fallen_justice_remix)

    workmeta_2 = WorkMeta()
    session.add(workmeta_2)

    work_the_fallen = Work()
    work_the_fallen.id = 6688572
    work_the_fallen.gid = '30524491-df69-3678-aa67-64c5da804d93'
    work_the_fallen.name = u'The Fallen'
    work_the_fallen.comment = u''
    work_the_fallen.edits_pending = 0
    work_the_fallen.last_updated = datetime.datetime(2011, 7, 26, 8, 0, 16, 808255)
    work_the_fallen.meta = workmeta_2
    session.add(work_the_fallen)

    area_almondsbury = Area()
    area_almondsbury.id = 116461
    area_almondsbury.gid = '64e96c0b-57b6-4038-bbd6-7b87cf4ac263'
    area_almondsbury.name = u'Almondsbury'
    area_almondsbury.edits_pending = 0
    area_almondsbury.last_updated = datetime.datetime(2016, 6, 25, 22, 10, 34, 192389)
    area_almondsbury.ended = False
    area_almondsbury.comment = u''
    area_almondsbury.type = areatype_city
    session.add(area_almondsbury)

    iso31662_10 = ISO31662()
    iso31662_10.code = u'GB-SGC'
    session.add(iso31662_10)

    area_south_gloucestershire = Area()
    area_south_gloucestershire.id = 3990
    area_south_gloucestershire.gid = '1ab3c66d-f4e6-4663-b2da-5699c2ebd4cd'
    area_south_gloucestershire.name = u'South Gloucestershire'
    area_south_gloucestershire.edits_pending = 0
    area_south_gloucestershire.last_updated = datetime.datetime(2013, 5, 21, 15, 8, 50, 857583)
    area_south_gloucestershire.ended = False
    area_south_gloucestershire.comment = u''
    area_south_gloucestershire.iso_3166_2_codes = [
        iso31662_10,
    ]
    area_south_gloucestershire.type = areatype_subdivision
    session.add(area_south_gloucestershire)

    linkareaarea_18 = LinkAreaArea()
    linkareaarea_18.id = 3756
    linkareaarea_18.edits_pending = 0
    linkareaarea_18.last_updated = datetime.datetime(2013, 5, 21, 15, 9, 2, 381572)
    linkareaarea_18.link_order = 0
    linkareaarea_18.entity0_credit = u''
    linkareaarea_18.entity1_credit = u''
    linkareaarea_18.entity0 = area_england
    linkareaarea_18.entity1 = area_south_gloucestershire
    linkareaarea_18.link = link_1
    session.add(linkareaarea_18)

    linkareaarea_17 = LinkAreaArea()
    linkareaarea_17.id = 116323
    linkareaarea_17.edits_pending = 0
    linkareaarea_17.last_updated = datetime.datetime(2016, 6, 25, 22, 10, 34, 192389)
    linkareaarea_17.link_order = 0
    linkareaarea_17.entity0_credit = u''
    linkareaarea_17.entity1_credit = u''
    linkareaarea_17.entity0 = area_south_gloucestershire
    linkareaarea_17.entity1 = area_almondsbury
    linkareaarea_17.link = link_1
    session.add(linkareaarea_17)

    artistipi_5 = ArtistIPI()
    artistipi_5.ipi = u'00267327940'
    artistipi_5.edits_pending = 0
    artistipi_5.created = datetime.datetime(2013, 5, 6, 6, 0, 14, 518494)
    session.add(artistipi_5)

    artistisni_5 = ArtistISNI()
    artistisni_5.isni = u'0000000120173767'
    artistisni_5.edits_pending = 0
    artistisni_5.created = datetime.datetime(2016, 6, 25, 22, 13, 20, 254336)
    session.add(artistisni_5)

    artistmeta_11 = ArtistMeta()
    session.add(artistmeta_11)

    artist_alex_kapranos = Artist()
    artist_alex_kapranos.id = 314063
    artist_alex_kapranos.gid = '262b08bd-539c-43b4-9dbf-1d85d25e79b8'
    artist_alex_kapranos.name = u'Alex Kapranos'
    artist_alex_kapranos.sort_name = u'Kapranos, Alex'
    artist_alex_kapranos.begin_date_year = 1972
    artist_alex_kapranos.begin_date_month = 3
    artist_alex_kapranos.begin_date_day = 20
    artist_alex_kapranos.comment = u''
    artist_alex_kapranos.edits_pending = 0
    artist_alex_kapranos.last_updated = datetime.datetime(2016, 6, 27, 23, 1, 16, 122028)
    artist_alex_kapranos.ended = False
    artist_alex_kapranos.area = area_united_kingdom
    artist_alex_kapranos.begin_area = area_almondsbury
    artist_alex_kapranos.gender = gender_male
    artist_alex_kapranos.ipis = [
        artistipi_5,
    ]
    artist_alex_kapranos.isnis = [
        artistisni_5,
    ]
    artist_alex_kapranos.meta = artistmeta_11
    artist_alex_kapranos.type = artisttype_person
    session.add(artist_alex_kapranos)

    linkartistwork_3 = LinkArtistWork()
    linkartistwork_3.id = 566019
    linkartistwork_3.edits_pending = 0
    linkartistwork_3.last_updated = datetime.datetime(2016, 6, 27, 23, 1, 16, 122028)
    linkartistwork_3.link_order = 0
    linkartistwork_3.entity0_credit = u''
    linkartistwork_3.entity1_credit = u''
    linkartistwork_3.entity0 = artist_alex_kapranos
    linkartistwork_3.entity1 = work_the_fallen
    linkartistwork_3.link = link_2
    session.add(linkartistwork_3)

    linkartistwork_4 = LinkArtistWork()
    linkartistwork_4.id = 566017
    linkartistwork_4.edits_pending = 0
    linkartistwork_4.last_updated = datetime.datetime(2016, 6, 27, 23, 1, 16, 122028)
    linkartistwork_4.link_order = 0
    linkartistwork_4.entity0_credit = u''
    linkartistwork_4.entity1_credit = u''
    linkartistwork_4.entity0 = artist_alex_kapranos
    linkartistwork_4.entity1 = work_the_fallen
    linkartistwork_4.link = link_3
    session.add(linkartistwork_4)

    iso31662_11 = ISO31662()
    iso31662_11.code = u'GB-BPL'
    session.add(iso31662_11)

    area_blackpool = Area()
    area_blackpool.id = 3804
    area_blackpool.gid = '75aace97-0d87-4f8d-841a-095c85052581'
    area_blackpool.name = u'Blackpool'
    area_blackpool.edits_pending = 0
    area_blackpool.last_updated = datetime.datetime(2013, 6, 5, 6, 37, 0, 287904)
    area_blackpool.ended = False
    area_blackpool.comment = u''
    area_blackpool.iso_3166_2_codes = [
        iso31662_11,
    ]
    area_blackpool.type = areatype_subdivision
    session.add(area_blackpool)

    iso31662_12 = ISO31662()
    iso31662_12.code = u'GB-LAN'
    session.add(iso31662_12)

    area_lancashire = Area()
    area_lancashire.id = 3869
    area_lancashire.gid = '5c6f4550-e4ae-4570-99c9-dc133582d1aa'
    area_lancashire.name = u'Lancashire'
    area_lancashire.edits_pending = 0
    area_lancashire.last_updated = datetime.datetime(2013, 5, 21, 14, 44, 42, 600182)
    area_lancashire.ended = False
    area_lancashire.comment = u''
    area_lancashire.iso_3166_2_codes = [
        iso31662_12,
    ]
    area_lancashire.type = areatype_subdivision
    session.add(area_lancashire)

    linkareaarea_20 = LinkAreaArea()
    linkareaarea_20.id = 3635
    linkareaarea_20.edits_pending = 0
    linkareaarea_20.last_updated = datetime.datetime(2013, 5, 21, 14, 44, 51, 102922)
    linkareaarea_20.link_order = 0
    linkareaarea_20.entity0_credit = u''
    linkareaarea_20.entity1_credit = u''
    linkareaarea_20.entity0 = area_england
    linkareaarea_20.entity1 = area_lancashire
    linkareaarea_20.link = link_1
    session.add(linkareaarea_20)

    linkareaarea_19 = LinkAreaArea()
    linkareaarea_19.id = 3570
    linkareaarea_19.edits_pending = 0
    linkareaarea_19.last_updated = datetime.datetime(2015, 12, 4, 21, 4, 29, 825613)
    linkareaarea_19.link_order = 0
    linkareaarea_19.entity0_credit = u''
    linkareaarea_19.entity1_credit = u''
    linkareaarea_19.entity0 = area_lancashire
    linkareaarea_19.entity1 = area_blackpool
    linkareaarea_19.link = link_1
    session.add(linkareaarea_19)

    artistipi_6 = ArtistIPI()
    artistipi_6.ipi = u'00443131398'
    artistipi_6.edits_pending = 0
    artistipi_6.created = datetime.datetime(2013, 5, 6, 6, 0, 14, 566553)
    session.add(artistipi_6)

    artistisni_6 = ArtistISNI()
    artistisni_6.isni = u'0000000131149236'
    artistisni_6.edits_pending = 0
    artistisni_6.created = datetime.datetime(2016, 1, 22, 20, 9, 49, 103129)
    session.add(artistisni_6)

    artistmeta_12 = ArtistMeta()
    session.add(artistmeta_12)

    artist_nicholas_mccarthy = Artist()
    artist_nicholas_mccarthy.id = 314075
    artist_nicholas_mccarthy.gid = 'deaf2729-cc2b-4a84-8acb-0cea2e5fee49'
    artist_nicholas_mccarthy.name = u'Nicholas McCarthy'
    artist_nicholas_mccarthy.sort_name = u'McCarthy, Nicholas'
    artist_nicholas_mccarthy.begin_date_year = 1974
    artist_nicholas_mccarthy.begin_date_month = 12
    artist_nicholas_mccarthy.begin_date_day = 13
    artist_nicholas_mccarthy.comment = u''
    artist_nicholas_mccarthy.edits_pending = 0
    artist_nicholas_mccarthy.last_updated = datetime.datetime(2016, 1, 22, 20, 9, 49, 103129)
    artist_nicholas_mccarthy.ended = False
    artist_nicholas_mccarthy.area = area_united_kingdom
    artist_nicholas_mccarthy.begin_area = area_blackpool
    artist_nicholas_mccarthy.gender = gender_male
    artist_nicholas_mccarthy.ipis = [
        artistipi_6,
    ]
    artist_nicholas_mccarthy.isnis = [
        artistisni_6,
    ]
    artist_nicholas_mccarthy.meta = artistmeta_12
    artist_nicholas_mccarthy.type = artisttype_person
    session.add(artist_nicholas_mccarthy)

    linkartistwork_5 = LinkArtistWork()
    linkartistwork_5.id = 566039
    linkartistwork_5.edits_pending = 0
    linkartistwork_5.last_updated = datetime.datetime(2012, 7, 24, 12, 16, 17, 271740)
    linkartistwork_5.link_order = 0
    linkartistwork_5.entity0_credit = u''
    linkartistwork_5.entity1_credit = u''
    linkartistwork_5.entity0 = artist_nicholas_mccarthy
    linkartistwork_5.entity1 = work_the_fallen
    linkartistwork_5.link = link_3
    session.add(linkartistwork_5)

    linkartistwork_6 = LinkArtistWork()
    linkartistwork_6.id = 566040
    linkartistwork_6.edits_pending = 0
    linkartistwork_6.last_updated = datetime.datetime(2012, 7, 24, 12, 16, 18, 812026)
    linkartistwork_6.link_order = 0
    linkartistwork_6.entity0_credit = u''
    linkartistwork_6.entity1_credit = u''
    linkartistwork_6.entity0 = artist_nicholas_mccarthy
    linkartistwork_6.entity1 = work_the_fallen
    linkartistwork_6.link = link_2
    session.add(linkartistwork_6)

    artistipi_7 = ArtistIPI()
    artistipi_7.ipi = u'00448626528'
    artistipi_7.edits_pending = 0
    artistipi_7.created = datetime.datetime(2013, 5, 6, 6, 0, 14, 540367)
    session.add(artistipi_7)

    artistmeta_13 = ArtistMeta()
    session.add(artistmeta_13)

    artist_robert_hardy = Artist()
    artist_robert_hardy.id = 314073
    artist_robert_hardy.gid = '6797e740-b6a5-4019-9369-dd49e1381ff6'
    artist_robert_hardy.name = u'Robert Hardy'
    artist_robert_hardy.sort_name = u'Hardy, Robert'
    artist_robert_hardy.begin_date_year = 1980
    artist_robert_hardy.begin_date_month = 8
    artist_robert_hardy.begin_date_day = 16
    artist_robert_hardy.comment = u'bassist for Franz Ferdinand'
    artist_robert_hardy.edits_pending = 0
    artist_robert_hardy.last_updated = datetime.datetime(2015, 3, 17, 9, 47, 35, 410044)
    artist_robert_hardy.ended = False
    artist_robert_hardy.area = area_united_kingdom
    artist_robert_hardy.gender = gender_male
    artist_robert_hardy.ipis = [
        artistipi_7,
    ]
    artist_robert_hardy.meta = artistmeta_13
    artist_robert_hardy.type = artisttype_person
    session.add(artist_robert_hardy)

    linkartistwork_7 = LinkArtistWork()
    linkartistwork_7.id = 566061
    linkartistwork_7.edits_pending = 0
    linkartistwork_7.last_updated = datetime.datetime(2012, 7, 24, 12, 17, 14, 846711)
    linkartistwork_7.link_order = 0
    linkartistwork_7.entity0_credit = u''
    linkartistwork_7.entity1_credit = u''
    linkartistwork_7.entity0 = artist_robert_hardy
    linkartistwork_7.entity1 = work_the_fallen
    linkartistwork_7.link = link_3
    session.add(linkartistwork_7)

    linkartistwork_8 = LinkArtistWork()
    linkartistwork_8.id = 566062
    linkartistwork_8.edits_pending = 0
    linkartistwork_8.last_updated = datetime.datetime(2012, 7, 24, 12, 17, 16, 351483)
    linkartistwork_8.link_order = 0
    linkartistwork_8.entity0_credit = u''
    linkartistwork_8.entity1_credit = u''
    linkartistwork_8.entity0 = artist_robert_hardy
    linkartistwork_8.entity1 = work_the_fallen
    linkartistwork_8.link = link_2
    session.add(linkartistwork_8)

    artistipi_8 = ArtistIPI()
    artistipi_8.ipi = u'00448625825'
    artistipi_8.edits_pending = 0
    artistipi_8.created = datetime.datetime(2013, 5, 6, 6, 0, 14, 475190)
    session.add(artistipi_8)

    artistmeta_14 = ArtistMeta()
    session.add(artistmeta_14)

    artist_paul_thomson = Artist()
    artist_paul_thomson.id = 314064
    artist_paul_thomson.gid = '72ee22fc-938b-45f8-8e9f-8870d7639805'
    artist_paul_thomson.name = u'Paul Thomson'
    artist_paul_thomson.sort_name = u'Thomson, Paul'
    artist_paul_thomson.begin_date_year = 1976
    artist_paul_thomson.begin_date_month = 9
    artist_paul_thomson.begin_date_day = 15
    artist_paul_thomson.comment = u''
    artist_paul_thomson.edits_pending = 0
    artist_paul_thomson.last_updated = datetime.datetime(2014, 1, 18, 1, 0, 19, 602124)
    artist_paul_thomson.ended = False
    artist_paul_thomson.area = area_united_kingdom
    artist_paul_thomson.gender = gender_male
    artist_paul_thomson.ipis = [
        artistipi_8,
    ]
    artist_paul_thomson.meta = artistmeta_14
    artist_paul_thomson.type = artisttype_person
    session.add(artist_paul_thomson)

    linkartistwork_9 = LinkArtistWork()
    linkartistwork_9.id = 566083
    linkartistwork_9.edits_pending = 0
    linkartistwork_9.last_updated = datetime.datetime(2012, 7, 24, 12, 18, 12, 318295)
    linkartistwork_9.link_order = 0
    linkartistwork_9.entity0_credit = u''
    linkartistwork_9.entity1_credit = u''
    linkartistwork_9.entity0 = artist_paul_thomson
    linkartistwork_9.entity1 = work_the_fallen
    linkartistwork_9.link = link_3
    session.add(linkartistwork_9)

    linkartistwork_10 = LinkArtistWork()
    linkartistwork_10.id = 566084
    linkartistwork_10.edits_pending = 0
    linkartistwork_10.last_updated = datetime.datetime(2012, 7, 24, 12, 18, 13, 558797)
    linkartistwork_10.link_order = 0
    linkartistwork_10.entity0_credit = u''
    linkartistwork_10.entity1_credit = u''
    linkartistwork_10.entity0 = artist_paul_thomson
    linkartistwork_10.entity1 = work_the_fallen
    linkartistwork_10.link = link_2
    session.add(linkartistwork_10)

    linkrecordingwork_2 = LinkRecordingWork()
    linkrecordingwork_2.id = 705613
    linkrecordingwork_2.edits_pending = 0
    linkrecordingwork_2.last_updated = datetime.datetime(2012, 9, 15, 15, 32, 53, 774726)
    linkrecordingwork_2.link_order = 0
    linkrecordingwork_2.entity0_credit = u''
    linkrecordingwork_2.entity1_credit = u''
    linkrecordingwork_2.entity0 = recording_the_fallen_justice_remix
    linkrecordingwork_2.entity1 = work_the_fallen
    linkrecordingwork_2.link = link_6
    session.add(linkrecordingwork_2)

    track_the_fallen_justice_remix = Track()
    track_the_fallen_justice_remix.id = 5918645
    track_the_fallen_justice_remix.gid = '0291a4dd-f5c0-3fce-aea0-516755e75a1f'
    track_the_fallen_justice_remix.position = 3
    track_the_fallen_justice_remix.number = u'3'
    track_the_fallen_justice_remix.name = u'The Fallen (Justice remix)'
    track_the_fallen_justice_remix.length = 97973
    track_the_fallen_justice_remix.edits_pending = 0
    track_the_fallen_justice_remix.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_the_fallen_justice_remix.is_data_track = False
    track_the_fallen_justice_remix.artist_credit = artistcredit_franz_ferdinand
    track_the_fallen_justice_remix.recording = recording_the_fallen_justice_remix
    session.add(track_the_fallen_justice_remix)

    area_new_york_1 = Area()
    area_new_york_1.id = 7020
    area_new_york_1.gid = '74e50e58-5deb-4b99-93a2-decbb365c07f'
    area_new_york_1.name = u'New York'
    area_new_york_1.edits_pending = 0
    area_new_york_1.last_updated = datetime.datetime(2014, 12, 2, 22, 23, 17, 690134)
    area_new_york_1.ended = False
    area_new_york_1.comment = u''
    area_new_york_1.type = areatype_city
    session.add(area_new_york_1)

    linkareaarea_21 = LinkAreaArea()
    linkareaarea_21.id = 6786
    linkareaarea_21.edits_pending = 0
    linkareaarea_21.last_updated = datetime.datetime(2013, 5, 26, 12, 1, 42, 787582)
    linkareaarea_21.link_order = 0
    linkareaarea_21.entity0_credit = u''
    linkareaarea_21.entity1_credit = u''
    linkareaarea_21.entity0 = area_new_york
    linkareaarea_21.entity1 = area_new_york_1
    linkareaarea_21.link = link_1
    session.add(linkareaarea_21)

    artistmeta_15 = ArtistMeta()
    session.add(artistmeta_15)

    artist_le_tigre = Artist()
    artist_le_tigre.id = 51
    artist_le_tigre.gid = '2d67239c-aa40-4ad5-a807-9052b66857a6'
    artist_le_tigre.name = u'Le Tigre'
    artist_le_tigre.sort_name = u'Tigre, Le'
    artist_le_tigre.begin_date_year = 1998
    artist_le_tigre.comment = u''
    artist_le_tigre.edits_pending = 0
    artist_le_tigre.last_updated = datetime.datetime(2013, 7, 26, 9, 14, 16, 631116)
    artist_le_tigre.ended = False
    artist_le_tigre.area = area_united_states
    artist_le_tigre.begin_area = area_new_york_1
    artist_le_tigre.meta = artistmeta_15
    artist_le_tigre.type = artisttype_group
    session.add(artist_le_tigre)

    artistcreditname_le_tigre = ArtistCreditName()
    artistcreditname_le_tigre.position = 0
    artistcreditname_le_tigre.name = u'Le Tigre'
    artistcreditname_le_tigre.join_phrase = u''
    artistcreditname_le_tigre.artist = artist_le_tigre
    session.add(artistcreditname_le_tigre)

    artistcredit_le_tigre = ArtistCredit()
    artistcredit_le_tigre.id = 51
    artistcredit_le_tigre.name = u'Le Tigre'
    artistcredit_le_tigre.artist_count = 1
    artistcredit_le_tigre.ref_count = 397
    artistcredit_le_tigre.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_le_tigre.artists = [
        artistcreditname_le_tigre,
    ]
    session.add(artistcredit_le_tigre)

    recordingmeta_16 = RecordingMeta()
    session.add(recordingmeta_16)

    recording_nanny_nanny_boo_boo_junior_senior_remix = Recording()
    recording_nanny_nanny_boo_boo_junior_senior_remix.id = 7134072
    recording_nanny_nanny_boo_boo_junior_senior_remix.gid = '483dc8c2-93d6-4a3c-a07a-3a2244e7e343'
    recording_nanny_nanny_boo_boo_junior_senior_remix.name = u'Nanny Nanny Boo Boo (Junior Senior remix)'
    recording_nanny_nanny_boo_boo_junior_senior_remix.length = 149506
    recording_nanny_nanny_boo_boo_junior_senior_remix.comment = u''
    recording_nanny_nanny_boo_boo_junior_senior_remix.edits_pending = 0
    recording_nanny_nanny_boo_boo_junior_senior_remix.video = False
    recording_nanny_nanny_boo_boo_junior_senior_remix.artist_credit = artistcredit_le_tigre
    recording_nanny_nanny_boo_boo_junior_senior_remix.meta = recordingmeta_16
    session.add(recording_nanny_nanny_boo_boo_junior_senior_remix)

    track_nanny_nanny_boo_boo_junior_senior_remix = Track()
    track_nanny_nanny_boo_boo_junior_senior_remix.id = 5918646
    track_nanny_nanny_boo_boo_junior_senior_remix.gid = '25a57cd3-77ce-39d6-952c-d3b91a5e59dc'
    track_nanny_nanny_boo_boo_junior_senior_remix.position = 4
    track_nanny_nanny_boo_boo_junior_senior_remix.number = u'4'
    track_nanny_nanny_boo_boo_junior_senior_remix.name = u'Nanny Nanny Boo Boo (Junior Senior remix)'
    track_nanny_nanny_boo_boo_junior_senior_remix.length = 149506
    track_nanny_nanny_boo_boo_junior_senior_remix.edits_pending = 0
    track_nanny_nanny_boo_boo_junior_senior_remix.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_nanny_nanny_boo_boo_junior_senior_remix.is_data_track = False
    track_nanny_nanny_boo_boo_junior_senior_remix.artist_credit = artistcredit_le_tigre
    track_nanny_nanny_boo_boo_junior_senior_remix.recording = recording_nanny_nanny_boo_boo_junior_senior_remix
    session.add(track_nanny_nanny_boo_boo_junior_senior_remix)

    artistmeta_16 = ArtistMeta()
    session.add(artistmeta_16)

    artist_james_white_and_the_blacks = Artist()
    artist_james_white_and_the_blacks.id = 107002
    artist_james_white_and_the_blacks.gid = '4e303fcf-0f7e-42f4-b84e-454a7922e725'
    artist_james_white_and_the_blacks.name = u'James White and The Blacks'
    artist_james_white_and_the_blacks.sort_name = u'White, James and The Blacks'
    artist_james_white_and_the_blacks.comment = u''
    artist_james_white_and_the_blacks.edits_pending = 0
    artist_james_white_and_the_blacks.last_updated = datetime.datetime(2010, 7, 25, 4, 44, 13, 723447)
    artist_james_white_and_the_blacks.ended = False
    artist_james_white_and_the_blacks.meta = artistmeta_16
    artist_james_white_and_the_blacks.type = artisttype_group
    session.add(artist_james_white_and_the_blacks)

    artistcreditname_james_white_and_the_blacks = ArtistCreditName()
    artistcreditname_james_white_and_the_blacks.position = 0
    artistcreditname_james_white_and_the_blacks.name = u'James White and The Blacks'
    artistcreditname_james_white_and_the_blacks.join_phrase = u''
    artistcreditname_james_white_and_the_blacks.artist = artist_james_white_and_the_blacks
    session.add(artistcreditname_james_white_and_the_blacks)

    artistcredit_james_white_and_the_blacks = ArtistCredit()
    artistcredit_james_white_and_the_blacks.id = 107002
    artistcredit_james_white_and_the_blacks.name = u'James White and The Blacks'
    artistcredit_james_white_and_the_blacks.artist_count = 1
    artistcredit_james_white_and_the_blacks.ref_count = 142
    artistcredit_james_white_and_the_blacks.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_james_white_and_the_blacks.artists = [
        artistcreditname_james_white_and_the_blacks,
    ]
    session.add(artistcredit_james_white_and_the_blacks)

    recordingmeta_17 = RecordingMeta()
    session.add(recordingmeta_17)

    recording_contort_yourself = Recording()
    recording_contort_yourself.id = 7134073
    recording_contort_yourself.gid = '3af60ae0-abf9-41b1-971c-e1560441410d'
    recording_contort_yourself.name = u'Contort Yourself'
    recording_contort_yourself.length = 153226
    recording_contort_yourself.comment = u''
    recording_contort_yourself.edits_pending = 0
    recording_contort_yourself.video = False
    recording_contort_yourself.artist_credit = artistcredit_james_white_and_the_blacks
    recording_contort_yourself.meta = recordingmeta_17
    session.add(recording_contort_yourself)

    track_contort_yourself = Track()
    track_contort_yourself.id = 5918647
    track_contort_yourself.gid = '2fe80875-51a9-3a60-a253-0b99d3dc5edf'
    track_contort_yourself.position = 5
    track_contort_yourself.number = u'5'
    track_contort_yourself.name = u'Contort Yourself'
    track_contort_yourself.length = 153226
    track_contort_yourself.edits_pending = 0
    track_contort_yourself.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_contort_yourself.is_data_track = False
    track_contort_yourself.artist_credit = artistcredit_james_white_and_the_blacks
    track_contort_yourself.recording = recording_contort_yourself
    session.add(track_contort_yourself)

    iso31661_7 = ISO31661()
    iso31661_7.code = u'SE'
    session.add(iso31661_7)

    area_sweden = Area()
    area_sweden.id = 202
    area_sweden.gid = '23d10872-f5ae-3f0c-bf55-332788a16ecb'
    area_sweden.name = u'Sweden'
    area_sweden.edits_pending = 0
    area_sweden.last_updated = datetime.datetime(2013, 5, 27, 13, 49, 3, 298388)
    area_sweden.ended = False
    area_sweden.comment = u''
    area_sweden.iso_3166_1_codes = [
        iso31661_7,
    ]
    area_sweden.type = areatype_country
    session.add(area_sweden)

    artistmeta_17 = ArtistMeta()
    session.add(artistmeta_17)

    artist_revl9n = Artist()
    artist_revl9n.id = 226950
    artist_revl9n.gid = 'f07c698b-f559-4dd0-a65b-b7fddd30355b'
    artist_revl9n.name = u'Revl9n'
    artist_revl9n.sort_name = u'Revl9n'
    artist_revl9n.comment = u''
    artist_revl9n.edits_pending = 0
    artist_revl9n.last_updated = datetime.datetime(2011, 12, 6, 20, 27, 11, 764329)
    artist_revl9n.ended = False
    artist_revl9n.area = area_sweden
    artist_revl9n.meta = artistmeta_17
    artist_revl9n.type = artisttype_group
    session.add(artist_revl9n)

    artistcreditname_revl9n = ArtistCreditName()
    artistcreditname_revl9n.position = 0
    artistcreditname_revl9n.name = u'Revl9n'
    artistcreditname_revl9n.join_phrase = u''
    artistcreditname_revl9n.artist = artist_revl9n
    session.add(artistcreditname_revl9n)

    artistcredit_revl9n = ArtistCredit()
    artistcredit_revl9n.id = 226950
    artistcredit_revl9n.name = u'Revl9n'
    artistcredit_revl9n.artist_count = 1
    artistcredit_revl9n.ref_count = 96
    artistcredit_revl9n.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_revl9n.artists = [
        artistcreditname_revl9n,
    ]
    session.add(artistcredit_revl9n)

    recordingmeta_18 = RecordingMeta()
    session.add(recordingmeta_18)

    recording_someone_like_you = Recording()
    recording_someone_like_you.id = 7134074
    recording_someone_like_you.gid = 'cd25d8ee-9cbd-40c7-891c-9dc68384e335'
    recording_someone_like_you.name = u'Someone Like You'
    recording_someone_like_you.length = 149373
    recording_someone_like_you.comment = u''
    recording_someone_like_you.edits_pending = 0
    recording_someone_like_you.video = False
    recording_someone_like_you.artist_credit = artistcredit_revl9n
    recording_someone_like_you.meta = recordingmeta_18
    session.add(recording_someone_like_you)

    track_someone_like_you = Track()
    track_someone_like_you.id = 5918648
    track_someone_like_you.gid = '755abf8b-337f-3558-97e5-910ec05028c3'
    track_someone_like_you.position = 6
    track_someone_like_you.number = u'6'
    track_someone_like_you.name = u'Someone Like You'
    track_someone_like_you.length = 149373
    track_someone_like_you.edits_pending = 0
    track_someone_like_you.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_someone_like_you.is_data_track = False
    track_someone_like_you.artist_credit = artistcredit_revl9n
    track_someone_like_you.recording = recording_someone_like_you
    session.add(track_someone_like_you)

    iso31661_8 = ISO31661()
    iso31661_8.code = u'DE'
    session.add(iso31661_8)

    area_germany = Area()
    area_germany.id = 81
    area_germany.gid = '85752fda-13c4-31a3-bee5-0e5cb1f51dad'
    area_germany.name = u'Germany'
    area_germany.edits_pending = 0
    area_germany.last_updated = datetime.datetime(2013, 5, 27, 12, 44, 37, 529747)
    area_germany.ended = False
    area_germany.comment = u''
    area_germany.iso_3166_1_codes = [
        iso31661_8,
    ]
    area_germany.type = areatype_country
    session.add(area_germany)

    iso31662_13 = ISO31662()
    iso31662_13.code = u'DE-BE'
    session.add(iso31662_13)

    area_berlin = Area()
    area_berlin.id = 326
    area_berlin.gid = 'c9ac1239-e832-41bc-9930-e252a1fd1105'
    area_berlin.name = u'Berlin'
    area_berlin.edits_pending = 0
    area_berlin.last_updated = datetime.datetime(2013, 11, 26, 5, 28, 11, 738587)
    area_berlin.ended = False
    area_berlin.comment = u''
    area_berlin.iso_3166_2_codes = [
        iso31662_13,
    ]
    area_berlin.type = areatype_city
    session.add(area_berlin)

    linkareaarea_22 = LinkAreaArea()
    linkareaarea_22.id = 67
    linkareaarea_22.edits_pending = 0
    linkareaarea_22.last_updated = datetime.datetime(2013, 5, 17, 21, 33, 36, 112118)
    linkareaarea_22.link_order = 0
    linkareaarea_22.entity0_credit = u''
    linkareaarea_22.entity1_credit = u''
    linkareaarea_22.entity0 = area_germany
    linkareaarea_22.entity1 = area_berlin
    linkareaarea_22.link = link_1
    session.add(linkareaarea_22)

    artistipi_9 = ArtistIPI()
    artistipi_9.ipi = u'00251387665'
    artistipi_9.edits_pending = 0
    artistipi_9.created = datetime.datetime(2014, 1, 6, 6, 55, 18, 605572)
    session.add(artistipi_9)

    artistmeta_18 = ArtistMeta()
    artistmeta_18.rating = 100
    artistmeta_18.rating_count = 1
    session.add(artistmeta_18)

    artist_thomas_schumacher = Artist()
    artist_thomas_schumacher.id = 43060
    artist_thomas_schumacher.gid = '25fdd039-edad-466e-b150-d7405c4da995'
    artist_thomas_schumacher.name = u'Thomas Schumacher'
    artist_thomas_schumacher.sort_name = u'Schumacher, Thomas'
    artist_thomas_schumacher.comment = u''
    artist_thomas_schumacher.edits_pending = 0
    artist_thomas_schumacher.last_updated = datetime.datetime(2015, 10, 24, 13, 0, 55, 812217)
    artist_thomas_schumacher.ended = False
    artist_thomas_schumacher.area = area_germany
    artist_thomas_schumacher.begin_area = area_berlin
    artist_thomas_schumacher.gender = gender_male
    artist_thomas_schumacher.ipis = [
        artistipi_9,
    ]
    artist_thomas_schumacher.meta = artistmeta_18
    artist_thomas_schumacher.type = artisttype_person
    session.add(artist_thomas_schumacher)

    artistcreditname_thomas_schumacher = ArtistCreditName()
    artistcreditname_thomas_schumacher.position = 0
    artistcreditname_thomas_schumacher.name = u'Thomas Schumacher'
    artistcreditname_thomas_schumacher.join_phrase = u''
    artistcreditname_thomas_schumacher.artist = artist_thomas_schumacher
    session.add(artistcreditname_thomas_schumacher)

    artistcredit_thomas_schumacher = ArtistCredit()
    artistcredit_thomas_schumacher.id = 43060
    artistcredit_thomas_schumacher.name = u'Thomas Schumacher'
    artistcredit_thomas_schumacher.artist_count = 1
    artistcredit_thomas_schumacher.ref_count = 724
    artistcredit_thomas_schumacher.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_thomas_schumacher.artists = [
        artistcreditname_thomas_schumacher,
    ]
    session.add(artistcredit_thomas_schumacher)

    recordingmeta_19 = RecordingMeta()
    session.add(recordingmeta_19)

    recording_high_on_you = Recording()
    recording_high_on_you.id = 7134075
    recording_high_on_you.gid = '4549104e-18e1-4006-af43-7b973d995025'
    recording_high_on_you.name = u'High on You'
    recording_high_on_you.length = 402466
    recording_high_on_you.comment = u''
    recording_high_on_you.edits_pending = 0
    recording_high_on_you.video = False
    recording_high_on_you.artist_credit = artistcredit_thomas_schumacher
    recording_high_on_you.meta = recordingmeta_19
    session.add(recording_high_on_you)

    track_high_on_you = Track()
    track_high_on_you.id = 5918649
    track_high_on_you.gid = '081781bf-f10d-3406-ac7b-5df2aa03d0f1'
    track_high_on_you.position = 7
    track_high_on_you.number = u'7'
    track_high_on_you.name = u'High on You'
    track_high_on_you.length = 402466
    track_high_on_you.edits_pending = 0
    track_high_on_you.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_high_on_you.is_data_track = False
    track_high_on_you.artist_credit = artistcredit_thomas_schumacher
    track_high_on_you.recording = recording_high_on_you
    session.add(track_high_on_you)

    areatype_district = AreaType()
    areatype_district.id = 5
    areatype_district.name = u'District'
    areatype_district.child_order = 5
    areatype_district.description = u'District is used for a division of a large city, e.g. Queens.'
    areatype_district.gid = '84039871-5e47-38ca-a66a-45e512c8290f'
    session.add(areatype_district)

    area_harlem = Area()
    area_harlem.id = 88554
    area_harlem.gid = '7e037c94-d999-4611-a8fd-56e8770f2e3c'
    area_harlem.name = u'Harlem'
    area_harlem.edits_pending = 0
    area_harlem.last_updated = datetime.datetime(2014, 1, 15, 15, 1, 57, 288705)
    area_harlem.ended = False
    area_harlem.comment = u''
    area_harlem.type = areatype_district
    session.add(area_harlem)

    area_manhattan = Area()
    area_manhattan.id = 10862
    area_manhattan.gid = '261962ea-d8c2-4eaf-a80c-f14376ffadb0'
    area_manhattan.name = u'Manhattan'
    area_manhattan.edits_pending = 0
    area_manhattan.last_updated = datetime.datetime(2013, 8, 28, 13, 49, 3, 230143)
    area_manhattan.ended = False
    area_manhattan.comment = u''
    area_manhattan.type = areatype_district
    session.add(area_manhattan)

    linkareaarea_24 = LinkAreaArea()
    linkareaarea_24.id = 10626
    linkareaarea_24.edits_pending = 0
    linkareaarea_24.last_updated = datetime.datetime(2013, 6, 20, 22, 9, 0, 648765)
    linkareaarea_24.link_order = 0
    linkareaarea_24.entity0_credit = u''
    linkareaarea_24.entity1_credit = u''
    linkareaarea_24.entity0 = area_new_york_1
    linkareaarea_24.entity1 = area_manhattan
    linkareaarea_24.link = link_1
    session.add(linkareaarea_24)

    linkareaarea_23 = LinkAreaArea()
    linkareaarea_23.id = 88309
    linkareaarea_23.edits_pending = 0
    linkareaarea_23.last_updated = datetime.datetime(2014, 1, 15, 15, 2, 22, 242722)
    linkareaarea_23.link_order = 0
    linkareaarea_23.entity0_credit = u''
    linkareaarea_23.entity1_credit = u''
    linkareaarea_23.entity0 = area_manhattan
    linkareaarea_23.entity1 = area_harlem
    linkareaarea_23.link = link_1
    session.add(linkareaarea_23)

    artistipi_10 = ArtistIPI()
    artistipi_10.ipi = u'00232910692'
    artistipi_10.edits_pending = 0
    artistipi_10.created = datetime.datetime(2015, 2, 26, 5, 0, 57, 3239)
    session.add(artistipi_10)

    artistipi_11 = ArtistIPI()
    artistipi_11.ipi = u'00232910003'
    artistipi_11.edits_pending = 0
    artistipi_11.created = datetime.datetime(2015, 2, 26, 5, 0, 57, 3239)
    session.add(artistipi_11)

    artistipi_12 = ArtistIPI()
    artistipi_12.ipi = u'00232910101'
    artistipi_12.edits_pending = 0
    artistipi_12.created = datetime.datetime(2015, 2, 26, 5, 0, 57, 3239)
    session.add(artistipi_12)

    artistisni_7 = ArtistISNI()
    artistisni_7.isni = u'000000005705334X'
    artistisni_7.edits_pending = 0
    artistisni_7.created = datetime.datetime(2015, 2, 26, 5, 0, 57, 3239)
    session.add(artistisni_7)

    artistisni_8 = ArtistISNI()
    artistisni_8.isni = u'0000000078243206'
    artistisni_8.edits_pending = 0
    artistisni_8.created = datetime.datetime(2015, 2, 26, 5, 0, 57, 3239)
    session.add(artistisni_8)

    artistisni_9 = ArtistISNI()
    artistisni_9.isni = u'0000000041815776'
    artistisni_9.edits_pending = 0
    artistisni_9.created = datetime.datetime(2015, 2, 26, 5, 0, 57, 3239)
    session.add(artistisni_9)

    artistmeta_19 = ArtistMeta()
    artistmeta_19.rating = 80
    artistmeta_19.rating_count = 13
    session.add(artistmeta_19)

    artist_moby = Artist()
    artist_moby.id = 359
    artist_moby.gid = '8970d868-0723-483b-a75b-51088913d3d4'
    artist_moby.name = u'Moby'
    artist_moby.sort_name = u'Moby'
    artist_moby.begin_date_year = 1965
    artist_moby.begin_date_month = 9
    artist_moby.begin_date_day = 11
    artist_moby.comment = u'electronic musician Richard Melville Hall'
    artist_moby.edits_pending = 0
    artist_moby.last_updated = datetime.datetime(2016, 4, 28, 14, 42, 8, 578978)
    artist_moby.ended = False
    artist_moby.area = area_united_states
    artist_moby.begin_area = area_harlem
    artist_moby.gender = gender_male
    artist_moby.ipis = [
        artistipi_10,
        artistipi_11,
        artistipi_12,
    ]
    artist_moby.isnis = [
        artistisni_7,
        artistisni_8,
        artistisni_9,
    ]
    artist_moby.meta = artistmeta_19
    artist_moby.type = artisttype_person
    session.add(artist_moby)

    artistcreditname_moby = ArtistCreditName()
    artistcreditname_moby.position = 0
    artistcreditname_moby.name = u'Moby'
    artistcreditname_moby.join_phrase = u''
    artistcreditname_moby.artist = artist_moby
    session.add(artistcreditname_moby)

    artistcredit_moby = ArtistCredit()
    artistcredit_moby.id = 359
    artistcredit_moby.name = u'Moby'
    artistcredit_moby.artist_count = 1
    artistcredit_moby.ref_count = 9355
    artistcredit_moby.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_moby.artists = [
        artistcreditname_moby,
    ]
    session.add(artistcredit_moby)

    recordingmeta_20 = RecordingMeta()
    session.add(recordingmeta_20)

    recording_go_trentemoller_remix = Recording()
    recording_go_trentemoller_remix.id = 7134076
    recording_go_trentemoller_remix.gid = '79e29af0-5dda-4ac9-a0a8-43ba8f31efa0'
    recording_go_trentemoller_remix.name = u'Go! (Trentem\xf8ller remix)'
    recording_go_trentemoller_remix.length = 392373
    recording_go_trentemoller_remix.comment = u''
    recording_go_trentemoller_remix.edits_pending = 0
    recording_go_trentemoller_remix.video = False
    recording_go_trentemoller_remix.artist_credit = artistcredit_moby
    recording_go_trentemoller_remix.meta = recordingmeta_20
    session.add(recording_go_trentemoller_remix)

    linktype_remixer = LinkType()
    linktype_remixer.id = 153
    linktype_remixer.child_order = 0
    linktype_remixer.gid = '7950be4d-13a3-48e7-906b-5af562e39544'
    linktype_remixer.entity_type0 = u'artist'
    linktype_remixer.entity_type1 = u'recording'
    linktype_remixer.name = u'remixer'
    linktype_remixer.description = u'This links a recording to the person who remixed it by taking one or more other tracks, substantially altering them and mixing them together with other material. Note that this includes the artist who created a mash-up or used samples as well.'
    linktype_remixer.link_phrase = u'{additional:additionally} remixed'
    linktype_remixer.reverse_link_phrase = u'{additional} remixer'
    linktype_remixer.long_link_phrase = u'{additional:additionally} remixed'
    linktype_remixer.priority = 0
    linktype_remixer.last_updated = datetime.datetime(2014, 4, 26, 12, 27, 35, 727039)
    linktype_remixer.is_deprecated = False
    linktype_remixer.has_dates = True
    linktype_remixer.entity0_cardinality = 1
    linktype_remixer.entity1_cardinality = 0
    session.add(linktype_remixer)

    link_7 = Link()
    link_7.id = 12735
    link_7.attribute_count = 0
    link_7.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_7.ended = False
    link_7.link_type = linktype_remixer
    session.add(link_7)

    linkartistrecording_1 = LinkArtistRecording()
    linkartistrecording_1.id = 106130
    linkartistrecording_1.edits_pending = 0
    linkartistrecording_1.last_updated = datetime.datetime(2015, 8, 8, 10, 4, 9, 402935)
    linkartistrecording_1.link_order = 0
    linkartistrecording_1.entity0_credit = u''
    linkartistrecording_1.entity1_credit = u''
    linkartistrecording_1.entity0 = artist_trentemoller
    linkartistrecording_1.entity1 = recording_go_trentemoller_remix
    linkartistrecording_1.link = link_7
    session.add(linkartistrecording_1)

    workmeta_3 = WorkMeta()
    session.add(workmeta_3)

    work_go = Work()
    work_go.id = 231738
    work_go.gid = 'e02ccc5b-d39f-31d2-aaf5-b56ad67e4ffe'
    work_go.name = u'Go'
    work_go.comment = u''
    work_go.edits_pending = 0
    work_go.last_updated = datetime.datetime(2011, 6, 19, 16, 0, 41, 600042)
    work_go.meta = workmeta_3
    session.add(work_go)

    artistipi_13 = ArtistIPI()
    artistipi_13.ipi = u'00232910003'
    artistipi_13.edits_pending = 0
    artistipi_13.created = datetime.datetime(2014, 8, 21, 22, 45, 25, 328888)
    session.add(artistipi_13)

    artistipi_14 = ArtistIPI()
    artistipi_14.ipi = u'00232910692'
    artistipi_14.edits_pending = 0
    artistipi_14.created = datetime.datetime(2014, 8, 21, 22, 45, 25, 328888)
    session.add(artistipi_14)

    artistisni_10 = ArtistISNI()
    artistisni_10.isni = u'0000000041815776'
    artistisni_10.edits_pending = 0
    artistisni_10.created = datetime.datetime(2014, 3, 21, 4, 45, 0, 95440)
    session.add(artistisni_10)

    artistisni_11 = ArtistISNI()
    artistisni_11.isni = u'000000005705334X'
    artistisni_11.edits_pending = 0
    artistisni_11.created = datetime.datetime(2014, 3, 21, 4, 45, 0, 95440)
    session.add(artistisni_11)

    artistmeta_20 = ArtistMeta()
    session.add(artistmeta_20)

    artist_richard_melville_hall = Artist()
    artist_richard_melville_hall.id = 245110
    artist_richard_melville_hall.gid = '8abdbc82-b5f0-4bd8-9c06-9c3393c9f99f'
    artist_richard_melville_hall.name = u'Richard Melville Hall'
    artist_richard_melville_hall.sort_name = u'Hall, Richard Melville'
    artist_richard_melville_hall.begin_date_year = 1965
    artist_richard_melville_hall.begin_date_month = 9
    artist_richard_melville_hall.begin_date_day = 11
    artist_richard_melville_hall.comment = u''
    artist_richard_melville_hall.edits_pending = 0
    artist_richard_melville_hall.last_updated = datetime.datetime(2014, 8, 21, 22, 45, 25, 328888)
    artist_richard_melville_hall.ended = False
    artist_richard_melville_hall.area = area_united_states
    artist_richard_melville_hall.begin_area = area_harlem
    artist_richard_melville_hall.gender = gender_male
    artist_richard_melville_hall.ipis = [
        artistipi_13,
        artistipi_14,
    ]
    artist_richard_melville_hall.isnis = [
        artistisni_10,
        artistisni_11,
    ]
    artist_richard_melville_hall.meta = artistmeta_20
    artist_richard_melville_hall.type = artisttype_person
    session.add(artist_richard_melville_hall)

    linkartistwork_11 = LinkArtistWork()
    linkartistwork_11.id = 262864
    linkartistwork_11.edits_pending = 0
    linkartistwork_11.last_updated = datetime.datetime(2011, 6, 19, 16, 0, 41, 600042)
    linkartistwork_11.link_order = 0
    linkartistwork_11.entity0_credit = u''
    linkartistwork_11.entity1_credit = u''
    linkartistwork_11.entity0 = artist_richard_melville_hall
    linkartistwork_11.entity1 = work_go
    linkartistwork_11.link = link_3
    session.add(linkartistwork_11)

    linkartistwork_12 = LinkArtistWork()
    linkartistwork_12.id = 296042
    linkartistwork_12.edits_pending = 0
    linkartistwork_12.last_updated = datetime.datetime(2011, 6, 19, 16, 0, 41, 600042)
    linkartistwork_12.link_order = 0
    linkartistwork_12.entity0_credit = u''
    linkartistwork_12.entity1_credit = u''
    linkartistwork_12.entity0 = artist_richard_melville_hall
    linkartistwork_12.entity1 = work_go
    linkartistwork_12.link = link_2
    session.add(linkartistwork_12)

    url_3 = URL()
    url_3.id = 1779416
    url_3.gid = 'a6f1aa9a-ccc0-4ee8-a464-5e8366ace995'
    url_3.url = u'https://www.wikidata.org/wiki/Q1652489'
    url_3.edits_pending = 0
    url_3.last_updated = datetime.datetime(2016, 6, 30, 20, 0, 2, 659808)
    session.add(url_3)

    linkurlwork_3 = LinkURLWork()
    linkurlwork_3.id = 45904
    linkurlwork_3.edits_pending = 0
    linkurlwork_3.last_updated = datetime.datetime(2013, 6, 18, 22, 28, 12, 863852)
    linkurlwork_3.link_order = 0
    linkurlwork_3.entity0_credit = u''
    linkurlwork_3.entity1_credit = u''
    linkurlwork_3.entity0 = url_3
    linkurlwork_3.entity1 = work_go
    linkurlwork_3.link = link_4
    session.add(linkurlwork_3)

    linkrecordingwork_3 = LinkRecordingWork()
    linkrecordingwork_3.id = 1095562
    linkrecordingwork_3.edits_pending = 0
    linkrecordingwork_3.last_updated = datetime.datetime(2013, 6, 18, 1, 50, 31, 199668)
    linkrecordingwork_3.link_order = 0
    linkrecordingwork_3.entity0_credit = u''
    linkrecordingwork_3.entity1_credit = u''
    linkrecordingwork_3.entity0 = recording_go_trentemoller_remix
    linkrecordingwork_3.entity1 = work_go
    linkrecordingwork_3.link = link_6
    session.add(linkrecordingwork_3)

    track_go_trentemoller_remix = Track()
    track_go_trentemoller_remix.id = 5918650
    track_go_trentemoller_remix.gid = '9aa04088-f04b-3b98-8aa6-0d579de621fd'
    track_go_trentemoller_remix.position = 8
    track_go_trentemoller_remix.number = u'8'
    track_go_trentemoller_remix.name = u'Go! (Trentem\xf8ller remix)'
    track_go_trentemoller_remix.length = 392373
    track_go_trentemoller_remix.edits_pending = 0
    track_go_trentemoller_remix.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_go_trentemoller_remix.is_data_track = False
    track_go_trentemoller_remix.artist_credit = artistcredit_moby
    track_go_trentemoller_remix.recording = recording_go_trentemoller_remix
    session.add(track_go_trentemoller_remix)

    area_stockholm = Area()
    area_stockholm.id = 5114
    area_stockholm.gid = '1127ddc2-eab3-4662-8718-6adbdeea3b10'
    area_stockholm.name = u'Stockholm'
    area_stockholm.edits_pending = 0
    area_stockholm.last_updated = datetime.datetime(2013, 11, 24, 6, 30, 16, 374681)
    area_stockholm.ended = False
    area_stockholm.comment = u''
    area_stockholm.type = areatype_city
    session.add(area_stockholm)

    iso31662_14 = ISO31662()
    iso31662_14.code = u'SE-AB'
    session.add(iso31662_14)

    area_stockholm_1 = Area()
    area_stockholm_1.id = 469
    area_stockholm_1.gid = '63ee9426-d32f-4593-a262-6401bc85c6ba'
    area_stockholm_1.name = u'Stockholm'
    area_stockholm_1.edits_pending = 0
    area_stockholm_1.last_updated = datetime.datetime(2014, 12, 8, 19, 59, 50, 698419)
    area_stockholm_1.ended = False
    area_stockholm_1.comment = u''
    area_stockholm_1.iso_3166_2_codes = [
        iso31662_14,
    ]
    area_stockholm_1.type = areatype_subdivision
    session.add(area_stockholm_1)

    linkareaarea_26 = LinkAreaArea()
    linkareaarea_26.id = 229
    linkareaarea_26.edits_pending = 0
    linkareaarea_26.last_updated = datetime.datetime(2013, 5, 18, 22, 42, 19, 419007)
    linkareaarea_26.link_order = 0
    linkareaarea_26.entity0_credit = u''
    linkareaarea_26.entity1_credit = u''
    linkareaarea_26.entity0 = area_sweden
    linkareaarea_26.entity1 = area_stockholm_1
    linkareaarea_26.link = link_1
    session.add(linkareaarea_26)

    linkareaarea_25 = LinkAreaArea()
    linkareaarea_25.id = 4880
    linkareaarea_25.edits_pending = 0
    linkareaarea_25.last_updated = datetime.datetime(2013, 5, 24, 20, 30, 17, 245957)
    linkareaarea_25.link_order = 0
    linkareaarea_25.entity0_credit = u''
    linkareaarea_25.entity1_credit = u''
    linkareaarea_25.entity0 = area_stockholm_1
    linkareaarea_25.entity1 = area_stockholm
    linkareaarea_25.link = link_1
    session.add(linkareaarea_25)

    artistmeta_21 = ArtistMeta()
    artistmeta_21.rating = 100
    artistmeta_21.rating_count = 2
    session.add(artistmeta_21)

    artist_the_knife = Artist()
    artist_the_knife.id = 61967
    artist_the_knife.gid = 'bf710b71-48e5-4e15-9bd6-96debb2e4e98'
    artist_the_knife.name = u'The Knife'
    artist_the_knife.sort_name = u'Knife, The'
    artist_the_knife.begin_date_year = 1999
    artist_the_knife.end_date_year = 2014
    artist_the_knife.end_date_month = 11
    artist_the_knife.comment = u'Swedish indie electronic duo'
    artist_the_knife.edits_pending = 0
    artist_the_knife.last_updated = datetime.datetime(2015, 1, 9, 11, 0, 14, 339928)
    artist_the_knife.ended = True
    artist_the_knife.area = area_sweden
    artist_the_knife.begin_area = area_stockholm
    artist_the_knife.meta = artistmeta_21
    artist_the_knife.type = artisttype_group
    session.add(artist_the_knife)

    artistcreditname_the_knife = ArtistCreditName()
    artistcreditname_the_knife.position = 0
    artistcreditname_the_knife.name = u'The Knife'
    artistcreditname_the_knife.join_phrase = u''
    artistcreditname_the_knife.artist = artist_the_knife
    session.add(artistcreditname_the_knife)

    artistcredit_the_knife = ArtistCredit()
    artistcredit_the_knife.id = 61967
    artistcredit_the_knife.name = u'The Knife'
    artistcredit_the_knife.artist_count = 1
    artistcredit_the_knife.ref_count = 1342
    artistcredit_the_knife.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_the_knife.artists = [
        artistcreditname_the_knife,
    ]
    session.add(artistcredit_the_knife)

    recordingmeta_21 = RecordingMeta()
    session.add(recordingmeta_21)

    recording_silent_shout_trente_short_edit = Recording()
    recording_silent_shout_trente_short_edit.id = 7134077
    recording_silent_shout_trente_short_edit.gid = 'e2c36349-6092-4b26-8eec-40c5a3c89e54'
    recording_silent_shout_trente_short_edit.name = u'Silent Shout (Trente short edit)'
    recording_silent_shout_trente_short_edit.length = 14986
    recording_silent_shout_trente_short_edit.comment = u''
    recording_silent_shout_trente_short_edit.edits_pending = 0
    recording_silent_shout_trente_short_edit.video = False
    recording_silent_shout_trente_short_edit.artist_credit = artistcredit_the_knife
    recording_silent_shout_trente_short_edit.meta = recordingmeta_21
    session.add(recording_silent_shout_trente_short_edit)

    linkartistrecording_2 = LinkArtistRecording()
    linkartistrecording_2.id = 106129
    linkartistrecording_2.edits_pending = 0
    linkartistrecording_2.last_updated = datetime.datetime(2015, 8, 8, 10, 4, 9, 402935)
    linkartistrecording_2.link_order = 0
    linkartistrecording_2.entity0_credit = u''
    linkartistrecording_2.entity1_credit = u''
    linkartistrecording_2.entity0 = artist_trentemoller
    linkartistrecording_2.entity1 = recording_silent_shout_trente_short_edit
    linkartistrecording_2.link = link_7
    session.add(linkartistrecording_2)

    track_silent_shout_trente_short_edit = Track()
    track_silent_shout_trente_short_edit.id = 5918651
    track_silent_shout_trente_short_edit.gid = '88d0b720-1aca-3513-8ab3-50d2a1293743'
    track_silent_shout_trente_short_edit.position = 9
    track_silent_shout_trente_short_edit.number = u'9'
    track_silent_shout_trente_short_edit.name = u'Silent Shout (Trente short edit)'
    track_silent_shout_trente_short_edit.length = 14986
    track_silent_shout_trente_short_edit.edits_pending = 0
    track_silent_shout_trente_short_edit.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_silent_shout_trente_short_edit.is_data_track = False
    track_silent_shout_trente_short_edit.artist_credit = artistcredit_the_knife
    track_silent_shout_trente_short_edit.recording = recording_silent_shout_trente_short_edit
    session.add(track_silent_shout_trente_short_edit)

    artistmeta_22 = ArtistMeta()
    session.add(artistmeta_22)

    artist_jokke_ilsoe = Artist()
    artist_jokke_ilsoe.id = 362912
    artist_jokke_ilsoe.gid = 'e1c79c85-44ed-4483-8ec6-28cfe6440345'
    artist_jokke_ilsoe.name = u'Jokke Ils\xf8e'
    artist_jokke_ilsoe.sort_name = u'Ils\xf8e, Jokke'
    artist_jokke_ilsoe.comment = u''
    artist_jokke_ilsoe.edits_pending = 0
    artist_jokke_ilsoe.last_updated = datetime.datetime(2014, 5, 1, 17, 5, 18, 237341)
    artist_jokke_ilsoe.ended = False
    artist_jokke_ilsoe.area = area_denmark
    artist_jokke_ilsoe.gender = gender_male
    artist_jokke_ilsoe.meta = artistmeta_22
    artist_jokke_ilsoe.type = artisttype_person
    session.add(artist_jokke_ilsoe)

    artistcreditname_jokke_ilsoe = ArtistCreditName()
    artistcreditname_jokke_ilsoe.position = 0
    artistcreditname_jokke_ilsoe.name = u'Jokke Ils\xf8e'
    artistcreditname_jokke_ilsoe.join_phrase = u''
    artistcreditname_jokke_ilsoe.artist = artist_jokke_ilsoe
    session.add(artistcreditname_jokke_ilsoe)

    artistcredit_jokke_ilsoe = ArtistCredit()
    artistcredit_jokke_ilsoe.id = 362912
    artistcredit_jokke_ilsoe.name = u'Jokke Ils\xf8e'
    artistcredit_jokke_ilsoe.artist_count = 1
    artistcredit_jokke_ilsoe.ref_count = 41
    artistcredit_jokke_ilsoe.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_jokke_ilsoe.artists = [
        artistcreditname_jokke_ilsoe,
    ]
    session.add(artistcredit_jokke_ilsoe)

    recordingmeta_22 = RecordingMeta()
    session.add(recordingmeta_22)

    recording_feelin_good_trentemoller_remix = Recording()
    recording_feelin_good_trentemoller_remix.id = 7134078
    recording_feelin_good_trentemoller_remix.gid = 'cc58b376-53a0-41a2-9a6d-a569b81228b5'
    recording_feelin_good_trentemoller_remix.name = u"Feelin' Good (Trentem\xf8ller remix)"
    recording_feelin_good_trentemoller_remix.length = 383320
    recording_feelin_good_trentemoller_remix.comment = u''
    recording_feelin_good_trentemoller_remix.edits_pending = 0
    recording_feelin_good_trentemoller_remix.video = False
    recording_feelin_good_trentemoller_remix.artist_credit = artistcredit_jokke_ilsoe
    recording_feelin_good_trentemoller_remix.meta = recordingmeta_22
    session.add(recording_feelin_good_trentemoller_remix)

    linkartistrecording_3 = LinkArtistRecording()
    linkartistrecording_3.id = 106128
    linkartistrecording_3.edits_pending = 0
    linkartistrecording_3.last_updated = datetime.datetime(2015, 8, 8, 10, 4, 9, 402935)
    linkartistrecording_3.link_order = 0
    linkartistrecording_3.entity0_credit = u''
    linkartistrecording_3.entity1_credit = u''
    linkartistrecording_3.entity0 = artist_trentemoller
    linkartistrecording_3.entity1 = recording_feelin_good_trentemoller_remix
    linkartistrecording_3.link = link_7
    session.add(linkartistrecording_3)

    track_feelin_good_trentemoller_remix = Track()
    track_feelin_good_trentemoller_remix.id = 5918652
    track_feelin_good_trentemoller_remix.gid = '8a14c288-f753-3c2b-9cb0-306b3eca70dc'
    track_feelin_good_trentemoller_remix.position = 10
    track_feelin_good_trentemoller_remix.number = u'10'
    track_feelin_good_trentemoller_remix.name = u"Feelin' Good (Trentem\xf8ller remix)"
    track_feelin_good_trentemoller_remix.length = 383320
    track_feelin_good_trentemoller_remix.edits_pending = 0
    track_feelin_good_trentemoller_remix.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_feelin_good_trentemoller_remix.is_data_track = False
    track_feelin_good_trentemoller_remix.artist_credit = artistcredit_jokke_ilsoe
    track_feelin_good_trentemoller_remix.recording = recording_feelin_good_trentemoller_remix
    session.add(track_feelin_good_trentemoller_remix)

    area_frankfurt_am_main = Area()
    area_frankfurt_am_main.id = 7948
    area_frankfurt_am_main.gid = '16560d3e-358b-4869-8a6d-727db2ee7b69'
    area_frankfurt_am_main.name = u'Frankfurt am Main'
    area_frankfurt_am_main.edits_pending = 0
    area_frankfurt_am_main.last_updated = datetime.datetime(2013, 11, 26, 9, 27, 26, 784317)
    area_frankfurt_am_main.ended = False
    area_frankfurt_am_main.comment = u''
    area_frankfurt_am_main.type = areatype_city
    session.add(area_frankfurt_am_main)

    iso31662_15 = ISO31662()
    iso31662_15.code = u'DE-HE'
    session.add(iso31662_15)

    area_hessen = Area()
    area_hessen.id = 330
    area_hessen.gid = '1b761636-6166-4dec-af7f-48c506f4e24d'
    area_hessen.name = u'Hessen'
    area_hessen.edits_pending = 0
    area_hessen.last_updated = datetime.datetime(2013, 11, 26, 12, 17, 33, 793273)
    area_hessen.ended = False
    area_hessen.comment = u''
    area_hessen.iso_3166_2_codes = [
        iso31662_15,
    ]
    area_hessen.type = areatype_subdivision
    session.add(area_hessen)

    linkareaarea_28 = LinkAreaArea()
    linkareaarea_28.id = 71
    linkareaarea_28.edits_pending = 0
    linkareaarea_28.last_updated = datetime.datetime(2013, 5, 17, 21, 34, 23, 799399)
    linkareaarea_28.link_order = 0
    linkareaarea_28.entity0_credit = u''
    linkareaarea_28.entity1_credit = u''
    linkareaarea_28.entity0 = area_germany
    linkareaarea_28.entity1 = area_hessen
    linkareaarea_28.link = link_1
    session.add(linkareaarea_28)

    linkareaarea_27 = LinkAreaArea()
    linkareaarea_27.id = 7714
    linkareaarea_27.edits_pending = 0
    linkareaarea_27.last_updated = datetime.datetime(2013, 5, 29, 8, 22, 15, 892480)
    linkareaarea_27.link_order = 0
    linkareaarea_27.entity0_credit = u''
    linkareaarea_27.entity1_credit = u''
    linkareaarea_27.entity0 = area_hessen
    linkareaarea_27.entity1 = area_frankfurt_am_main
    linkareaarea_27.link = link_1
    session.add(linkareaarea_27)

    artistisni_12 = ArtistISNI()
    artistisni_12.isni = u'0000000018888096'
    artistisni_12.edits_pending = 0
    artistisni_12.created = datetime.datetime(2014, 4, 23, 21, 57, 23, 427938)
    session.add(artistisni_12)

    artistmeta_23 = ArtistMeta()
    session.add(artistmeta_23)

    artist_isolee = Artist()
    artist_isolee.id = 57862
    artist_isolee.gid = '4c99c0b4-5d46-44d2-8c49-ba47a522b016'
    artist_isolee.name = u'Isol\xe9e'
    artist_isolee.sort_name = u'Isol\xe9e'
    artist_isolee.comment = u''
    artist_isolee.edits_pending = 0
    artist_isolee.last_updated = datetime.datetime(2014, 4, 23, 21, 57, 23, 427938)
    artist_isolee.ended = False
    artist_isolee.area = area_germany
    artist_isolee.begin_area = area_frankfurt_am_main
    artist_isolee.gender = gender_male
    artist_isolee.isnis = [
        artistisni_12,
    ]
    artist_isolee.meta = artistmeta_23
    artist_isolee.type = artisttype_person
    session.add(artist_isolee)

    artistcreditname_isolee = ArtistCreditName()
    artistcreditname_isolee.position = 0
    artistcreditname_isolee.name = u'Isol\xe9e'
    artistcreditname_isolee.join_phrase = u''
    artistcreditname_isolee.artist = artist_isolee
    session.add(artistcreditname_isolee)

    artistcredit_isolee = ArtistCredit()
    artistcredit_isolee.id = 57862
    artistcredit_isolee.name = u'Isol\xe9e'
    artistcredit_isolee.artist_count = 1
    artistcredit_isolee.ref_count = 548
    artistcredit_isolee.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_isolee.artists = [
        artistcreditname_isolee,
    ]
    session.add(artistcredit_isolee)

    recordingmeta_23 = RecordingMeta()
    session.add(recordingmeta_23)

    recording_beau_mot_plage_freeform_five_remix_re_edit = Recording()
    recording_beau_mot_plage_freeform_five_remix_re_edit.id = 7134079
    recording_beau_mot_plage_freeform_five_remix_re_edit.gid = 'a0484b13-1136-47b3-9950-7c2633d989d7'
    recording_beau_mot_plage_freeform_five_remix_re_edit.name = u'Beau Mot Plage (Freeform Five remix re-edit)'
    recording_beau_mot_plage_freeform_five_remix_re_edit.length = 144373
    recording_beau_mot_plage_freeform_five_remix_re_edit.comment = u''
    recording_beau_mot_plage_freeform_five_remix_re_edit.edits_pending = 0
    recording_beau_mot_plage_freeform_five_remix_re_edit.video = False
    recording_beau_mot_plage_freeform_five_remix_re_edit.artist_credit = artistcredit_isolee
    recording_beau_mot_plage_freeform_five_remix_re_edit.meta = recordingmeta_23
    session.add(recording_beau_mot_plage_freeform_five_remix_re_edit)

    iswc_1 = ISWC()
    iswc_1.id = 67575
    iswc_1.iswc = u'T-801.459.648-7'
    iswc_1.edits_pending = 0
    iswc_1.created = datetime.datetime(2014, 6, 24, 12, 21, 13, 39727)
    session.add(iswc_1)

    workmeta_4 = WorkMeta()
    session.add(workmeta_4)

    work_beau_mot_plage = Work()
    work_beau_mot_plage.id = 1386245
    work_beau_mot_plage.gid = '4e383c03-2a58-33d1-8cb2-bafdbbb963b7'
    work_beau_mot_plage.name = u'Beau Mot Plage'
    work_beau_mot_plage.comment = u''
    work_beau_mot_plage.edits_pending = 0
    work_beau_mot_plage.iswcs = [
        iswc_1,
    ]
    work_beau_mot_plage.meta = workmeta_4
    session.add(work_beau_mot_plage)

    artistipi_15 = ArtistIPI()
    artistipi_15.ipi = u'00269810536'
    artistipi_15.edits_pending = 0
    artistipi_15.created = datetime.datetime(2014, 4, 23, 23, 5, 54, 627541)
    session.add(artistipi_15)

    artistmeta_24 = ArtistMeta()
    session.add(artistmeta_24)

    artist_rajko_muller = Artist()
    artist_rajko_muller.id = 291852
    artist_rajko_muller.gid = 'fa8c5306-b6db-49dc-b065-0f15a175117c'
    artist_rajko_muller.name = u'Rajko M\xfcller'
    artist_rajko_muller.sort_name = u'M\xfcller, Rajko'
    artist_rajko_muller.comment = u''
    artist_rajko_muller.edits_pending = 0
    artist_rajko_muller.last_updated = datetime.datetime(2014, 4, 23, 23, 5, 54, 627541)
    artist_rajko_muller.ended = False
    artist_rajko_muller.area = area_germany
    artist_rajko_muller.begin_area = area_frankfurt_am_main
    artist_rajko_muller.gender = gender_male
    artist_rajko_muller.ipis = [
        artistipi_15,
    ]
    artist_rajko_muller.meta = artistmeta_24
    artist_rajko_muller.type = artisttype_person
    session.add(artist_rajko_muller)

    linkartistwork_13 = LinkArtistWork()
    linkartistwork_13.id = 72855
    linkartistwork_13.edits_pending = 0
    linkartistwork_13.last_updated = datetime.datetime(2011, 5, 16, 16, 27, 39, 450042)
    linkartistwork_13.link_order = 0
    linkartistwork_13.entity0_credit = u''
    linkartistwork_13.entity1_credit = u''
    linkartistwork_13.entity0 = artist_rajko_muller
    linkartistwork_13.entity1 = work_beau_mot_plage
    linkartistwork_13.link = link_3
    session.add(linkartistwork_13)

    linkrecordingwork_4 = LinkRecordingWork()
    linkrecordingwork_4.id = 1447947
    linkrecordingwork_4.edits_pending = 0
    linkrecordingwork_4.last_updated = datetime.datetime(2014, 6, 24, 12, 28, 31, 389674)
    linkrecordingwork_4.link_order = 0
    linkrecordingwork_4.entity0_credit = u''
    linkrecordingwork_4.entity1_credit = u''
    linkrecordingwork_4.entity0 = recording_beau_mot_plage_freeform_five_remix_re_edit
    linkrecordingwork_4.entity1 = work_beau_mot_plage
    linkrecordingwork_4.link = link_6
    session.add(linkrecordingwork_4)

    track_beau_mot_plage_freeform_five_remix_re_edit = Track()
    track_beau_mot_plage_freeform_five_remix_re_edit.id = 5918653
    track_beau_mot_plage_freeform_five_remix_re_edit.gid = 'e23716f6-6900-356a-bb73-b1b0e5e26b4d'
    track_beau_mot_plage_freeform_five_remix_re_edit.position = 11
    track_beau_mot_plage_freeform_five_remix_re_edit.number = u'11'
    track_beau_mot_plage_freeform_five_remix_re_edit.name = u'Beau Mot Plage (Freeform Five remix re-edit)'
    track_beau_mot_plage_freeform_five_remix_re_edit.length = 144373
    track_beau_mot_plage_freeform_five_remix_re_edit.edits_pending = 0
    track_beau_mot_plage_freeform_five_remix_re_edit.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_beau_mot_plage_freeform_five_remix_re_edit.is_data_track = False
    track_beau_mot_plage_freeform_five_remix_re_edit.artist_credit = artistcredit_isolee
    track_beau_mot_plage_freeform_five_remix_re_edit.recording = recording_beau_mot_plage_freeform_five_remix_re_edit
    session.add(track_beau_mot_plage_freeform_five_remix_re_edit)

    recordingmeta_24 = RecordingMeta()
    session.add(recordingmeta_24)

    recording_always_something_better_feat_richard_davis = Recording()
    recording_always_something_better_feat_richard_davis.id = 7134080
    recording_always_something_better_feat_richard_davis.gid = 'e2191030-6274-4a14-9491-30782cc23525'
    recording_always_something_better_feat_richard_davis.name = u'Always Something Better (feat. Richard Davis)'
    recording_always_something_better_feat_richard_davis.length = 461706
    recording_always_something_better_feat_richard_davis.comment = u''
    recording_always_something_better_feat_richard_davis.edits_pending = 0
    recording_always_something_better_feat_richard_davis.video = False
    recording_always_something_better_feat_richard_davis.artist_credit = artistcredit_trentemoller
    recording_always_something_better_feat_richard_davis.meta = recordingmeta_24
    session.add(recording_always_something_better_feat_richard_davis)

    track_always_something_better_feat_richard_davis = Track()
    track_always_something_better_feat_richard_davis.id = 5918654
    track_always_something_better_feat_richard_davis.gid = '258b1498-0b8d-30a5-a2fc-2ea92c4957b7'
    track_always_something_better_feat_richard_davis.position = 12
    track_always_something_better_feat_richard_davis.number = u'12'
    track_always_something_better_feat_richard_davis.name = u'Always Something Better (feat. Richard Davis)'
    track_always_something_better_feat_richard_davis.length = 461706
    track_always_something_better_feat_richard_davis.edits_pending = 0
    track_always_something_better_feat_richard_davis.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_always_something_better_feat_richard_davis.is_data_track = False
    track_always_something_better_feat_richard_davis.artist_credit = artistcredit_trentemoller
    track_always_something_better_feat_richard_davis.recording = recording_always_something_better_feat_richard_davis
    session.add(track_always_something_better_feat_richard_davis)

    recordingmeta_25 = RecordingMeta()
    session.add(recordingmeta_25)

    recording_we_share_our_mothers_health_trentemoller_remix = Recording()
    recording_we_share_our_mothers_health_trentemoller_remix.id = 7134081
    recording_we_share_our_mothers_health_trentemoller_remix.gid = 'be80f050-1549-4a3e-8a65-5d28e14b1a20'
    recording_we_share_our_mothers_health_trentemoller_remix.name = u"We Share Our Mothers' Health (Trentem\xf8ller remix)"
    recording_we_share_our_mothers_health_trentemoller_remix.length = 356160
    recording_we_share_our_mothers_health_trentemoller_remix.comment = u''
    recording_we_share_our_mothers_health_trentemoller_remix.edits_pending = 0
    recording_we_share_our_mothers_health_trentemoller_remix.last_updated = datetime.datetime(2012, 5, 28, 20, 0, 13, 371964)
    recording_we_share_our_mothers_health_trentemoller_remix.video = False
    recording_we_share_our_mothers_health_trentemoller_remix.artist_credit = artistcredit_the_knife
    recording_we_share_our_mothers_health_trentemoller_remix.meta = recordingmeta_25
    session.add(recording_we_share_our_mothers_health_trentemoller_remix)

    linkartistrecording_4 = LinkArtistRecording()
    linkartistrecording_4.id = 106127
    linkartistrecording_4.edits_pending = 0
    linkartistrecording_4.last_updated = datetime.datetime(2015, 8, 8, 10, 4, 9, 402935)
    linkartistrecording_4.link_order = 0
    linkartistrecording_4.entity0_credit = u''
    linkartistrecording_4.entity1_credit = u''
    linkartistrecording_4.entity0 = artist_trentemoller
    linkartistrecording_4.entity1 = recording_we_share_our_mothers_health_trentemoller_remix
    linkartistrecording_4.link = link_7
    session.add(linkartistrecording_4)

    track_we_share_our_mother_s_health_trentemoller_remix = Track()
    track_we_share_our_mother_s_health_trentemoller_remix.id = 5918655
    track_we_share_our_mother_s_health_trentemoller_remix.gid = '7d3c3101-db47-34dd-807f-a125afba6631'
    track_we_share_our_mother_s_health_trentemoller_remix.position = 13
    track_we_share_our_mother_s_health_trentemoller_remix.number = u'13'
    track_we_share_our_mother_s_health_trentemoller_remix.name = u"We Share Our Mother's Health (Trentem\xf8ller remix)"
    track_we_share_our_mother_s_health_trentemoller_remix.length = 356160
    track_we_share_our_mother_s_health_trentemoller_remix.edits_pending = 0
    track_we_share_our_mother_s_health_trentemoller_remix.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_we_share_our_mother_s_health_trentemoller_remix.is_data_track = False
    track_we_share_our_mother_s_health_trentemoller_remix.artist_credit = artistcredit_the_knife
    track_we_share_our_mother_s_health_trentemoller_remix.recording = recording_we_share_our_mothers_health_trentemoller_remix
    session.add(track_we_share_our_mother_s_health_trentemoller_remix)

    medium_2 = Medium()
    medium_2.id = 291059
    medium_2.position = 2
    medium_2.name = u''
    medium_2.edits_pending = 0
    medium_2.last_updated = datetime.datetime(2012, 5, 27, 11, 5, 54, 679406)
    medium_2.track_count = 13
    medium_2.format = mediumformat_cd
    medium_2.tracks = [
        track_moan_feat_ane_trolle,
        track_break_on_through_dark_ride_dub_mix,
        track_the_fallen_justice_remix,
        track_nanny_nanny_boo_boo_junior_senior_remix,
        track_contort_yourself,
        track_someone_like_you,
        track_high_on_you,
        track_go_trentemoller_remix,
        track_silent_shout_trente_short_edit,
        track_feelin_good_trentemoller_remix,
        track_beau_mot_plage_freeform_five_remix_re_edit,
        track_always_something_better_feat_richard_davis,
        track_we_share_our_mother_s_health_trentemoller_remix,
    ]
    session.add(medium_2)

    releasemeta_1 = ReleaseMeta()
    releasemeta_1.date_added = datetime.datetime(2007, 7, 24, 4, 30, 26, 1888)
    releasemeta_1.cover_art_presence = 'present'
    session.add(releasemeta_1)

    releasegroupmeta_1 = ReleaseGroupMeta()
    releasegroupmeta_1.release_count = 1
    releasegroupmeta_1.first_release_date_year = 2007
    releasegroupmeta_1.first_release_date_month = 3
    releasegroupmeta_1.first_release_date_day = 23
    releasegroupmeta_1.rating = 40
    releasegroupmeta_1.rating_count = 1
    session.add(releasegroupmeta_1)

    releasegroupsecondarytype_compilation = ReleaseGroupSecondaryType()
    releasegroupsecondarytype_compilation.id = 1
    releasegroupsecondarytype_compilation.name = u'Compilation'
    releasegroupsecondarytype_compilation.child_order = 0
    releasegroupsecondarytype_compilation.gid = 'dd2a21e1-0c00-3729-a7a0-de60b84eb5d1'
    session.add(releasegroupsecondarytype_compilation)

    releasegroupsecondarytypejoin_1 = ReleaseGroupSecondaryTypeJoin()
    releasegroupsecondarytypejoin_1.created = datetime.datetime(2012, 5, 15, 0, 0)
    releasegroupsecondarytypejoin_1.secondary_type = releasegroupsecondarytype_compilation
    session.add(releasegroupsecondarytypejoin_1)

    releasegroupprimarytype_album = ReleaseGroupPrimaryType()
    releasegroupprimarytype_album.id = 1
    releasegroupprimarytype_album.name = u'Album'
    releasegroupprimarytype_album.child_order = 1
    releasegroupprimarytype_album.gid = 'f529b476-6e62-324f-b0aa-1f3e33d313fc'
    session.add(releasegroupprimarytype_album)

    releasegroup_trentemoller_the_polar_mix = ReleaseGroup()
    releasegroup_trentemoller_the_polar_mix.id = 633232
    releasegroup_trentemoller_the_polar_mix.gid = 'baca4e84-aa67-3ef9-adbe-0dfebe7b6a82'
    releasegroup_trentemoller_the_polar_mix.name = u'Trentem\xf8ller: The P\xf8lar Mix'
    releasegroup_trentemoller_the_polar_mix.comment = u''
    releasegroup_trentemoller_the_polar_mix.edits_pending = 0
    releasegroup_trentemoller_the_polar_mix.last_updated = datetime.datetime(2012, 5, 15, 19, 1, 58, 718541)
    releasegroup_trentemoller_the_polar_mix.artist_credit = artistcredit_trentemoller
    releasegroup_trentemoller_the_polar_mix.meta = releasegroupmeta_1
    releasegroup_trentemoller_the_polar_mix.secondary_types = [
        releasegroupsecondarytypejoin_1,
    ]
    releasegroup_trentemoller_the_polar_mix.type = releasegroupprimarytype_album
    session.add(releasegroup_trentemoller_the_polar_mix)

    script_latin = Script()
    script_latin.id = 28
    script_latin.iso_code = u'Latn'
    script_latin.iso_number = u'215'
    script_latin.name = u'Latin'
    script_latin.frequency = 4
    session.add(script_latin)

    releasestatus_promotion = ReleaseStatus()
    releasestatus_promotion.id = 2
    releasestatus_promotion.name = u'Promotion'
    releasestatus_promotion.child_order = 2
    releasestatus_promotion.description = u'A give-away release or a release intended to promote an upcoming official release (e.g. pre-release versions, releases included with a magazine, versions supplied to radio DJs for air-play).'
    releasestatus_promotion.gid = '518ffc83-5cde-34df-8627-81bff5093d92'
    session.add(releasestatus_promotion)

    release_trentemoller_the_polar_mix = Release()
    release_trentemoller_the_polar_mix.id = 291054
    release_trentemoller_the_polar_mix.gid = '89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149'
    release_trentemoller_the_polar_mix.name = u'Trentem\xf8ller: The P\xf8lar Mix'
    release_trentemoller_the_polar_mix.comment = u''
    release_trentemoller_the_polar_mix.edits_pending = 0
    release_trentemoller_the_polar_mix.quality = -1
    release_trentemoller_the_polar_mix.last_updated = datetime.datetime(2012, 10, 11, 6, 53, 15, 922324)
    release_trentemoller_the_polar_mix.artist_credit = artistcredit_trentemoller
    release_trentemoller_the_polar_mix.country_dates = [
        releasecountry_1,
    ]
    release_trentemoller_the_polar_mix.labels = [
        releaselabel_1,
    ]
    release_trentemoller_the_polar_mix.language = language_english
    release_trentemoller_the_polar_mix.mediums = [
        medium_1,
        medium_2,
    ]
    release_trentemoller_the_polar_mix.meta = releasemeta_1
    release_trentemoller_the_polar_mix.release_group = releasegroup_trentemoller_the_polar_mix
    release_trentemoller_the_polar_mix.script = script_latin
    release_trentemoller_the_polar_mix.status = releasestatus_promotion
    session.add(release_trentemoller_the_polar_mix)

    linktype_mix_dj = LinkType()
    linktype_mix_dj.id = 43
    linktype_mix_dj.child_order = 0
    linktype_mix_dj.gid = '9162dedd-790c-446c-838e-240f877dbfe2'
    linktype_mix_dj.entity_type0 = u'artist'
    linktype_mix_dj.entity_type1 = u'release'
    linktype_mix_dj.name = u'mix-DJ'
    linktype_mix_dj.description = u'This links a <a href="/doc/Mix_Terminology#DJ_mix">DJ-mix</a> to the artist who mixed it.'
    linktype_mix_dj.link_phrase = u'DJ-mixed {medium}'
    linktype_mix_dj.reverse_link_phrase = u'DJ-mixer {medium}'
    linktype_mix_dj.long_link_phrase = u'DJ-mixed {medium:% of}'
    linktype_mix_dj.priority = 0
    linktype_mix_dj.last_updated = datetime.datetime(2014, 5, 2, 11, 42, 42, 10843)
    linktype_mix_dj.is_deprecated = False
    linktype_mix_dj.has_dates = True
    linktype_mix_dj.entity0_cardinality = 1
    linktype_mix_dj.entity1_cardinality = 0
    session.add(linktype_mix_dj)

    link_8 = Link()
    link_8.id = 90
    link_8.attribute_count = 0
    link_8.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_8.ended = False
    link_8.link_type = linktype_mix_dj
    session.add(link_8)

    linkartistrelease_1 = LinkArtistRelease()
    linkartistrelease_1.id = 52649
    linkartistrelease_1.edits_pending = 0
    linkartistrelease_1.last_updated = datetime.datetime(2015, 8, 8, 10, 4, 9, 402935)
    linkartistrelease_1.link_order = 0
    linkartistrelease_1.entity0_credit = u''
    linkartistrelease_1.entity1_credit = u''
    linkartistrelease_1.entity0 = artist_trentemoller
    linkartistrelease_1.entity1 = release_trentemoller_the_polar_mix
    linkartistrelease_1.link = link_8
    session.add(linkartistrelease_1)

    url_4 = URL()
    url_4.id = 234836
    url_4.gid = '261acd6e-6025-4698-ac78-c8a3058c6d2c'
    url_4.url = u'http://www.discogs.com/release/986613'
    url_4.edits_pending = 0
    url_4.last_updated = datetime.datetime(2011, 5, 16, 16, 31, 52)
    session.add(url_4)

    linktype_discogs = LinkType()
    linktype_discogs.id = 76
    linktype_discogs.child_order = 0
    linktype_discogs.gid = '4a78823c-1c53-4176-a5f3-58026c76f2bc'
    linktype_discogs.entity_type0 = u'release'
    linktype_discogs.entity_type1 = u'url'
    linktype_discogs.name = u'discogs'
    linktype_discogs.description = u'This is used to link the Discogs page for this release.'
    linktype_discogs.link_phrase = u'Discogs'
    linktype_discogs.reverse_link_phrase = u'Discogs page for'
    linktype_discogs.long_link_phrase = u'has a Discogs page at'
    linktype_discogs.priority = 0
    linktype_discogs.last_updated = datetime.datetime(2014, 5, 24, 1, 42, 3, 623552)
    linktype_discogs.is_deprecated = False
    linktype_discogs.has_dates = False
    linktype_discogs.entity0_cardinality = 0
    linktype_discogs.entity1_cardinality = 0
    session.add(linktype_discogs)

    link_9 = Link()
    link_9.id = 6301
    link_9.attribute_count = 0
    link_9.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_9.ended = False
    link_9.link_type = linktype_discogs
    session.add(link_9)

    linkreleaseurl_1 = LinkReleaseURL()
    linkreleaseurl_1.id = 92637
    linkreleaseurl_1.edits_pending = 0
    linkreleaseurl_1.last_updated = datetime.datetime(2012, 5, 27, 11, 5, 54, 679406)
    linkreleaseurl_1.link_order = 0
    linkreleaseurl_1.entity0_credit = u''
    linkreleaseurl_1.entity1_credit = u''
    linkreleaseurl_1.entity0 = release_trentemoller_the_polar_mix
    linkreleaseurl_1.entity1 = url_4
    linkreleaseurl_1.link = link_9
    session.add(linkreleaseurl_1)

    artistmeta_25 = ArtistMeta()
    artistmeta_25.rating = 81
    artistmeta_25.rating_count = 21
    session.add(artistmeta_25)

    artisttype_other = ArtistType()
    artisttype_other.id = 3
    artisttype_other.name = u'Other'
    artisttype_other.child_order = 99
    artisttype_other.gid = 'ac897045-5043-3294-969b-187360e45d86'
    session.add(artisttype_other)

    artist_various_artists = Artist()
    artist_various_artists.id = 1
    artist_various_artists.gid = '89ad4ac3-39f7-470e-963a-56509c546377'
    artist_various_artists.name = u'Various Artists'
    artist_various_artists.sort_name = u'Various Artists'
    artist_various_artists.comment = u'add compilations to this artist'
    artist_various_artists.edits_pending = 0
    artist_various_artists.last_updated = datetime.datetime(2016, 5, 12, 7, 0, 27, 104853)
    artist_various_artists.ended = False
    artist_various_artists.meta = artistmeta_25
    artist_various_artists.type = artisttype_other
    session.add(artist_various_artists)

    artistcreditname_various_artists = ArtistCreditName()
    artistcreditname_various_artists.position = 0
    artistcreditname_various_artists.name = u'Various Artists'
    artistcreditname_various_artists.join_phrase = u''
    artistcreditname_various_artists.artist = artist_various_artists
    session.add(artistcreditname_various_artists)

    artistcredit_various_artists = ArtistCredit()
    artistcredit_various_artists.id = 1
    artistcredit_various_artists.name = u'Various Artists'
    artistcredit_various_artists.artist_count = 1
    artistcredit_various_artists.ref_count = 226104
    artistcredit_various_artists.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_various_artists.artists = [
        artistcreditname_various_artists,
    ]
    session.add(artistcredit_various_artists)

    countryarea_2 = CountryArea()
    countryarea_2.area = area_germany
    session.add(countryarea_2)

    releasecountry_2 = ReleaseCountry()
    releasecountry_2.date_year = 2009
    releasecountry_2.country = countryarea_2
    session.add(releasecountry_2)

    labelmeta_2 = LabelMeta()
    session.add(labelmeta_2)

    labeltype_imprint = LabelType()
    labeltype_imprint.id = 9
    labeltype_imprint.name = u'Imprint'
    labeltype_imprint.child_order = 0
    labeltype_imprint.gid = 'b6285b2a-3514-3d43-80df-fcf528824ded'
    session.add(labeltype_imprint)

    label_universal_music = Label()
    label_universal_music.id = 36455
    label_universal_music.gid = '13a464dc-b9fd-4d16-a4f4-d4316f6a46c7'
    label_universal_music.name = u'Universal Music'
    label_universal_music.label_code = 7340
    label_universal_music.comment = u'plain logo: "Universal Music"'
    label_universal_music.edits_pending = 0
    label_universal_music.last_updated = datetime.datetime(2015, 3, 18, 3, 16, 19, 962534)
    label_universal_music.ended = False
    label_universal_music.area = area_united_states
    label_universal_music.meta = labelmeta_2
    label_universal_music.type = labeltype_imprint
    session.add(label_universal_music)

    releaselabel_2 = ReleaseLabel()
    releaselabel_2.id = 533902
    releaselabel_2.catalog_number = u'4802220'
    releaselabel_2.last_updated = datetime.datetime(2016, 2, 11, 17, 28, 12, 203995)
    releaselabel_2.label = label_universal_music
    session.add(releaselabel_2)

    artistmeta_26 = ArtistMeta()
    session.add(artistmeta_26)

    artist_lawrence = Artist()
    artist_lawrence.id = 168462
    artist_lawrence.gid = '819a9744-627b-4bf5-92e9-f894b0f252e6'
    artist_lawrence.name = u'Lawrence'
    artist_lawrence.sort_name = u'Lawrence'
    artist_lawrence.comment = u'Electronic artist Peter M. Kersten'
    artist_lawrence.edits_pending = 0
    artist_lawrence.ended = False
    artist_lawrence.meta = artistmeta_26
    artist_lawrence.type = artisttype_person
    session.add(artist_lawrence)

    artistcreditname_lawrence = ArtistCreditName()
    artistcreditname_lawrence.position = 0
    artistcreditname_lawrence.name = u'Lawrence'
    artistcreditname_lawrence.join_phrase = u''
    artistcreditname_lawrence.artist = artist_lawrence
    session.add(artistcreditname_lawrence)

    artistcredit_lawrence = ArtistCredit()
    artistcredit_lawrence.id = 168462
    artistcredit_lawrence.name = u'Lawrence'
    artistcredit_lawrence.artist_count = 1
    artistcredit_lawrence.ref_count = 482
    artistcredit_lawrence.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_lawrence.artists = [
        artistcreditname_lawrence,
    ]
    session.add(artistcredit_lawrence)

    recordingmeta_26 = RecordingMeta()
    session.add(recordingmeta_26)

    recording_daydream = Recording()
    recording_daydream.id = 11935810
    recording_daydream.gid = 'a85d3576-389a-471c-8c90-c2c173f8cadf'
    recording_daydream.name = u'Daydream'
    recording_daydream.length = 199000
    recording_daydream.comment = u''
    recording_daydream.edits_pending = 0
    recording_daydream.video = False
    recording_daydream.artist_credit = artistcredit_lawrence
    recording_daydream.meta = recordingmeta_26
    session.add(recording_daydream)

    track_daydream = Track()
    track_daydream.id = 10364135
    track_daydream.gid = '250dbf09-ebad-3fa4-b152-d16b19e7f3b2'
    track_daydream.position = 1
    track_daydream.number = u'1'
    track_daydream.name = u'Daydream'
    track_daydream.length = 199000
    track_daydream.edits_pending = 0
    track_daydream.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_daydream.is_data_track = False
    track_daydream.artist_credit = artistcredit_lawrence
    track_daydream.recording = recording_daydream
    session.add(track_daydream)

    artistmeta_27 = ArtistMeta()
    session.add(artistmeta_27)

    artist_takeo_toyama = Artist()
    artist_takeo_toyama.id = 299529
    artist_takeo_toyama.gid = 'b2d731d0-252d-4842-9707-4f5c5247ee34'
    artist_takeo_toyama.name = u'Takeo Toyama'
    artist_takeo_toyama.sort_name = u'Toyama, Takeo'
    artist_takeo_toyama.comment = u''
    artist_takeo_toyama.edits_pending = 0
    artist_takeo_toyama.ended = False
    artist_takeo_toyama.meta = artistmeta_27
    artist_takeo_toyama.type = artisttype_person
    session.add(artist_takeo_toyama)

    artistcreditname_takeo_toyama = ArtistCreditName()
    artistcreditname_takeo_toyama.position = 0
    artistcreditname_takeo_toyama.name = u'Takeo Toyama'
    artistcreditname_takeo_toyama.join_phrase = u''
    artistcreditname_takeo_toyama.artist = artist_takeo_toyama
    session.add(artistcreditname_takeo_toyama)

    artistcredit_takeo_toyama = ArtistCredit()
    artistcredit_takeo_toyama.id = 299529
    artistcredit_takeo_toyama.name = u'Takeo Toyama'
    artistcredit_takeo_toyama.artist_count = 1
    artistcredit_takeo_toyama.ref_count = 33
    artistcredit_takeo_toyama.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_takeo_toyama.artists = [
        artistcreditname_takeo_toyama,
    ]
    session.add(artistcredit_takeo_toyama)

    recordingmeta_27 = RecordingMeta()
    session.add(recordingmeta_27)

    recording_lithium = Recording()
    recording_lithium.id = 11935811
    recording_lithium.gid = '4bbda17a-f2e2-4584-9a86-ac9254ea4a06'
    recording_lithium.name = u'Lithium'
    recording_lithium.length = 213000
    recording_lithium.comment = u''
    recording_lithium.edits_pending = 0
    recording_lithium.video = False
    recording_lithium.artist_credit = artistcredit_takeo_toyama
    recording_lithium.meta = recordingmeta_27
    session.add(recording_lithium)

    track_lithium = Track()
    track_lithium.id = 10364136
    track_lithium.gid = 'e1b6f5b7-d313-3ad0-a1f3-e38aed23f441'
    track_lithium.position = 2
    track_lithium.number = u'2'
    track_lithium.name = u'Lithium'
    track_lithium.length = 213000
    track_lithium.edits_pending = 0
    track_lithium.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_lithium.is_data_track = False
    track_lithium.artist_credit = artistcredit_takeo_toyama
    track_lithium.recording = recording_lithium
    session.add(track_lithium)

    area_kreuztal = Area()
    area_kreuztal.id = 69357
    area_kreuztal.gid = '7fcd3ea2-da7b-4dca-9025-9953bf2a8c13'
    area_kreuztal.name = u'Kreuztal'
    area_kreuztal.edits_pending = 0
    area_kreuztal.last_updated = datetime.datetime(2013, 11, 22, 14, 49, 26, 388436)
    area_kreuztal.ended = False
    area_kreuztal.comment = u''
    area_kreuztal.type = areatype_city
    session.add(area_kreuztal)

    iso31662_16 = ISO31662()
    iso31662_16.code = u'DE-NW'
    session.add(iso31662_16)

    area_nordrhein_westfalen = Area()
    area_nordrhein_westfalen.id = 334
    area_nordrhein_westfalen.gid = '1de7fa77-cb52-40a2-b82a-251c7818249d'
    area_nordrhein_westfalen.name = u'Nordrhein-Westfalen'
    area_nordrhein_westfalen.edits_pending = 0
    area_nordrhein_westfalen.last_updated = datetime.datetime(2013, 11, 23, 12, 27, 41, 902600)
    area_nordrhein_westfalen.ended = False
    area_nordrhein_westfalen.comment = u''
    area_nordrhein_westfalen.iso_3166_2_codes = [
        iso31662_16,
    ]
    area_nordrhein_westfalen.type = areatype_subdivision
    session.add(area_nordrhein_westfalen)

    linkareaarea_30 = LinkAreaArea()
    linkareaarea_30.id = 75
    linkareaarea_30.edits_pending = 0
    linkareaarea_30.last_updated = datetime.datetime(2013, 5, 17, 21, 35, 11, 33649)
    linkareaarea_30.link_order = 0
    linkareaarea_30.entity0_credit = u''
    linkareaarea_30.entity1_credit = u''
    linkareaarea_30.entity0 = area_germany
    linkareaarea_30.entity1 = area_nordrhein_westfalen
    linkareaarea_30.link = link_1
    session.add(linkareaarea_30)

    linkareaarea_29 = LinkAreaArea()
    linkareaarea_29.id = 69117
    linkareaarea_29.edits_pending = 0
    linkareaarea_29.last_updated = datetime.datetime(2013, 11, 8, 14, 37, 15, 208707)
    linkareaarea_29.link_order = 0
    linkareaarea_29.entity0_credit = u''
    linkareaarea_29.entity1_credit = u''
    linkareaarea_29.entity0 = area_nordrhein_westfalen
    linkareaarea_29.entity1 = area_kreuztal
    linkareaarea_29.link = link_1
    session.add(linkareaarea_29)

    artistmeta_28 = ArtistMeta()
    session.add(artistmeta_28)

    artist_hauschka = Artist()
    artist_hauschka.id = 299525
    artist_hauschka.gid = '767026a6-9e39-463b-9d04-ed0f86ac5ee7'
    artist_hauschka.name = u'Hauschka'
    artist_hauschka.sort_name = u'Hauschka'
    artist_hauschka.begin_date_year = 1966
    artist_hauschka.comment = u''
    artist_hauschka.edits_pending = 0
    artist_hauschka.last_updated = datetime.datetime(2015, 3, 24, 10, 19, 46, 859645)
    artist_hauschka.ended = False
    artist_hauschka.area = area_germany
    artist_hauschka.begin_area = area_kreuztal
    artist_hauschka.gender = gender_male
    artist_hauschka.meta = artistmeta_28
    artist_hauschka.type = artisttype_person
    session.add(artist_hauschka)

    artistcreditname_hauschka = ArtistCreditName()
    artistcreditname_hauschka.position = 0
    artistcreditname_hauschka.name = u'Hauschka'
    artistcreditname_hauschka.join_phrase = u''
    artistcreditname_hauschka.artist = artist_hauschka
    session.add(artistcreditname_hauschka)

    artistcredit_hauschka = ArtistCredit()
    artistcredit_hauschka.id = 299525
    artistcredit_hauschka.name = u'Hauschka'
    artistcredit_hauschka.artist_count = 1
    artistcredit_hauschka.ref_count = 497
    artistcredit_hauschka.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_hauschka.artists = [
        artistcreditname_hauschka,
    ]
    session.add(artistcredit_hauschka)

    recordingmeta_28 = RecordingMeta()
    session.add(recordingmeta_28)

    recording_zuhause = Recording()
    recording_zuhause.id = 11935812
    recording_zuhause.gid = '9b0d0b07-3775-4b68-93e2-073d05deadc4'
    recording_zuhause.name = u'Zuhause'
    recording_zuhause.length = 282000
    recording_zuhause.comment = u''
    recording_zuhause.edits_pending = 0
    recording_zuhause.video = False
    recording_zuhause.artist_credit = artistcredit_hauschka
    recording_zuhause.meta = recordingmeta_28
    session.add(recording_zuhause)

    track_zuhause = Track()
    track_zuhause.id = 10364137
    track_zuhause.gid = '7001c041-2e27-3825-93d5-b8293b8a08f1'
    track_zuhause.position = 3
    track_zuhause.number = u'3'
    track_zuhause.name = u'Zuhause'
    track_zuhause.length = 282000
    track_zuhause.edits_pending = 0
    track_zuhause.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_zuhause.is_data_track = False
    track_zuhause.artist_credit = artistcredit_hauschka
    track_zuhause.recording = recording_zuhause
    session.add(track_zuhause)

    iso31661_9 = ISO31661()
    iso31661_9.code = u'FR'
    session.add(iso31661_9)

    area_france = Area()
    area_france.id = 73
    area_france.gid = '08310658-51eb-3801-80de-5a0739207115'
    area_france.name = u'France'
    area_france.edits_pending = 0
    area_france.last_updated = datetime.datetime(2013, 5, 27, 12, 50, 32, 702645)
    area_france.ended = False
    area_france.comment = u''
    area_france.iso_3166_1_codes = [
        iso31661_9,
    ]
    area_france.type = areatype_country
    session.add(area_france)

    area_bayonne = Area()
    area_bayonne.id = 68462
    area_bayonne.gid = '7ab649d2-bc49-455d-9cdd-0084c5107f0b'
    area_bayonne.name = u'Bayonne'
    area_bayonne.edits_pending = 0
    area_bayonne.last_updated = datetime.datetime(2013, 11, 6, 18, 49, 29, 749851)
    area_bayonne.ended = False
    area_bayonne.comment = u''
    area_bayonne.type = areatype_city
    session.add(area_bayonne)

    iso31662_17 = ISO31662()
    iso31662_17.code = u'FR-64'
    session.add(iso31662_17)

    area_pyrenees_atlantiques = Area()
    area_pyrenees_atlantiques.id = 4423
    area_pyrenees_atlantiques.gid = '44054ea5-a713-4c6f-9830-ae22ed40eaec'
    area_pyrenees_atlantiques.name = u'Pyr\xe9n\xe9es-Atlantiques'
    area_pyrenees_atlantiques.edits_pending = 0
    area_pyrenees_atlantiques.last_updated = datetime.datetime(2013, 5, 22, 11, 27, 3, 852143)
    area_pyrenees_atlantiques.ended = False
    area_pyrenees_atlantiques.comment = u''
    area_pyrenees_atlantiques.iso_3166_2_codes = [
        iso31662_17,
    ]
    area_pyrenees_atlantiques.type = areatype_subdivision
    session.add(area_pyrenees_atlantiques)

    iso31662_18 = ISO31662()
    iso31662_18.code = u'FR-B'
    session.add(iso31662_18)

    area_aquitaine = Area()
    area_aquitaine.id = 1830
    area_aquitaine.gid = 'cd5b5aa5-d185-46e9-ad9d-e7c0eb8bc4c3'
    area_aquitaine.name = u'Aquitaine'
    area_aquitaine.edits_pending = 0
    area_aquitaine.last_updated = datetime.datetime(2013, 6, 5, 8, 6, 52, 206116)
    area_aquitaine.ended = False
    area_aquitaine.comment = u''
    area_aquitaine.iso_3166_2_codes = [
        iso31662_18,
    ]
    area_aquitaine.type = areatype_subdivision
    session.add(area_aquitaine)

    linkareaarea_33 = LinkAreaArea()
    linkareaarea_33.id = 1590
    linkareaarea_33.edits_pending = 0
    linkareaarea_33.last_updated = datetime.datetime(2013, 5, 20, 11, 59, 23, 660704)
    linkareaarea_33.link_order = 0
    linkareaarea_33.entity0_credit = u''
    linkareaarea_33.entity1_credit = u''
    linkareaarea_33.entity0 = area_france
    linkareaarea_33.entity1 = area_aquitaine
    linkareaarea_33.link = link_1
    session.add(linkareaarea_33)

    linkareaarea_32 = LinkAreaArea()
    linkareaarea_32.id = 4189
    linkareaarea_32.edits_pending = 0
    linkareaarea_32.last_updated = datetime.datetime(2013, 5, 22, 11, 27, 20, 874971)
    linkareaarea_32.link_order = 0
    linkareaarea_32.entity0_credit = u''
    linkareaarea_32.entity1_credit = u''
    linkareaarea_32.entity0 = area_aquitaine
    linkareaarea_32.entity1 = area_pyrenees_atlantiques
    linkareaarea_32.link = link_1
    session.add(linkareaarea_32)

    linkareaarea_31 = LinkAreaArea()
    linkareaarea_31.id = 68222
    linkareaarea_31.edits_pending = 0
    linkareaarea_31.last_updated = datetime.datetime(2013, 11, 6, 18, 49, 45, 756720)
    linkareaarea_31.link_order = 0
    linkareaarea_31.entity0_credit = u''
    linkareaarea_31.entity1_credit = u''
    linkareaarea_31.entity0 = area_pyrenees_atlantiques
    linkareaarea_31.entity1 = area_bayonne
    linkareaarea_31.link = link_1
    session.add(linkareaarea_31)

    artistipi_16 = ArtistIPI()
    artistipi_16.ipi = u'00152909075'
    artistipi_16.edits_pending = 0
    artistipi_16.created = datetime.datetime(2014, 1, 5, 17, 2, 13, 794235)
    session.add(artistipi_16)

    artistipi_17 = ArtistIPI()
    artistipi_17.ipi = u'00152909173'
    artistipi_17.edits_pending = 0
    artistipi_17.created = datetime.datetime(2014, 1, 5, 17, 2, 13, 794235)
    session.add(artistipi_17)

    artistisni_13 = ArtistISNI()
    artistisni_13.isni = u'0000000055255415'
    artistisni_13.edits_pending = 0
    artistisni_13.created = datetime.datetime(2014, 1, 5, 17, 2, 13, 794235)
    session.add(artistisni_13)

    artistmeta_29 = ArtistMeta()
    session.add(artistmeta_29)

    artist_sylvain_chauveau = Artist()
    artist_sylvain_chauveau.id = 139706
    artist_sylvain_chauveau.gid = 'e0443586-8830-4b7a-91c1-d6876c16d669'
    artist_sylvain_chauveau.name = u'Sylvain Chauveau'
    artist_sylvain_chauveau.sort_name = u'Chauveau, Sylvain'
    artist_sylvain_chauveau.begin_date_year = 1971
    artist_sylvain_chauveau.comment = u''
    artist_sylvain_chauveau.edits_pending = 0
    artist_sylvain_chauveau.last_updated = datetime.datetime(2015, 8, 30, 10, 2, 12, 397612)
    artist_sylvain_chauveau.ended = False
    artist_sylvain_chauveau.area = area_france
    artist_sylvain_chauveau.begin_area = area_bayonne
    artist_sylvain_chauveau.gender = gender_male
    artist_sylvain_chauveau.ipis = [
        artistipi_16,
        artistipi_17,
    ]
    artist_sylvain_chauveau.isnis = [
        artistisni_13,
    ]
    artist_sylvain_chauveau.meta = artistmeta_29
    artist_sylvain_chauveau.type = artisttype_person
    session.add(artist_sylvain_chauveau)

    artistcreditname_sylvain_chauveau = ArtistCreditName()
    artistcreditname_sylvain_chauveau.position = 0
    artistcreditname_sylvain_chauveau.name = u'Sylvain Chauveau'
    artistcreditname_sylvain_chauveau.join_phrase = u''
    artistcreditname_sylvain_chauveau.artist = artist_sylvain_chauveau
    session.add(artistcreditname_sylvain_chauveau)

    artistcredit_sylvain_chauveau = ArtistCredit()
    artistcredit_sylvain_chauveau.id = 139706
    artistcredit_sylvain_chauveau.name = u'Sylvain Chauveau'
    artistcredit_sylvain_chauveau.artist_count = 1
    artistcredit_sylvain_chauveau.ref_count = 369
    artistcredit_sylvain_chauveau.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_sylvain_chauveau.artists = [
        artistcreditname_sylvain_chauveau,
    ]
    session.add(artistcredit_sylvain_chauveau)

    recordingmeta_29 = RecordingMeta()
    session.add(recordingmeta_29)

    recording_il_fait_nuit_noire_a_berlin = Recording()
    recording_il_fait_nuit_noire_a_berlin.id = 11935813
    recording_il_fait_nuit_noire_a_berlin.gid = 'b69f3606-1e64-4e4a-bc54-18c6ccbf97f3'
    recording_il_fait_nuit_noire_a_berlin.name = u'Il Fait Nuit Noire \xc0 Berlin'
    recording_il_fait_nuit_noire_a_berlin.length = 127000
    recording_il_fait_nuit_noire_a_berlin.comment = u''
    recording_il_fait_nuit_noire_a_berlin.edits_pending = 0
    recording_il_fait_nuit_noire_a_berlin.video = False
    recording_il_fait_nuit_noire_a_berlin.artist_credit = artistcredit_sylvain_chauveau
    recording_il_fait_nuit_noire_a_berlin.meta = recordingmeta_29
    session.add(recording_il_fait_nuit_noire_a_berlin)

    track_il_fait_nuit_noire_a_berlin = Track()
    track_il_fait_nuit_noire_a_berlin.id = 10364138
    track_il_fait_nuit_noire_a_berlin.gid = '15d9ad31-48e5-34d9-aca4-ed428679e943'
    track_il_fait_nuit_noire_a_berlin.position = 4
    track_il_fait_nuit_noire_a_berlin.number = u'4'
    track_il_fait_nuit_noire_a_berlin.name = u'Il Fait Nuit Noire \xc0 Berlin'
    track_il_fait_nuit_noire_a_berlin.length = 127000
    track_il_fait_nuit_noire_a_berlin.edits_pending = 0
    track_il_fait_nuit_noire_a_berlin.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_il_fait_nuit_noire_a_berlin.is_data_track = False
    track_il_fait_nuit_noire_a_berlin.artist_credit = artistcredit_sylvain_chauveau
    track_il_fait_nuit_noire_a_berlin.recording = recording_il_fait_nuit_noire_a_berlin
    session.add(track_il_fait_nuit_noire_a_berlin)

    artistmeta_30 = ArtistMeta()
    session.add(artistmeta_30)

    artist_alva_noto_ryuichi_sakamoto = Artist()
    artist_alva_noto_ryuichi_sakamoto.id = 127630
    artist_alva_noto_ryuichi_sakamoto.gid = '6edc70bb-c340-4ae6-bdd4-d5fb0c7411de'
    artist_alva_noto_ryuichi_sakamoto.name = u'Alva Noto + Ryuichi Sakamoto'
    artist_alva_noto_ryuichi_sakamoto.sort_name = u'Noto, Alva + Sakamoto, Ryuichi'
    artist_alva_noto_ryuichi_sakamoto.comment = u''
    artist_alva_noto_ryuichi_sakamoto.edits_pending = 0
    artist_alva_noto_ryuichi_sakamoto.last_updated = datetime.datetime(2013, 1, 23, 19, 0, 17, 638468)
    artist_alva_noto_ryuichi_sakamoto.ended = False
    artist_alva_noto_ryuichi_sakamoto.meta = artistmeta_30
    artist_alva_noto_ryuichi_sakamoto.type = artisttype_group
    session.add(artist_alva_noto_ryuichi_sakamoto)

    artistcreditname_alva_noto_ryuichi_sakamoto = ArtistCreditName()
    artistcreditname_alva_noto_ryuichi_sakamoto.position = 0
    artistcreditname_alva_noto_ryuichi_sakamoto.name = u'Alva Noto & Ryuichi Sakamoto'
    artistcreditname_alva_noto_ryuichi_sakamoto.join_phrase = u''
    artistcreditname_alva_noto_ryuichi_sakamoto.artist = artist_alva_noto_ryuichi_sakamoto
    session.add(artistcreditname_alva_noto_ryuichi_sakamoto)

    artistcredit_alva_noto_ryuichi_sakamoto = ArtistCredit()
    artistcredit_alva_noto_ryuichi_sakamoto.id = 127630
    artistcredit_alva_noto_ryuichi_sakamoto.name = u'Alva Noto & Ryuichi Sakamoto'
    artistcredit_alva_noto_ryuichi_sakamoto.artist_count = 1
    artistcredit_alva_noto_ryuichi_sakamoto.ref_count = 66
    artistcredit_alva_noto_ryuichi_sakamoto.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_alva_noto_ryuichi_sakamoto.artists = [
        artistcreditname_alva_noto_ryuichi_sakamoto,
    ]
    session.add(artistcredit_alva_noto_ryuichi_sakamoto)

    recordingmeta_30 = RecordingMeta()
    session.add(recordingmeta_30)

    recording_moon = Recording()
    recording_moon.id = 11935814
    recording_moon.gid = '7853bd8c-2141-4b4d-9f62-578bab214ab9'
    recording_moon.name = u'Moon'
    recording_moon.length = 367000
    recording_moon.comment = u''
    recording_moon.edits_pending = 0
    recording_moon.video = False
    recording_moon.artist_credit = artistcredit_alva_noto_ryuichi_sakamoto
    recording_moon.meta = recordingmeta_30
    session.add(recording_moon)

    track_moon = Track()
    track_moon.id = 10364139
    track_moon.gid = '4e7da4ee-d2a4-379f-9619-699fe23124a2'
    track_moon.position = 5
    track_moon.number = u'5'
    track_moon.name = u'Moon'
    track_moon.length = 367000
    track_moon.edits_pending = 0
    track_moon.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_moon.is_data_track = False
    track_moon.artist_credit = artistcredit_alva_noto_ryuichi_sakamoto
    track_moon.recording = recording_moon
    session.add(track_moon)

    area_cologne = Area()
    area_cologne.id = 7954
    area_cologne.gid = 'b8a2776a-eedf-48ea-a6f3-1a9070f0b823'
    area_cologne.name = u'Cologne'
    area_cologne.edits_pending = 0
    area_cologne.last_updated = datetime.datetime(2013, 11, 26, 6, 59, 1, 235384)
    area_cologne.ended = False
    area_cologne.comment = u''
    area_cologne.type = areatype_city
    session.add(area_cologne)

    linkareaarea_34 = LinkAreaArea()
    linkareaarea_34.id = 7720
    linkareaarea_34.edits_pending = 0
    linkareaarea_34.last_updated = datetime.datetime(2013, 5, 29, 8, 23, 25, 429047)
    linkareaarea_34.link_order = 0
    linkareaarea_34.entity0_credit = u''
    linkareaarea_34.entity1_credit = u''
    linkareaarea_34.entity0 = area_nordrhein_westfalen
    linkareaarea_34.entity1 = area_cologne
    linkareaarea_34.link = link_1
    session.add(linkareaarea_34)

    artistisni_14 = ArtistISNI()
    artistisni_14.isni = u'0000000066303400'
    artistisni_14.edits_pending = 0
    artistisni_14.created = datetime.datetime(2015, 8, 9, 6, 14, 43, 667083)
    session.add(artistisni_14)

    artistmeta_31 = ArtistMeta()
    artistmeta_31.rating = 100
    artistmeta_31.rating_count = 1
    session.add(artistmeta_31)

    artist_gas = Artist()
    artist_gas.id = 51632
    artist_gas.gid = '054b0483-eeb8-48ce-bb72-f1cb57ff44f9'
    artist_gas.name = u'Gas'
    artist_gas.sort_name = u'Gas'
    artist_gas.begin_date_year = 1961
    artist_gas.comment = u'German electronic producer Wolfgang Voigt'
    artist_gas.edits_pending = 0
    artist_gas.last_updated = datetime.datetime(2016, 4, 13, 19, 6, 32, 109363)
    artist_gas.ended = False
    artist_gas.area = area_germany
    artist_gas.begin_area = area_cologne
    artist_gas.gender = gender_male
    artist_gas.isnis = [
        artistisni_14,
    ]
    artist_gas.meta = artistmeta_31
    artist_gas.type = artisttype_person
    session.add(artist_gas)

    artistcreditname_gas = ArtistCreditName()
    artistcreditname_gas.position = 0
    artistcreditname_gas.name = u'Gas'
    artistcreditname_gas.join_phrase = u''
    artistcreditname_gas.artist = artist_gas
    session.add(artistcreditname_gas)

    artistcredit_gas = ArtistCredit()
    artistcredit_gas.id = 51632
    artistcredit_gas.name = u'Gas'
    artistcredit_gas.artist_count = 1
    artistcredit_gas.ref_count = 244
    artistcredit_gas.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_gas.artists = [
        artistcreditname_gas,
    ]
    session.add(artistcredit_gas)

    recordingmeta_31 = RecordingMeta()
    session.add(recordingmeta_31)

    recording_zauberberg_iv = Recording()
    recording_zauberberg_iv.id = 11935815
    recording_zauberberg_iv.gid = '60a8fedc-993f-45b2-8b8e-f585c52f6481'
    recording_zauberberg_iv.name = u'Zauberberg IV'
    recording_zauberberg_iv.length = 356000
    recording_zauberberg_iv.comment = u''
    recording_zauberberg_iv.edits_pending = 0
    recording_zauberberg_iv.video = False
    recording_zauberberg_iv.artist_credit = artistcredit_gas
    recording_zauberberg_iv.meta = recordingmeta_31
    session.add(recording_zauberberg_iv)

    track_zauberberg_iv = Track()
    track_zauberberg_iv.id = 10364140
    track_zauberberg_iv.gid = '4258655a-0271-3a63-a61b-53ba29d3b2f8'
    track_zauberberg_iv.position = 6
    track_zauberberg_iv.number = u'6'
    track_zauberberg_iv.name = u'Zauberberg IV'
    track_zauberberg_iv.length = 356000
    track_zauberberg_iv.edits_pending = 0
    track_zauberberg_iv.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_zauberberg_iv.is_data_track = False
    track_zauberberg_iv.artist_credit = artistcredit_gas
    track_zauberberg_iv.recording = recording_zauberberg_iv
    session.add(track_zauberberg_iv)

    area_mississauga = Area()
    area_mississauga.id = 70247
    area_mississauga.gid = '23b82a5a-5a5e-4b62-ab84-5222a8e443cd'
    area_mississauga.name = u'Mississauga'
    area_mississauga.edits_pending = 0
    area_mississauga.last_updated = datetime.datetime(2013, 11, 9, 1, 15, 54, 293695)
    area_mississauga.ended = False
    area_mississauga.comment = u''
    area_mississauga.type = areatype_city
    session.add(area_mississauga)

    iso31662_19 = ISO31662()
    iso31662_19.code = u'CA-ON'
    session.add(iso31662_19)

    area_ontario = Area()
    area_ontario.id = 320
    area_ontario.gid = '2747553f-b44d-44c4-a7c3-b67412b6f10b'
    area_ontario.name = u'Ontario'
    area_ontario.edits_pending = 0
    area_ontario.last_updated = datetime.datetime(2013, 5, 17, 21, 29, 46, 963224)
    area_ontario.ended = False
    area_ontario.comment = u''
    area_ontario.iso_3166_2_codes = [
        iso31662_19,
    ]
    area_ontario.type = areatype_subdivision
    session.add(area_ontario)

    linkareaarea_36 = LinkAreaArea()
    linkareaarea_36.id = 61
    linkareaarea_36.edits_pending = 0
    linkareaarea_36.last_updated = datetime.datetime(2013, 5, 17, 21, 29, 55, 817130)
    linkareaarea_36.link_order = 0
    linkareaarea_36.entity0_credit = u''
    linkareaarea_36.entity1_credit = u''
    linkareaarea_36.entity0 = area_canada
    linkareaarea_36.entity1 = area_ontario
    linkareaarea_36.link = link_1
    session.add(linkareaarea_36)

    linkareaarea_35 = LinkAreaArea()
    linkareaarea_35.id = 70007
    linkareaarea_35.edits_pending = 0
    linkareaarea_35.last_updated = datetime.datetime(2013, 11, 9, 1, 16, 10, 45259)
    linkareaarea_35.link_order = 0
    linkareaarea_35.entity0_credit = u''
    linkareaarea_35.entity1_credit = u''
    linkareaarea_35.entity0 = area_ontario
    linkareaarea_35.entity1 = area_mississauga
    linkareaarea_35.link = link_1
    session.add(linkareaarea_35)

    artistmeta_32 = ArtistMeta()
    session.add(artistmeta_32)

    artist_final_fantasy = Artist()
    artist_final_fantasy.id = 238993
    artist_final_fantasy.gid = 'dcbd7e51-de76-47d6-aadc-7e38b779f82d'
    artist_final_fantasy.name = u'Final Fantasy'
    artist_final_fantasy.sort_name = u'Final Fantasy'
    artist_final_fantasy.begin_date_year = 1979
    artist_final_fantasy.begin_date_month = 9
    artist_final_fantasy.begin_date_day = 7
    artist_final_fantasy.comment = u'Canadian indie pop, Owen Pallett'
    artist_final_fantasy.edits_pending = 0
    artist_final_fantasy.last_updated = datetime.datetime(2015, 6, 14, 7, 21, 51, 132143)
    artist_final_fantasy.ended = False
    artist_final_fantasy.area = area_canada
    artist_final_fantasy.begin_area = area_mississauga
    artist_final_fantasy.gender = gender_male
    artist_final_fantasy.meta = artistmeta_32
    artist_final_fantasy.type = artisttype_person
    session.add(artist_final_fantasy)

    artistcreditname_final_fantasy = ArtistCreditName()
    artistcreditname_final_fantasy.position = 0
    artistcreditname_final_fantasy.name = u'Final Fantasy'
    artistcreditname_final_fantasy.join_phrase = u''
    artistcreditname_final_fantasy.artist = artist_final_fantasy
    session.add(artistcreditname_final_fantasy)

    artistcredit_final_fantasy = ArtistCredit()
    artistcredit_final_fantasy.id = 238993
    artistcredit_final_fantasy.name = u'Final Fantasy'
    artistcredit_final_fantasy.artist_count = 1
    artistcredit_final_fantasy.ref_count = 284
    artistcredit_final_fantasy.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_final_fantasy.artists = [
        artistcreditname_final_fantasy,
    ]
    session.add(artistcredit_final_fantasy)

    recordingmeta_32 = RecordingMeta()
    session.add(recordingmeta_32)

    recording_he_poos_clouds = Recording()
    recording_he_poos_clouds.id = 11935816
    recording_he_poos_clouds.gid = '85948a43-b1f8-4d4e-8c16-0b5fae69ddc3'
    recording_he_poos_clouds.name = u'He Poos Clouds'
    recording_he_poos_clouds.length = 211840
    recording_he_poos_clouds.comment = u''
    recording_he_poos_clouds.edits_pending = 0
    recording_he_poos_clouds.last_updated = datetime.datetime(2014, 4, 21, 18, 22, 14, 890359)
    recording_he_poos_clouds.video = False
    recording_he_poos_clouds.artist_credit = artistcredit_final_fantasy
    recording_he_poos_clouds.meta = recordingmeta_32
    session.add(recording_he_poos_clouds)

    workmeta_5 = WorkMeta()
    session.add(workmeta_5)

    work_he_poos_clouds = Work()
    work_he_poos_clouds.id = 12642856
    work_he_poos_clouds.gid = '5cc3e760-bcab-4721-995e-7950807e045b'
    work_he_poos_clouds.name = u'He Poos Clouds'
    work_he_poos_clouds.comment = u''
    work_he_poos_clouds.edits_pending = 0
    work_he_poos_clouds.last_updated = datetime.datetime(2013, 8, 1, 12, 5, 51, 364186)
    work_he_poos_clouds.meta = workmeta_5
    work_he_poos_clouds.type = worktype_song
    session.add(work_he_poos_clouds)

    artistisni_15 = ArtistISNI()
    artistisni_15.isni = u'0000000115052426'
    artistisni_15.edits_pending = 0
    artistisni_15.created = datetime.datetime(2015, 6, 14, 8, 39, 26, 86442)
    session.add(artistisni_15)

    artistmeta_33 = ArtistMeta()
    session.add(artistmeta_33)

    artist_owen_pallett = Artist()
    artist_owen_pallett.id = 238992
    artist_owen_pallett.gid = '6d394418-a565-4c16-9dec-f5a89e213cde'
    artist_owen_pallett.name = u'Owen Pallett'
    artist_owen_pallett.sort_name = u'Pallett, Owen'
    artist_owen_pallett.begin_date_year = 1979
    artist_owen_pallett.begin_date_month = 9
    artist_owen_pallett.begin_date_day = 7
    artist_owen_pallett.comment = u''
    artist_owen_pallett.edits_pending = 0
    artist_owen_pallett.last_updated = datetime.datetime(2015, 6, 14, 8, 39, 26, 86442)
    artist_owen_pallett.ended = False
    artist_owen_pallett.area = area_canada
    artist_owen_pallett.begin_area = area_mississauga
    artist_owen_pallett.gender = gender_male
    artist_owen_pallett.isnis = [
        artistisni_15,
    ]
    artist_owen_pallett.meta = artistmeta_33
    artist_owen_pallett.type = artisttype_person
    session.add(artist_owen_pallett)

    linkartistwork_14 = LinkArtistWork()
    linkartistwork_14.id = 785337
    linkartistwork_14.edits_pending = 0
    linkartistwork_14.last_updated = datetime.datetime(2013, 8, 1, 12, 10, 4, 859337)
    linkartistwork_14.link_order = 0
    linkartistwork_14.entity0_credit = u''
    linkartistwork_14.entity1_credit = u''
    linkartistwork_14.entity0 = artist_owen_pallett
    linkartistwork_14.entity1 = work_he_poos_clouds
    linkartistwork_14.link = link_2
    session.add(linkartistwork_14)

    linkartistwork_15 = LinkArtistWork()
    linkartistwork_15.id = 785336
    linkartistwork_15.edits_pending = 0
    linkartistwork_15.last_updated = datetime.datetime(2013, 8, 1, 12, 10, 4, 859337)
    linkartistwork_15.link_order = 0
    linkartistwork_15.entity0_credit = u''
    linkartistwork_15.entity1_credit = u''
    linkartistwork_15.entity0 = artist_owen_pallett
    linkartistwork_15.entity1 = work_he_poos_clouds
    linkartistwork_15.link = link_3
    session.add(linkartistwork_15)

    linkrecordingwork_5 = LinkRecordingWork()
    linkrecordingwork_5.id = 1132131
    linkrecordingwork_5.edits_pending = 0
    linkrecordingwork_5.last_updated = datetime.datetime(2013, 8, 8, 13, 0, 42, 88409)
    linkrecordingwork_5.link_order = 0
    linkrecordingwork_5.entity0_credit = u''
    linkrecordingwork_5.entity1_credit = u''
    linkrecordingwork_5.entity0 = recording_he_poos_clouds
    linkrecordingwork_5.entity1 = work_he_poos_clouds
    linkrecordingwork_5.link = link_6
    session.add(linkrecordingwork_5)

    track_he_poos_clouds = Track()
    track_he_poos_clouds.id = 10364141
    track_he_poos_clouds.gid = '59b034d9-1bcb-32be-8890-f1f555a279aa'
    track_he_poos_clouds.position = 7
    track_he_poos_clouds.number = u'7'
    track_he_poos_clouds.name = u'He Poos Clouds'
    track_he_poos_clouds.length = 211000
    track_he_poos_clouds.edits_pending = 0
    track_he_poos_clouds.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_he_poos_clouds.is_data_track = False
    track_he_poos_clouds.artist_credit = artistcredit_final_fantasy
    track_he_poos_clouds.recording = recording_he_poos_clouds
    session.add(track_he_poos_clouds)

    iso31661_10 = ISO31661()
    iso31661_10.code = u'LU'
    session.add(iso31661_10)

    area_luxembourg = Area()
    area_luxembourg.id = 124
    area_luxembourg.gid = '563d21b7-4a8e-35e2-83a7-7804baefbfa7'
    area_luxembourg.name = u'Luxembourg'
    area_luxembourg.edits_pending = 0
    area_luxembourg.last_updated = datetime.datetime(2013, 5, 27, 13, 51, 12, 674706)
    area_luxembourg.ended = False
    area_luxembourg.comment = u''
    area_luxembourg.iso_3166_1_codes = [
        iso31661_10,
    ]
    area_luxembourg.type = areatype_country
    session.add(area_luxembourg)

    artistmeta_34 = ArtistMeta()
    session.add(artistmeta_34)

    artist_francesco_tristano = Artist()
    artist_francesco_tristano.id = 314969
    artist_francesco_tristano.gid = 'c2de59ca-07b1-431f-b946-e3e5421ede63'
    artist_francesco_tristano.name = u'Francesco Tristano'
    artist_francesco_tristano.sort_name = u'Tristano, Francesco'
    artist_francesco_tristano.begin_date_year = 1981
    artist_francesco_tristano.begin_date_month = 9
    artist_francesco_tristano.begin_date_day = 16
    artist_francesco_tristano.comment = u''
    artist_francesco_tristano.edits_pending = 0
    artist_francesco_tristano.last_updated = datetime.datetime(2015, 8, 7, 3, 8, 33, 544925)
    artist_francesco_tristano.ended = False
    artist_francesco_tristano.area = area_luxembourg
    artist_francesco_tristano.gender = gender_male
    artist_francesco_tristano.meta = artistmeta_34
    artist_francesco_tristano.type = artisttype_person
    session.add(artist_francesco_tristano)

    artistcreditname_francesco_tristano = ArtistCreditName()
    artistcreditname_francesco_tristano.position = 0
    artistcreditname_francesco_tristano.name = u'Francesco Tristano'
    artistcreditname_francesco_tristano.join_phrase = u''
    artistcreditname_francesco_tristano.artist = artist_francesco_tristano
    session.add(artistcreditname_francesco_tristano)

    artistcredit_francesco_tristano = ArtistCredit()
    artistcredit_francesco_tristano.id = 314969
    artistcredit_francesco_tristano.name = u'Francesco Tristano'
    artistcredit_francesco_tristano.artist_count = 1
    artistcredit_francesco_tristano.ref_count = 144
    artistcredit_francesco_tristano.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_francesco_tristano.artists = [
        artistcreditname_francesco_tristano,
    ]
    session.add(artistcredit_francesco_tristano)

    recordingmeta_33 = RecordingMeta()
    session.add(recordingmeta_33)

    recording_andover = Recording()
    recording_andover.id = 11935817
    recording_andover.gid = 'd75efd42-2c10-45ad-b1ce-74aea4ef508f'
    recording_andover.name = u'Andover'
    recording_andover.length = 373000
    recording_andover.comment = u''
    recording_andover.edits_pending = 0
    recording_andover.video = False
    recording_andover.artist_credit = artistcredit_francesco_tristano
    recording_andover.meta = recordingmeta_33
    session.add(recording_andover)

    track_andover = Track()
    track_andover.id = 10364142
    track_andover.gid = 'c55d9055-290c-3638-bb84-f330d42cfe6e'
    track_andover.position = 8
    track_andover.number = u'8'
    track_andover.name = u'Andover'
    track_andover.length = 373000
    track_andover.edits_pending = 0
    track_andover.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_andover.is_data_track = False
    track_andover.artist_credit = artistcredit_francesco_tristano
    track_andover.recording = recording_andover
    session.add(track_andover)

    area_baltimore = Area()
    area_baltimore.id = 5148
    area_baltimore.gid = '2fb5445d-3987-49fe-957a-f730a7acc4a2'
    area_baltimore.name = u'Baltimore'
    area_baltimore.edits_pending = 0
    area_baltimore.last_updated = datetime.datetime(2013, 5, 24, 20, 36, 45, 29411)
    area_baltimore.ended = False
    area_baltimore.comment = u''
    area_baltimore.type = areatype_city
    session.add(area_baltimore)

    iso31662_20 = ISO31662()
    iso31662_20.code = u'US-MD'
    session.add(iso31662_20)

    area_maryland = Area()
    area_maryland.id = 261
    area_maryland.gid = '1ed51cbe-4272-4df9-9b18-44b0d4714086'
    area_maryland.name = u'Maryland'
    area_maryland.edits_pending = 0
    area_maryland.last_updated = datetime.datetime(2013, 5, 17, 20, 5, 30, 115942)
    area_maryland.ended = False
    area_maryland.comment = u''
    area_maryland.iso_3166_2_codes = [
        iso31662_20,
    ]
    area_maryland.type = areatype_subdivision
    session.add(area_maryland)

    linkareaarea_38 = LinkAreaArea()
    linkareaarea_38.id = 1
    linkareaarea_38.edits_pending = 0
    linkareaarea_38.last_updated = datetime.datetime(2013, 5, 17, 20, 7, 10, 420660)
    linkareaarea_38.link_order = 0
    linkareaarea_38.entity0_credit = u''
    linkareaarea_38.entity1_credit = u''
    linkareaarea_38.entity0 = area_united_states
    linkareaarea_38.entity1 = area_maryland
    linkareaarea_38.link = link_1
    session.add(linkareaarea_38)

    linkareaarea_37 = LinkAreaArea()
    linkareaarea_37.id = 4914
    linkareaarea_37.edits_pending = 0
    linkareaarea_37.last_updated = datetime.datetime(2013, 5, 24, 20, 36, 53, 493341)
    linkareaarea_37.link_order = 0
    linkareaarea_37.entity0_credit = u''
    linkareaarea_37.entity1_credit = u''
    linkareaarea_37.entity0 = area_maryland
    linkareaarea_37.entity1 = area_baltimore
    linkareaarea_37.link = link_1
    session.add(linkareaarea_37)

    artistipi_18 = ArtistIPI()
    artistipi_18.ipi = u'00012034058'
    artistipi_18.edits_pending = 0
    artistipi_18.created = datetime.datetime(2013, 3, 26, 17, 40, 13, 338175)
    session.add(artistipi_18)

    artistipi_19 = ArtistIPI()
    artistipi_19.ipi = u'00125609583'
    artistipi_19.edits_pending = 0
    artistipi_19.created = datetime.datetime(2013, 3, 26, 17, 40, 13, 338175)
    session.add(artistipi_19)

    artistisni_16 = ArtistISNI()
    artistisni_16.isni = u'0000000121367029'
    artistisni_16.edits_pending = 0
    artistisni_16.created = datetime.datetime(2013, 10, 12, 16, 52, 44, 358667)
    session.add(artistisni_16)

    artistmeta_35 = ArtistMeta()
    artistmeta_35.rating = 95
    artistmeta_35.rating_count = 8
    session.add(artistmeta_35)

    artist_philip_glass = Artist()
    artist_philip_glass.id = 9193
    artist_philip_glass.gid = '5ae54dee-4dba-49c0-802a-a3b3b3adfe9b'
    artist_philip_glass.name = u'Philip Glass'
    artist_philip_glass.sort_name = u'Glass, Philip'
    artist_philip_glass.begin_date_year = 1937
    artist_philip_glass.begin_date_month = 1
    artist_philip_glass.begin_date_day = 31
    artist_philip_glass.comment = u''
    artist_philip_glass.edits_pending = 0
    artist_philip_glass.last_updated = datetime.datetime(2014, 7, 12, 22, 0, 38, 753933)
    artist_philip_glass.ended = False
    artist_philip_glass.area = area_united_states
    artist_philip_glass.begin_area = area_baltimore
    artist_philip_glass.gender = gender_male
    artist_philip_glass.ipis = [
        artistipi_18,
        artistipi_19,
    ]
    artist_philip_glass.isnis = [
        artistisni_16,
    ]
    artist_philip_glass.meta = artistmeta_35
    artist_philip_glass.type = artisttype_person
    session.add(artist_philip_glass)

    artistcreditname_philip_glass = ArtistCreditName()
    artistcreditname_philip_glass.position = 0
    artistcreditname_philip_glass.name = u'Philip Glass'
    artistcreditname_philip_glass.join_phrase = u''
    artistcreditname_philip_glass.artist = artist_philip_glass
    session.add(artistcreditname_philip_glass)

    artistcredit_philip_glass = ArtistCredit()
    artistcredit_philip_glass.id = 9193
    artistcredit_philip_glass.name = u'Philip Glass'
    artistcredit_philip_glass.artist_count = 1
    artistcredit_philip_glass.ref_count = 5746
    artistcredit_philip_glass.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_philip_glass.artists = [
        artistcreditname_philip_glass,
    ]
    session.add(artistcredit_philip_glass)

    recordingmeta_34 = RecordingMeta()
    session.add(recordingmeta_34)

    recording_abdulmajid = Recording()
    recording_abdulmajid.id = 11935818
    recording_abdulmajid.gid = '1fc199e0-9ca9-4c0b-a85a-f13ce581697f'
    recording_abdulmajid.name = u'Abdulmajid'
    recording_abdulmajid.length = 531000
    recording_abdulmajid.comment = u''
    recording_abdulmajid.edits_pending = 0
    recording_abdulmajid.video = False
    recording_abdulmajid.artist_credit = artistcredit_philip_glass
    recording_abdulmajid.meta = recordingmeta_34
    session.add(recording_abdulmajid)

    workmeta_6 = WorkMeta()
    session.add(workmeta_6)

    work_symphony_no_4_heroes_ii_abdulmajid = Work()
    work_symphony_no_4_heroes_ii_abdulmajid.id = 12435493
    work_symphony_no_4_heroes_ii_abdulmajid.gid = '1b941c6e-695c-4b93-ae6e-c3a97fa8663c'
    work_symphony_no_4_heroes_ii_abdulmajid.name = u'Symphony no. 4 "Heroes": II. Abdulmajid'
    work_symphony_no_4_heroes_ii_abdulmajid.comment = u''
    work_symphony_no_4_heroes_ii_abdulmajid.edits_pending = 0
    work_symphony_no_4_heroes_ii_abdulmajid.last_updated = datetime.datetime(2013, 3, 16, 14, 41, 6, 852092)
    work_symphony_no_4_heroes_ii_abdulmajid.meta = workmeta_6
    session.add(work_symphony_no_4_heroes_ii_abdulmajid)

    linkartistwork_16 = LinkArtistWork()
    linkartistwork_16.id = 459002
    linkartistwork_16.edits_pending = 0
    linkartistwork_16.last_updated = datetime.datetime(2011, 8, 26, 9, 31, 8, 130993)
    linkartistwork_16.link_order = 0
    linkartistwork_16.entity0_credit = u''
    linkartistwork_16.entity1_credit = u''
    linkartistwork_16.entity0 = artist_philip_glass
    linkartistwork_16.entity1 = work_symphony_no_4_heroes_ii_abdulmajid
    linkartistwork_16.link = link_3
    session.add(linkartistwork_16)

    linkrecordingwork_6 = LinkRecordingWork()
    linkrecordingwork_6.id = 1545288
    linkrecordingwork_6.edits_pending = 0
    linkrecordingwork_6.last_updated = datetime.datetime(2014, 11, 28, 6, 38, 57, 795684)
    linkrecordingwork_6.link_order = 0
    linkrecordingwork_6.entity0_credit = u''
    linkrecordingwork_6.entity1_credit = u''
    linkrecordingwork_6.entity0 = recording_abdulmajid
    linkrecordingwork_6.entity1 = work_symphony_no_4_heroes_ii_abdulmajid
    linkrecordingwork_6.link = link_6
    session.add(linkrecordingwork_6)

    track_abdulmajid = Track()
    track_abdulmajid.id = 10364143
    track_abdulmajid.gid = 'ae3a985f-835a-3c42-9b25-c1d7a56082e2'
    track_abdulmajid.position = 9
    track_abdulmajid.number = u'9'
    track_abdulmajid.name = u'Abdulmajid'
    track_abdulmajid.length = 531000
    track_abdulmajid.edits_pending = 0
    track_abdulmajid.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_abdulmajid.is_data_track = False
    track_abdulmajid.artist_credit = artistcredit_philip_glass
    track_abdulmajid.recording = recording_abdulmajid
    session.add(track_abdulmajid)

    recordingmeta_35 = RecordingMeta()
    session.add(recordingmeta_35)

    recording_maiz = Recording()
    recording_maiz.id = 11935819
    recording_maiz.gid = '66fd5822-107b-46a1-b11f-fd7eafd427d1'
    recording_maiz.name = u'Maiz'
    recording_maiz.length = 364000
    recording_maiz.comment = u''
    recording_maiz.edits_pending = 0
    recording_maiz.video = False
    recording_maiz.artist_credit = artistcredit_murcof
    recording_maiz.meta = recordingmeta_35
    session.add(recording_maiz)

    track_maiz = Track()
    track_maiz.id = 10364144
    track_maiz.gid = 'a8113c95-e21c-309d-9227-445dfe39e0bb'
    track_maiz.position = 10
    track_maiz.number = u'10'
    track_maiz.name = u'Maiz'
    track_maiz.length = 364000
    track_maiz.edits_pending = 0
    track_maiz.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_maiz.is_data_track = False
    track_maiz.artist_credit = artistcredit_murcof
    track_maiz.recording = recording_maiz
    session.add(track_maiz)

    artistmeta_36 = ArtistMeta()
    session.add(artistmeta_36)

    artist_slowcream = Artist()
    artist_slowcream.id = 775683
    artist_slowcream.gid = '27bc6454-5046-4066-8fe6-977190211880'
    artist_slowcream.name = u'Slowcream'
    artist_slowcream.sort_name = u'Slowcream'
    artist_slowcream.comment = u''
    artist_slowcream.edits_pending = 0
    artist_slowcream.last_updated = datetime.datetime(2011, 1, 1, 21, 3, 35, 272282)
    artist_slowcream.ended = False
    artist_slowcream.meta = artistmeta_36
    artist_slowcream.type = artisttype_person
    session.add(artist_slowcream)

    artistcreditname_slowcream = ArtistCreditName()
    artistcreditname_slowcream.position = 0
    artistcreditname_slowcream.name = u'Slowcream'
    artistcreditname_slowcream.join_phrase = u''
    artistcreditname_slowcream.artist = artist_slowcream
    session.add(artistcreditname_slowcream)

    artistcredit_slowcream = ArtistCredit()
    artistcredit_slowcream.id = 775683
    artistcredit_slowcream.name = u'Slowcream'
    artistcredit_slowcream.artist_count = 1
    artistcredit_slowcream.ref_count = 2
    artistcredit_slowcream.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_slowcream.artists = [
        artistcreditname_slowcream,
    ]
    session.add(artistcredit_slowcream)

    recordingmeta_36 = RecordingMeta()
    session.add(recordingmeta_36)

    recording_suburb_novel = Recording()
    recording_suburb_novel.id = 11935820
    recording_suburb_novel.gid = '9a9f2f46-1cf5-4dca-a763-ed459dd03ca5'
    recording_suburb_novel.name = u'Suburb Novel'
    recording_suburb_novel.length = 301000
    recording_suburb_novel.comment = u''
    recording_suburb_novel.edits_pending = 0
    recording_suburb_novel.video = False
    recording_suburb_novel.artist_credit = artistcredit_slowcream
    recording_suburb_novel.meta = recordingmeta_36
    session.add(recording_suburb_novel)

    track_suburb_novel = Track()
    track_suburb_novel.id = 10364145
    track_suburb_novel.gid = 'f33cb8d1-1a1e-386f-a808-3a44fe068887'
    track_suburb_novel.position = 11
    track_suburb_novel.number = u'11'
    track_suburb_novel.name = u'Suburb Novel'
    track_suburb_novel.length = 301000
    track_suburb_novel.edits_pending = 0
    track_suburb_novel.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_suburb_novel.is_data_track = False
    track_suburb_novel.artist_credit = artistcredit_slowcream
    track_suburb_novel.recording = recording_suburb_novel
    session.add(track_suburb_novel)

    area_hamelin = Area()
    area_hamelin.id = 69192
    area_hamelin.gid = '163074df-66ba-4c99-8627-1a61592699a5'
    area_hamelin.name = u'Hamelin'
    area_hamelin.edits_pending = 0
    area_hamelin.last_updated = datetime.datetime(2013, 11, 26, 11, 38, 48, 627914)
    area_hamelin.ended = False
    area_hamelin.comment = u''
    area_hamelin.type = areatype_city
    session.add(area_hamelin)

    iso31662_21 = ISO31662()
    iso31662_21.code = u'DE-NI'
    session.add(iso31662_21)

    area_niedersachsen = Area()
    area_niedersachsen.id = 333
    area_niedersachsen.gid = '2978b457-3c4a-4a34-8b3c-d35e4804c42b'
    area_niedersachsen.name = u'Niedersachsen'
    area_niedersachsen.edits_pending = 0
    area_niedersachsen.last_updated = datetime.datetime(2013, 11, 26, 21, 55, 5, 360390)
    area_niedersachsen.ended = False
    area_niedersachsen.comment = u''
    area_niedersachsen.iso_3166_2_codes = [
        iso31662_21,
    ]
    area_niedersachsen.type = areatype_subdivision
    session.add(area_niedersachsen)

    linkareaarea_40 = LinkAreaArea()
    linkareaarea_40.id = 74
    linkareaarea_40.edits_pending = 0
    linkareaarea_40.last_updated = datetime.datetime(2013, 5, 17, 21, 34, 59, 74594)
    linkareaarea_40.link_order = 0
    linkareaarea_40.entity0_credit = u''
    linkareaarea_40.entity1_credit = u''
    linkareaarea_40.entity0 = area_germany
    linkareaarea_40.entity1 = area_niedersachsen
    linkareaarea_40.link = link_1
    session.add(linkareaarea_40)

    linkareaarea_39 = LinkAreaArea()
    linkareaarea_39.id = 68952
    linkareaarea_39.edits_pending = 0
    linkareaarea_39.last_updated = datetime.datetime(2013, 11, 8, 13, 35, 57, 492977)
    linkareaarea_39.link_order = 0
    linkareaarea_39.entity0_credit = u''
    linkareaarea_39.entity1_credit = u''
    linkareaarea_39.entity0 = area_niedersachsen
    linkareaarea_39.entity1 = area_hamelin
    linkareaarea_39.link = link_1
    session.add(linkareaarea_39)

    artistipi_20 = ArtistIPI()
    artistipi_20.ipi = u'00269472428'
    artistipi_20.edits_pending = 0
    artistipi_20.created = datetime.datetime(2013, 3, 14, 8, 40, 55, 93741)
    session.add(artistipi_20)

    artistisni_17 = ArtistISNI()
    artistisni_17.isni = u'0000000071408901'
    artistisni_17.edits_pending = 0
    artistisni_17.created = datetime.datetime(2014, 10, 20, 21, 23, 4, 967472)
    session.add(artistisni_17)

    artistmeta_37 = ArtistMeta()
    artistmeta_37.rating = 100
    artistmeta_37.rating_count = 3
    session.add(artistmeta_37)

    artist_max_richter = Artist()
    artist_max_richter.id = 152260
    artist_max_richter.gid = '509f20b2-5df3-4aec-9bbc-002131fb3f99'
    artist_max_richter.name = u'Max Richter'
    artist_max_richter.sort_name = u'Richter, Max'
    artist_max_richter.begin_date_year = 1966
    artist_max_richter.begin_date_month = 3
    artist_max_richter.begin_date_day = 22
    artist_max_richter.comment = u''
    artist_max_richter.edits_pending = 0
    artist_max_richter.last_updated = datetime.datetime(2016, 2, 13, 11, 0, 29, 147767)
    artist_max_richter.ended = False
    artist_max_richter.area = area_united_kingdom
    artist_max_richter.begin_area = area_hamelin
    artist_max_richter.gender = gender_male
    artist_max_richter.ipis = [
        artistipi_20,
    ]
    artist_max_richter.isnis = [
        artistisni_17,
    ]
    artist_max_richter.meta = artistmeta_37
    artist_max_richter.type = artisttype_person
    session.add(artist_max_richter)

    artistcreditname_max_richter = ArtistCreditName()
    artistcreditname_max_richter.position = 0
    artistcreditname_max_richter.name = u'Max Richter'
    artistcreditname_max_richter.join_phrase = u''
    artistcreditname_max_richter.artist = artist_max_richter
    session.add(artistcreditname_max_richter)

    artistcredit_max_richter = ArtistCredit()
    artistcredit_max_richter.id = 152260
    artistcredit_max_richter.name = u'Max Richter'
    artistcredit_max_richter.artist_count = 1
    artistcredit_max_richter.ref_count = 1491
    artistcredit_max_richter.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_max_richter.artists = [
        artistcreditname_max_richter,
    ]
    session.add(artistcredit_max_richter)

    recordingmeta_37 = RecordingMeta()
    session.add(recordingmeta_37)

    recording_arboretum = Recording()
    recording_arboretum.id = 11935821
    recording_arboretum.gid = '50c6e81f-8ef4-4b63-982a-a5122fee7dae'
    recording_arboretum.name = u'Arboretum'
    recording_arboretum.length = 174000
    recording_arboretum.comment = u''
    recording_arboretum.edits_pending = 0
    recording_arboretum.video = False
    recording_arboretum.artist_credit = artistcredit_max_richter
    recording_arboretum.meta = recordingmeta_37
    session.add(recording_arboretum)

    track_arboretum = Track()
    track_arboretum.id = 10364146
    track_arboretum.gid = 'f5f456d4-4429-3c39-871e-e69367afd2d7'
    track_arboretum.position = 12
    track_arboretum.number = u'12'
    track_arboretum.name = u'Arboretum'
    track_arboretum.length = 174000
    track_arboretum.edits_pending = 0
    track_arboretum.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_arboretum.is_data_track = False
    track_arboretum.artist_credit = artistcredit_max_richter
    track_arboretum.recording = recording_arboretum
    session.add(track_arboretum)

    artistmeta_38 = ArtistMeta()
    session.add(artistmeta_38)

    artist_akira_rabelais = Artist()
    artist_akira_rabelais.id = 127886
    artist_akira_rabelais.gid = '22af9f10-e260-43dd-80ae-24f74ac04c95'
    artist_akira_rabelais.name = u'Akira Rabelais'
    artist_akira_rabelais.sort_name = u'Rabelais, Akira'
    artist_akira_rabelais.begin_date_year = 1966
    artist_akira_rabelais.comment = u''
    artist_akira_rabelais.edits_pending = 0
    artist_akira_rabelais.last_updated = datetime.datetime(2011, 12, 12, 21, 22, 45, 74149)
    artist_akira_rabelais.ended = False
    artist_akira_rabelais.meta = artistmeta_38
    artist_akira_rabelais.type = artisttype_person
    session.add(artist_akira_rabelais)

    artistcreditname_akira_rabelais = ArtistCreditName()
    artistcreditname_akira_rabelais.position = 0
    artistcreditname_akira_rabelais.name = u'Akira Rabelais'
    artistcreditname_akira_rabelais.join_phrase = u''
    artistcreditname_akira_rabelais.artist = artist_akira_rabelais
    session.add(artistcreditname_akira_rabelais)

    artistcredit_akira_rabelais = ArtistCredit()
    artistcredit_akira_rabelais.id = 127886
    artistcredit_akira_rabelais.name = u'Akira Rabelais'
    artistcredit_akira_rabelais.artist_count = 1
    artistcredit_akira_rabelais.ref_count = 188
    artistcredit_akira_rabelais.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_akira_rabelais.artists = [
        artistcreditname_akira_rabelais,
    ]
    session.add(artistcredit_akira_rabelais)

    recordingmeta_38 = RecordingMeta()
    session.add(recordingmeta_38)

    recording_1382_wyclif_gen_ii_7 = Recording()
    recording_1382_wyclif_gen_ii_7.id = 11935822
    recording_1382_wyclif_gen_ii_7.gid = '7a8212bc-71eb-4401-b99e-54dc285ac8fe'
    recording_1382_wyclif_gen_ii_7.name = u'1382 Wyclif Gen.II.7'
    recording_1382_wyclif_gen_ii_7.length = 379000
    recording_1382_wyclif_gen_ii_7.comment = u''
    recording_1382_wyclif_gen_ii_7.edits_pending = 0
    recording_1382_wyclif_gen_ii_7.video = False
    recording_1382_wyclif_gen_ii_7.artist_credit = artistcredit_akira_rabelais
    recording_1382_wyclif_gen_ii_7.meta = recordingmeta_38
    session.add(recording_1382_wyclif_gen_ii_7)

    track_1382_wyclif_gen_ii_7 = Track()
    track_1382_wyclif_gen_ii_7.id = 10364147
    track_1382_wyclif_gen_ii_7.gid = '27961250-0ceb-3a66-9b3f-c98a8b81b089'
    track_1382_wyclif_gen_ii_7.position = 13
    track_1382_wyclif_gen_ii_7.number = u'13'
    track_1382_wyclif_gen_ii_7.name = u'1382 Wyclif Gen.II.7'
    track_1382_wyclif_gen_ii_7.length = 379000
    track_1382_wyclif_gen_ii_7.edits_pending = 0
    track_1382_wyclif_gen_ii_7.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_1382_wyclif_gen_ii_7.is_data_track = False
    track_1382_wyclif_gen_ii_7.artist_credit = artistcredit_akira_rabelais
    track_1382_wyclif_gen_ii_7.recording = recording_1382_wyclif_gen_ii_7
    session.add(track_1382_wyclif_gen_ii_7)

    artistmeta_39 = ArtistMeta()
    session.add(artistmeta_39)

    artist_ryan_teague = Artist()
    artist_ryan_teague.id = 249985
    artist_ryan_teague.gid = '5b922398-d7de-4f9c-94e4-59871430c002'
    artist_ryan_teague.name = u'Ryan Teague'
    artist_ryan_teague.sort_name = u'Teague, Ryan'
    artist_ryan_teague.comment = u''
    artist_ryan_teague.edits_pending = 0
    artist_ryan_teague.ended = False
    artist_ryan_teague.meta = artistmeta_39
    artist_ryan_teague.type = artisttype_person
    session.add(artist_ryan_teague)

    artistcreditname_ryan_teague = ArtistCreditName()
    artistcreditname_ryan_teague.position = 0
    artistcreditname_ryan_teague.name = u'Ryan Teague'
    artistcreditname_ryan_teague.join_phrase = u''
    artistcreditname_ryan_teague.artist = artist_ryan_teague
    session.add(artistcreditname_ryan_teague)

    artistcredit_ryan_teague = ArtistCredit()
    artistcredit_ryan_teague.id = 249985
    artistcredit_ryan_teague.name = u'Ryan Teague'
    artistcredit_ryan_teague.artist_count = 1
    artistcredit_ryan_teague.ref_count = 182
    artistcredit_ryan_teague.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_ryan_teague.artists = [
        artistcreditname_ryan_teague,
    ]
    session.add(artistcredit_ryan_teague)

    recordingmeta_39 = RecordingMeta()
    session.add(recordingmeta_39)

    recording_prelude_iii = Recording()
    recording_prelude_iii.id = 11935823
    recording_prelude_iii.gid = '9d16a352-d4e0-45de-ae3b-4cb263ed6ba6'
    recording_prelude_iii.name = u'Prelude III'
    recording_prelude_iii.length = 307000
    recording_prelude_iii.comment = u''
    recording_prelude_iii.edits_pending = 0
    recording_prelude_iii.video = False
    recording_prelude_iii.artist_credit = artistcredit_ryan_teague
    recording_prelude_iii.meta = recordingmeta_39
    session.add(recording_prelude_iii)

    track_prelude_iii = Track()
    track_prelude_iii.id = 10364148
    track_prelude_iii.gid = '298108d5-c41e-38f5-9fe3-adb68ffaeb3f'
    track_prelude_iii.position = 14
    track_prelude_iii.number = u'14'
    track_prelude_iii.name = u'Prelude III'
    track_prelude_iii.length = 307000
    track_prelude_iii.edits_pending = 0
    track_prelude_iii.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_prelude_iii.is_data_track = False
    track_prelude_iii.artist_credit = artistcredit_ryan_teague
    track_prelude_iii.recording = recording_prelude_iii
    session.add(track_prelude_iii)

    artistmeta_40 = ArtistMeta()
    session.add(artistmeta_40)

    artist_greg_haines = Artist()
    artist_greg_haines.id = 366648
    artist_greg_haines.gid = '062b9fb1-4bb9-40b2-80a1-9bbf2be2d2cd'
    artist_greg_haines.name = u'Greg Haines'
    artist_greg_haines.sort_name = u'Haines, Greg'
    artist_greg_haines.comment = u''
    artist_greg_haines.edits_pending = 0
    artist_greg_haines.last_updated = datetime.datetime(2015, 9, 23, 14, 53, 49, 310811)
    artist_greg_haines.ended = False
    artist_greg_haines.area = area_united_kingdom
    artist_greg_haines.gender = gender_male
    artist_greg_haines.meta = artistmeta_40
    artist_greg_haines.type = artisttype_person
    session.add(artist_greg_haines)

    artistcreditname_greg_haines = ArtistCreditName()
    artistcreditname_greg_haines.position = 0
    artistcreditname_greg_haines.name = u'Greg Haines'
    artistcreditname_greg_haines.join_phrase = u''
    artistcreditname_greg_haines.artist = artist_greg_haines
    session.add(artistcreditname_greg_haines)

    artistcredit_greg_haines = ArtistCredit()
    artistcredit_greg_haines.id = 366648
    artistcredit_greg_haines.name = u'Greg Haines'
    artistcredit_greg_haines.artist_count = 1
    artistcredit_greg_haines.ref_count = 84
    artistcredit_greg_haines.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_greg_haines.artists = [
        artistcreditname_greg_haines,
    ]
    session.add(artistcredit_greg_haines)

    recordingmeta_40 = RecordingMeta()
    session.add(recordingmeta_40)

    recording_snow_airport = Recording()
    recording_snow_airport.id = 11935824
    recording_snow_airport.gid = '595040da-54b6-4717-96bb-457d72f5339a'
    recording_snow_airport.name = u'Snow Airport'
    recording_snow_airport.length = 297000
    recording_snow_airport.comment = u''
    recording_snow_airport.edits_pending = 0
    recording_snow_airport.video = False
    recording_snow_airport.artist_credit = artistcredit_greg_haines
    recording_snow_airport.meta = recordingmeta_40
    session.add(recording_snow_airport)

    track_snow_airport = Track()
    track_snow_airport.id = 10364149
    track_snow_airport.gid = 'c6bf9291-21de-3ffa-ba9a-753065c0754f'
    track_snow_airport.position = 15
    track_snow_airport.number = u'15'
    track_snow_airport.name = u'Snow Airport'
    track_snow_airport.length = 297000
    track_snow_airport.edits_pending = 0
    track_snow_airport.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_snow_airport.is_data_track = False
    track_snow_airport.artist_credit = artistcredit_greg_haines
    track_snow_airport.recording = recording_snow_airport
    session.add(track_snow_airport)

    area_goole = Area()
    area_goole.id = 99642
    area_goole.gid = '4d8e15f9-da69-4249-b72d-64c60dcc1403'
    area_goole.name = u'Goole'
    area_goole.edits_pending = 0
    area_goole.last_updated = datetime.datetime(2014, 11, 17, 14, 58, 37, 352429)
    area_goole.ended = False
    area_goole.comment = u''
    area_goole.type = areatype_city
    session.add(area_goole)

    iso31662_22 = ISO31662()
    iso31662_22.code = u'GB-ERY'
    session.add(iso31662_22)

    area_east_riding_of_yorkshire = Area()
    area_east_riding_of_yorkshire.id = 3847
    area_east_riding_of_yorkshire.gid = 'fce537c2-afa0-4bd5-b29b-2b75929f13f6'
    area_east_riding_of_yorkshire.name = u'East Riding of Yorkshire'
    area_east_riding_of_yorkshire.edits_pending = 0
    area_east_riding_of_yorkshire.last_updated = datetime.datetime(2013, 5, 21, 14, 40, 44, 138825)
    area_east_riding_of_yorkshire.ended = False
    area_east_riding_of_yorkshire.comment = u''
    area_east_riding_of_yorkshire.iso_3166_2_codes = [
        iso31662_22,
    ]
    area_east_riding_of_yorkshire.type = areatype_subdivision
    session.add(area_east_riding_of_yorkshire)

    linkareaarea_42 = LinkAreaArea()
    linkareaarea_42.id = 3613
    linkareaarea_42.edits_pending = 0
    linkareaarea_42.last_updated = datetime.datetime(2013, 5, 21, 14, 40, 52, 602679)
    linkareaarea_42.link_order = 0
    linkareaarea_42.entity0_credit = u''
    linkareaarea_42.entity1_credit = u''
    linkareaarea_42.entity0 = area_england
    linkareaarea_42.entity1 = area_east_riding_of_yorkshire
    linkareaarea_42.link = link_1
    session.add(linkareaarea_42)

    linkareaarea_41 = LinkAreaArea()
    linkareaarea_41.id = 99398
    linkareaarea_41.edits_pending = 0
    linkareaarea_41.last_updated = datetime.datetime(2014, 11, 17, 14, 58, 37, 352429)
    linkareaarea_41.link_order = 0
    linkareaarea_41.entity0_credit = u''
    linkareaarea_41.entity1_credit = u''
    linkareaarea_41.entity0 = area_east_riding_of_yorkshire
    linkareaarea_41.entity1 = area_goole
    linkareaarea_41.link = link_1
    session.add(linkareaarea_41)

    artistipi_21 = ArtistIPI()
    artistipi_21.ipi = u'00065393756'
    artistipi_21.edits_pending = 0
    artistipi_21.created = datetime.datetime(2012, 5, 15, 19, 4, 48, 684349)
    session.add(artistipi_21)

    artistisni_18 = ArtistISNI()
    artistisni_18.isni = u'0000000114449288'
    artistisni_18.edits_pending = 0
    artistisni_18.created = datetime.datetime(2015, 6, 1, 7, 10, 28, 202841)
    session.add(artistisni_18)

    artistmeta_41 = ArtistMeta()
    session.add(artistmeta_41)

    artist_gavin_bryars = Artist()
    artist_gavin_bryars.id = 34465
    artist_gavin_bryars.gid = 'af88ef96-ba9c-441c-9291-ac4389cd1464'
    artist_gavin_bryars.name = u'Gavin Bryars'
    artist_gavin_bryars.sort_name = u'Bryars, Gavin'
    artist_gavin_bryars.begin_date_year = 1943
    artist_gavin_bryars.begin_date_month = 1
    artist_gavin_bryars.begin_date_day = 16
    artist_gavin_bryars.comment = u''
    artist_gavin_bryars.edits_pending = 0
    artist_gavin_bryars.last_updated = datetime.datetime(2015, 6, 1, 7, 10, 28, 202841)
    artist_gavin_bryars.ended = False
    artist_gavin_bryars.area = area_united_kingdom
    artist_gavin_bryars.begin_area = area_goole
    artist_gavin_bryars.gender = gender_male
    artist_gavin_bryars.ipis = [
        artistipi_21,
    ]
    artist_gavin_bryars.isnis = [
        artistisni_18,
    ]
    artist_gavin_bryars.meta = artistmeta_41
    artist_gavin_bryars.type = artisttype_person
    session.add(artist_gavin_bryars)

    artistcreditname_gavin_bryars = ArtistCreditName()
    artistcreditname_gavin_bryars.position = 0
    artistcreditname_gavin_bryars.name = u'Gavin Bryars'
    artistcreditname_gavin_bryars.join_phrase = u''
    artistcreditname_gavin_bryars.artist = artist_gavin_bryars
    session.add(artistcreditname_gavin_bryars)

    artistcredit_gavin_bryars = ArtistCredit()
    artistcredit_gavin_bryars.id = 34465
    artistcredit_gavin_bryars.name = u'Gavin Bryars'
    artistcredit_gavin_bryars.artist_count = 1
    artistcredit_gavin_bryars.ref_count = 452
    artistcredit_gavin_bryars.created = datetime.datetime(2011, 5, 16, 16, 32, 11, 963929)
    artistcredit_gavin_bryars.artists = [
        artistcreditname_gavin_bryars,
    ]
    session.add(artistcredit_gavin_bryars)

    recordingmeta_41 = RecordingMeta()
    session.add(recordingmeta_41)

    recording_tramp_with_orchestra_iii = Recording()
    recording_tramp_with_orchestra_iii.id = 11935825
    recording_tramp_with_orchestra_iii.gid = '336bed41-b3b0-4886-80ec-7b9bada0ecf8'
    recording_tramp_with_orchestra_iii.name = u'Tramp With Orchestra III'
    recording_tramp_with_orchestra_iii.length = 288000
    recording_tramp_with_orchestra_iii.comment = u''
    recording_tramp_with_orchestra_iii.edits_pending = 0
    recording_tramp_with_orchestra_iii.video = False
    recording_tramp_with_orchestra_iii.artist_credit = artistcredit_gavin_bryars
    recording_tramp_with_orchestra_iii.meta = recordingmeta_41
    session.add(recording_tramp_with_orchestra_iii)

    track_tramp_with_orchestra_iii = Track()
    track_tramp_with_orchestra_iii.id = 10364150
    track_tramp_with_orchestra_iii.gid = '2abc397a-108a-3bab-a15f-3bae9a8b05c7'
    track_tramp_with_orchestra_iii.position = 16
    track_tramp_with_orchestra_iii.number = u'16'
    track_tramp_with_orchestra_iii.name = u'Tramp With Orchestra III'
    track_tramp_with_orchestra_iii.length = 288000
    track_tramp_with_orchestra_iii.edits_pending = 0
    track_tramp_with_orchestra_iii.last_updated = datetime.datetime(2011, 5, 16, 16, 8, 20, 288158)
    track_tramp_with_orchestra_iii.is_data_track = False
    track_tramp_with_orchestra_iii.artist_credit = artistcredit_gavin_bryars
    track_tramp_with_orchestra_iii.recording = recording_tramp_with_orchestra_iii
    session.add(track_tramp_with_orchestra_iii)

    medium_3 = Medium()
    medium_3.id = 785487
    medium_3.position = 1
    medium_3.name = u''
    medium_3.edits_pending = 0
    medium_3.last_updated = datetime.datetime(2011, 5, 16, 14, 57, 6, 530063)
    medium_3.track_count = 16
    medium_3.format = mediumformat_cd
    medium_3.tracks = [
        track_daydream,
        track_lithium,
        track_zuhause,
        track_il_fait_nuit_noire_a_berlin,
        track_moon,
        track_zauberberg_iv,
        track_he_poos_clouds,
        track_andover,
        track_abdulmajid,
        track_maiz,
        track_suburb_novel,
        track_arboretum,
        track_1382_wyclif_gen_ii_7,
        track_prelude_iii,
        track_snow_airport,
        track_tramp_with_orchestra_iii,
    ]
    session.add(medium_3)

    releasemeta_2 = ReleaseMeta()
    releasemeta_2.date_added = datetime.datetime(2011, 1, 1, 21, 34, 7, 280802)
    releasemeta_2.info_url = u'http://www.amazon.de/gp/product/B002JP1LCK'
    releasemeta_2.amazon_asin = u'B002JP1LCK'
    releasemeta_2.cover_art_presence = 'present'
    session.add(releasemeta_2)

    releasepackaging_digipak = ReleasePackaging()
    releasepackaging_digipak.id = 3
    releasepackaging_digipak.name = u'Digipak'
    releasepackaging_digipak.child_order = 0
    releasepackaging_digipak.gid = '8f931351-d2e2-310f-afc6-37b89ddba246'
    session.add(releasepackaging_digipak)

    releasegroupmeta_2 = ReleaseGroupMeta()
    releasegroupmeta_2.release_count = 1
    releasegroupmeta_2.first_release_date_year = 2009
    releasegroupmeta_2.rating = 100
    releasegroupmeta_2.rating_count = 1
    session.add(releasegroupmeta_2)

    releasegroupsecondarytypejoin_2 = ReleaseGroupSecondaryTypeJoin()
    releasegroupsecondarytypejoin_2.created = datetime.datetime(2012, 5, 15, 0, 0)
    releasegroupsecondarytypejoin_2.secondary_type = releasegroupsecondarytype_compilation
    session.add(releasegroupsecondarytypejoin_2)

    releasegroup_xvi_reflections_on_classical_music = ReleaseGroup()
    releasegroup_xvi_reflections_on_classical_music.id = 1029754
    releasegroup_xvi_reflections_on_classical_music.gid = '8650e20f-39cc-45e2-b4fa-a5bb6de349ad'
    releasegroup_xvi_reflections_on_classical_music.name = u'XVI Reflections on Classical Music'
    releasegroup_xvi_reflections_on_classical_music.comment = u''
    releasegroup_xvi_reflections_on_classical_music.edits_pending = 0
    releasegroup_xvi_reflections_on_classical_music.last_updated = datetime.datetime(2012, 5, 15, 19, 1, 58, 718541)
    releasegroup_xvi_reflections_on_classical_music.artist_credit = artistcredit_various_artists
    releasegroup_xvi_reflections_on_classical_music.meta = releasegroupmeta_2
    releasegroup_xvi_reflections_on_classical_music.secondary_types = [
        releasegroupsecondarytypejoin_2,
    ]
    releasegroup_xvi_reflections_on_classical_music.type = releasegroupprimarytype_album
    session.add(releasegroup_xvi_reflections_on_classical_music)

    releasestatus_official = ReleaseStatus()
    releasestatus_official.id = 1
    releasestatus_official.name = u'Official'
    releasestatus_official.child_order = 1
    releasestatus_official.description = u'Any release officially sanctioned by the artist and/or their record company. Most releases will fit into this category.'
    releasestatus_official.gid = '4e304316-386d-3409-af2e-78857eec5cfe'
    session.add(releasestatus_official)

    release_xvi_reflections_on_classical_music = Release()
    release_xvi_reflections_on_classical_music.id = 785487
    release_xvi_reflections_on_classical_music.gid = '7643ee96-fe19-4b76-aa9a-e8af7d0e9d73'
    release_xvi_reflections_on_classical_music.name = u'XVI Reflections on Classical Music'
    release_xvi_reflections_on_classical_music.barcode = u'0028948022205'
    release_xvi_reflections_on_classical_music.comment = u''
    release_xvi_reflections_on_classical_music.edits_pending = 0
    release_xvi_reflections_on_classical_music.quality = -1
    release_xvi_reflections_on_classical_music.last_updated = datetime.datetime(2016, 4, 14, 18, 0, 35, 937361)
    release_xvi_reflections_on_classical_music.artist_credit = artistcredit_various_artists
    release_xvi_reflections_on_classical_music.country_dates = [
        releasecountry_2,
    ]
    release_xvi_reflections_on_classical_music.labels = [
        releaselabel_2,
    ]
    release_xvi_reflections_on_classical_music.language = language_english
    release_xvi_reflections_on_classical_music.mediums = [
        medium_3,
    ]
    release_xvi_reflections_on_classical_music.meta = releasemeta_2
    release_xvi_reflections_on_classical_music.packaging = releasepackaging_digipak
    release_xvi_reflections_on_classical_music.release_group = releasegroup_xvi_reflections_on_classical_music
    release_xvi_reflections_on_classical_music.script = script_latin
    release_xvi_reflections_on_classical_music.status = releasestatus_official
    session.add(release_xvi_reflections_on_classical_music)

    url_5 = URL()
    url_5.id = 848180
    url_5.gid = '59db77f3-c903-405a-8d62-40b14496c2e7'
    url_5.url = u'http://www.amazon.de/gp/product/B002JP1LCK'
    url_5.edits_pending = 0
    url_5.last_updated = datetime.datetime(2011, 5, 16, 16, 31, 52)
    session.add(url_5)

    linktype_amazon_asin = LinkType()
    linktype_amazon_asin.id = 77
    linktype_amazon_asin.child_order = 0
    linktype_amazon_asin.gid = '4f2e710d-166c-480c-a293-2e2c8d658d87'
    linktype_amazon_asin.entity_type0 = u'release'
    linktype_amazon_asin.entity_type1 = u'url'
    linktype_amazon_asin.name = u'amazon asin'
    linktype_amazon_asin.description = u'This links a MusicBrainz release to the equivalent entry at Amazon and will often provide cover art if there is no cover art in the <a href="/doc/Cover_Art_Archive">Cover Art Archive</a>.'
    linktype_amazon_asin.link_phrase = u'ASIN'
    linktype_amazon_asin.reverse_link_phrase = u'ASIN'
    linktype_amazon_asin.long_link_phrase = u'has Amazon ASIN'
    linktype_amazon_asin.priority = 0
    linktype_amazon_asin.last_updated = datetime.datetime(2014, 4, 27, 12, 51, 28, 60431)
    linktype_amazon_asin.is_deprecated = False
    linktype_amazon_asin.has_dates = True
    linktype_amazon_asin.entity0_cardinality = 0
    linktype_amazon_asin.entity1_cardinality = 0
    session.add(linktype_amazon_asin)

    link_10 = Link()
    link_10.id = 6300
    link_10.attribute_count = 0
    link_10.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_10.ended = False
    link_10.link_type = linktype_amazon_asin
    session.add(link_10)

    linkreleaseurl_2 = LinkReleaseURL()
    linkreleaseurl_2.id = 573288
    linkreleaseurl_2.edits_pending = 0
    linkreleaseurl_2.last_updated = datetime.datetime(2011, 5, 16, 16, 31, 52, 155025)
    linkreleaseurl_2.link_order = 0
    linkreleaseurl_2.entity0_credit = u''
    linkreleaseurl_2.entity1_credit = u''
    linkreleaseurl_2.entity0 = release_xvi_reflections_on_classical_music
    linkreleaseurl_2.entity1 = url_5
    linkreleaseurl_2.link = link_10
    session.add(linkreleaseurl_2)

    area_st_john_s_wood = Area()
    area_st_john_s_wood.id = 66431
    area_st_john_s_wood.gid = '57296e85-ed07-4d79-88ef-7b70d23acf8d'
    area_st_john_s_wood.name = u"St John's Wood"
    area_st_john_s_wood.edits_pending = 0
    area_st_john_s_wood.last_updated = datetime.datetime(2013, 11, 6, 22, 54, 51, 28274)
    area_st_john_s_wood.ended = False
    area_st_john_s_wood.comment = u''
    area_st_john_s_wood.type = areatype_district
    session.add(area_st_john_s_wood)

    iso31662_23 = ISO31662()
    iso31662_23.code = u'GB-WSM'
    session.add(iso31662_23)

    area_westminster = Area()
    area_westminster.id = 3906
    area_westminster.gid = '48d08ee1-db45-4566-bb1d-c47ab6dbaf98'
    area_westminster.name = u'Westminster'
    area_westminster.edits_pending = 0
    area_westminster.last_updated = datetime.datetime(2013, 5, 21, 14, 51, 57, 923559)
    area_westminster.ended = False
    area_westminster.comment = u''
    area_westminster.iso_3166_2_codes = [
        iso31662_23,
    ]
    area_westminster.type = areatype_subdivision
    session.add(area_westminster)

    area_london = Area()
    area_london.id = 1178
    area_london.gid = 'f03d09b3-39dc-4083-afd6-159e3f0d462f'
    area_london.name = u'London'
    area_london.edits_pending = 0
    area_london.last_updated = datetime.datetime(2013, 5, 24, 0, 4, 48, 706550)
    area_london.ended = False
    area_london.comment = u''
    area_london.type = areatype_city
    session.add(area_london)

    linkareaarea_45 = LinkAreaArea()
    linkareaarea_45.id = 964
    linkareaarea_45.edits_pending = 0
    linkareaarea_45.last_updated = datetime.datetime(2013, 5, 19, 20, 29, 59, 930277)
    linkareaarea_45.link_order = 0
    linkareaarea_45.entity0_credit = u''
    linkareaarea_45.entity1_credit = u''
    linkareaarea_45.entity0 = area_england
    linkareaarea_45.entity1 = area_london
    linkareaarea_45.link = link_1
    session.add(linkareaarea_45)

    linkareaarea_44 = LinkAreaArea()
    linkareaarea_44.id = 3672
    linkareaarea_44.edits_pending = 0
    linkareaarea_44.last_updated = datetime.datetime(2013, 5, 21, 15, 55, 43, 356589)
    linkareaarea_44.link_order = 0
    linkareaarea_44.entity0_credit = u''
    linkareaarea_44.entity1_credit = u''
    linkareaarea_44.entity0 = area_london
    linkareaarea_44.entity1 = area_westminster
    linkareaarea_44.link = link_1
    session.add(linkareaarea_44)

    linkareaarea_43 = LinkAreaArea()
    linkareaarea_43.id = 66189
    linkareaarea_43.edits_pending = 0
    linkareaarea_43.last_updated = datetime.datetime(2013, 11, 4, 9, 43, 43, 118925)
    linkareaarea_43.link_order = 0
    linkareaarea_43.entity0_credit = u''
    linkareaarea_43.entity1_credit = u''
    linkareaarea_43.entity0 = area_westminster
    linkareaarea_43.entity1 = area_st_john_s_wood
    linkareaarea_43.link = link_1
    session.add(linkareaarea_43)

    placetype_studio = PlaceType()
    placetype_studio.id = 1
    placetype_studio.name = u'Studio'
    placetype_studio.child_order = 1
    placetype_studio.description = u'A place designed for non-live production of music, typically a recording studio.'
    placetype_studio.gid = '05fa6a09-ff92-3d34-bdbb-5141d3c24f38'
    session.add(placetype_studio)

    place_abbey_road_studios = Place()
    place_abbey_road_studios.id = 775
    place_abbey_road_studios.gid = 'bd55aeb7-19d1-4607-a500-14b8479d3fed'
    place_abbey_road_studios.name = u'Abbey Road Studios'
    place_abbey_road_studios.address = u"3 Abbey Road, St John's Wood, London"
    place_abbey_road_studios.coordinates = (51.53192, -0.17835)
    place_abbey_road_studios.comment = u''
    place_abbey_road_studios.edits_pending = 0
    place_abbey_road_studios.last_updated = datetime.datetime(2013, 12, 9, 22, 4, 9, 988010)
    place_abbey_road_studios.begin_date_year = 1931
    place_abbey_road_studios.ended = False
    place_abbey_road_studios.area = area_st_john_s_wood
    place_abbey_road_studios.type = placetype_studio
    session.add(place_abbey_road_studios)

    iso31661_11 = ISO31661()
    iso31661_11.code = u'JP'
    session.add(iso31661_11)

    area_japan = Area()
    area_japan.id = 107
    area_japan.gid = '2db42837-c832-3c27-b4a3-08198f75693c'
    area_japan.name = u'Japan'
    area_japan.edits_pending = 0
    area_japan.last_updated = datetime.datetime(2013, 5, 27, 12, 29, 56, 162248)
    area_japan.ended = False
    area_japan.comment = u''
    area_japan.iso_3166_1_codes = [
        iso31661_11,
    ]
    area_japan.type = areatype_country
    session.add(area_japan)

    labelipi_1 = LabelIPI()
    labelipi_1.ipi = u'00173517959'
    labelipi_1.edits_pending = 0
    labelipi_1.created = datetime.datetime(2013, 9, 20, 9, 17, 40, 201068)
    session.add(labelipi_1)

    labelipi_2 = LabelIPI()
    labelipi_2.ipi = u'00473554732'
    labelipi_2.edits_pending = 0
    labelipi_2.created = datetime.datetime(2013, 9, 20, 9, 17, 40, 201068)
    session.add(labelipi_2)

    labelisni_1 = LabelISNI()
    labelisni_1.isni = u'000000011781560X'
    labelisni_1.edits_pending = 0
    labelisni_1.created = datetime.datetime(2013, 9, 20, 9, 17, 40, 201068)
    session.add(labelisni_1)

    labelmeta_3 = LabelMeta()
    session.add(labelmeta_3)

    label = Label()
    label.id = 83683
    label.gid = 'ecc049d0-88a6-4806-a5b7-0f1367a7d6e1'
    label.name = u'\u30b9\u30bf\u30b8\u30aa\u30b8\u30d6\u30ea'
    label.begin_date_year = 1985
    label.begin_date_month = 6
    label.comment = u''
    label.edits_pending = 0
    label.last_updated = datetime.datetime(2013, 9, 20, 9, 17, 40, 201068)
    label.ended = False
    label.area = area_japan
    label.ipis = [
        labelipi_1,
        labelipi_2,
    ]
    label.isnis = [
        labelisni_1,
    ]
    label.meta = labelmeta_3
    label.type = labeltype_production
    session.add(label)

    session.commit()
