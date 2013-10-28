import datetime
from mbdata.models import Area, AreaType, Artist, ArtistCredit, ArtistCreditName
from mbdata.models import ArtistIPI, ArtistISNI, ArtistMeta, ArtistType, CountryArea
from mbdata.models import Gender, Label, LabelIPI, LabelISNI, LabelMeta
from mbdata.models import LabelType, Language, Medium, MediumFormat, Place
from mbdata.models import PlaceType, Recording, RecordingMeta, Release, ReleaseCountry
from mbdata.models import ReleaseGroup, ReleaseGroupMeta, ReleaseGroupPrimaryType, ReleaseGroupSecondaryType, ReleaseGroupSecondaryTypeJoin
from mbdata.models import ReleaseLabel, ReleaseMeta, ReleasePackaging, ReleaseStatus, Script
from mbdata.models import Track


def create_sample_data(session):
    areatype_country = AreaType()
    areatype_country.id = 1
    areatype_country.name = u'Country'
    session.add(areatype_country)

    area_denmark = Area()
    area_denmark.id = 57
    area_denmark.gid = '4757b525-2a60-324a-b060-578765d2c993'
    area_denmark.name = u'Denmark'
    area_denmark.sort_name = u'Denmark'
    area_denmark.edits_pending = 0
    area_denmark.last_updated = datetime.datetime(2013, 5, 27, 15, 28, 43, 191347)
    area_denmark.ended = False
    area_denmark.comment = u''
    area_denmark.type = areatype_country
    session.add(area_denmark)

    areatype_municipality = AreaType()
    areatype_municipality.id = 4
    areatype_municipality.name = u'Municipality'
    session.add(areatype_municipality)

    area_vordingborg_municipality = Area()
    area_vordingborg_municipality.id = 12847
    area_vordingborg_municipality.gid = 'ca8458e6-a8a2-4e46-a6a0-9aa6509499b1'
    area_vordingborg_municipality.name = u'Vordingborg Municipality'
    area_vordingborg_municipality.sort_name = u'Vordingborg Municipality'
    area_vordingborg_municipality.edits_pending = 0
    area_vordingborg_municipality.last_updated = datetime.datetime(2013, 7, 16, 11, 24, 32, 591103)
    area_vordingborg_municipality.ended = False
    area_vordingborg_municipality.comment = u''
    area_vordingborg_municipality.type = areatype_municipality
    session.add(area_vordingborg_municipality)

    gender_male = Gender()
    gender_male.id = 1
    gender_male.name = u'Male'
    session.add(gender_male)

    artistipi_1 = ArtistIPI()
    artistipi_1.ipi = u'00054968649'
    artistipi_1.edits_pending = 0
    artistipi_1.created = datetime.datetime(2013, 10, 2, 18, 0, 12, 326623)
    session.add(artistipi_1)

    artistisni_1 = ArtistISNI()
    artistisni_1.isni = u'0000000117742762'
    artistisni_1.edits_pending = 0
    artistisni_1.created = datetime.datetime(2013, 8, 4, 3, 48, 1, 946612)
    session.add(artistisni_1)

    artistmeta_1 = ArtistMeta()
    artistmeta_1.rating = 100
    artistmeta_1.rating_count = 2
    session.add(artistmeta_1)

    artisttype_person = ArtistType()
    artisttype_person.id = 1
    artisttype_person.name = u'Person'
    session.add(artisttype_person)

    artist_trentemoller = Artist()
    artist_trentemoller.id = 108703
    artist_trentemoller.gid = '95e9aba6-f85c-48a0-9ec9-395d4f0e3875'
    artist_trentemoller.name = u'Trentem\xf8ller'
    artist_trentemoller.sort_name = u'Trentem\xf8ller'
    artist_trentemoller.begin_date_year = 1974
    artist_trentemoller.begin_date_month = 10
    artist_trentemoller.begin_date_day = 16
    artist_trentemoller.comment = u''
    artist_trentemoller.edits_pending = 0
    artist_trentemoller.last_updated = datetime.datetime(2013, 10, 2, 18, 0, 12, 326623)
    artist_trentemoller.ended = False
    artist_trentemoller.area = area_denmark
    artist_trentemoller.begin_area = area_vordingborg_municipality
    artist_trentemoller.gender = gender_male
    artist_trentemoller.ipis = [
        artistipi_1,
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
    artistcredit_trentemoller.ref_count = 875
    artistcredit_trentemoller.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
    artistcredit_trentemoller.artists = [
        artistcreditname_trentemoller,
    ]
    session.add(artistcredit_trentemoller)

    area_united_kingdom = Area()
    area_united_kingdom.id = 221
    area_united_kingdom.gid = '8a754a16-0027-3a29-b6d7-2b40ea0481ed'
    area_united_kingdom.name = u'United Kingdom'
    area_united_kingdom.sort_name = u'United Kingdom'
    area_united_kingdom.edits_pending = 0
    area_united_kingdom.last_updated = datetime.datetime(2013, 5, 16, 13, 6, 19, 672350)
    area_united_kingdom.ended = False
    area_united_kingdom.comment = u''
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

    labeltype_production = LabelType()
    labeltype_production.id = 3
    labeltype_production.name = u'Production'
    session.add(labeltype_production)

    label_king_biscuit_recordings = Label()
    label_king_biscuit_recordings.id = 9000
    label_king_biscuit_recordings.gid = 'aefbe2a5-76d6-4c99-a51d-f9214fe1018b'
    label_king_biscuit_recordings.name = u'King Biscuit Recordings'
    label_king_biscuit_recordings.sort_name = u'King Biscuit Recordings'
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
    releaselabel_1.last_updated = datetime.datetime(2011, 5, 16, 17, 59, 0, 785958)
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
    session.add(mediumformat_hdcd)

    mediumformat_cd_r = MediumFormat()
    mediumformat_cd_r.id = 33
    mediumformat_cd_r.name = u'CD-R'
    mediumformat_cd_r.child_order = 1
    mediumformat_cd_r.has_discids = True
    session.add(mediumformat_cd_r)

    mediumformat_8cm_cd = MediumFormat()
    mediumformat_8cm_cd.id = 34
    mediumformat_8cm_cd.name = u'8cm CD'
    mediumformat_8cm_cd.child_order = 2
    mediumformat_8cm_cd.year = 1982
    mediumformat_8cm_cd.has_discids = True
    session.add(mediumformat_8cm_cd)

    mediumformat_cd = MediumFormat()
    mediumformat_cd.id = 1
    mediumformat_cd.name = u'CD'
    mediumformat_cd.child_order = 0
    mediumformat_cd.year = 1982
    mediumformat_cd.has_discids = True
    mediumformat_cd.parent = [
        mediumformat_hdcd,
        mediumformat_cd_r,
        mediumformat_8cm_cd,
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
    track_small_piano_piece.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    artistcredit_khan.ref_count = 321
    artistcredit_khan.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_fantomes.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    track_the_very_last_resort.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    track_miss_you.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_miss_you.artist_credit = artistcredit_trentemoller
    track_miss_you.recording = recording_miss_you
    session.add(track_miss_you)

    area_united_states = Area()
    area_united_states.id = 222
    area_united_states.gid = '489ce91b-6658-3307-9877-795b68554c98'
    area_united_states.name = u'United States'
    area_united_states.sort_name = u'United States'
    area_united_states.edits_pending = 0
    area_united_states.last_updated = datetime.datetime(2013, 6, 15, 20, 6, 39, 593230)
    area_united_states.ended = False
    area_united_states.comment = u''
    area_united_states.type = areatype_country
    session.add(area_united_states)

    areatype_subdivision = AreaType()
    areatype_subdivision.id = 2
    areatype_subdivision.name = u'Subdivision'
    session.add(areatype_subdivision)

    area_new_york = Area()
    area_new_york.id = 295
    area_new_york.gid = '75e398a3-5f3f-4224-9cd8-0fe44715bc95'
    area_new_york.name = u'New York'
    area_new_york.sort_name = u'New York'
    area_new_york.edits_pending = 0
    area_new_york.last_updated = datetime.datetime(2013, 5, 17, 22, 23, 26, 631791)
    area_new_york.ended = False
    area_new_york.comment = u''
    area_new_york.type = areatype_subdivision
    session.add(area_new_york)

    areatype_city = AreaType()
    areatype_city.id = 3
    areatype_city.name = u'City'
    session.add(areatype_city)

    area_montreal = Area()
    area_montreal.id = 7279
    area_montreal.gid = 'c3cc624e-b963-49cf-ad0b-e318cb341963'
    area_montreal.name = u'Montreal'
    area_montreal.sort_name = u'Montreal'
    area_montreal.edits_pending = 0
    area_montreal.last_updated = datetime.datetime(2013, 5, 26, 19, 19, 17, 882833)
    area_montreal.ended = False
    area_montreal.comment = u''
    area_montreal.type = areatype_city
    session.add(area_montreal)

    gender_female = Gender()
    gender_female.id = 2
    gender_female.name = u'Female'
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
    artist_lhasa.last_updated = datetime.datetime(2013, 6, 7, 6, 6, 30, 835699)
    artist_lhasa.ended = True
    artist_lhasa.area = area_united_states
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
    artistcredit_lhasa.ref_count = 234
    artistcredit_lhasa.created = datetime.datetime(2012, 2, 17, 11, 38, 33, 908280)
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
    recording_de_carla_a_pered.last_updated = datetime.datetime(2012, 4, 11, 2, 0, 11, 85366)
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
    track_de_carla_a_pered.last_updated = datetime.datetime(2012, 4, 11, 2, 0, 11, 85366)
    track_de_carla_a_pered.artist_credit = artistcredit_lhasa
    track_de_carla_a_pered.recording = recording_de_carla_a_pered
    session.add(track_de_carla_a_pered)

    area_mexico = Area()
    area_mexico.id = 138
    area_mexico.gid = '3e08b2cd-69f3-317c-b1e4-e71be581839e'
    area_mexico.name = u'Mexico'
    area_mexico.sort_name = u'Mexico'
    area_mexico.edits_pending = 0
    area_mexico.last_updated = datetime.datetime(2013, 5, 27, 15, 41, 13, 615269)
    area_mexico.ended = False
    area_mexico.comment = u''
    area_mexico.type = areatype_country
    session.add(area_mexico)

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
    artist_murcof.last_updated = datetime.datetime(2011, 5, 23, 0, 58, 8, 421516)
    artist_murcof.ended = False
    artist_murcof.area = area_mexico
    artist_murcof.gender = gender_male
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
    artistcredit_murcof.ref_count = 332
    artistcredit_murcof.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_una.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    track_snowflake.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_snowflake.artist_credit = artistcredit_trentemoller
    track_snowflake.recording = recording_snowflake
    session.add(track_snowflake)

    area_jamaica = Area()
    area_jamaica.id = 106
    area_jamaica.gid = '2dd47a64-91d5-3b13-bc94-80043ed063d7'
    area_jamaica.name = u'Jamaica'
    area_jamaica.sort_name = u'Jamaica'
    area_jamaica.edits_pending = 0
    area_jamaica.last_updated = datetime.datetime(2013, 5, 27, 14, 32, 31, 72979)
    area_jamaica.ended = False
    area_jamaica.comment = u''
    area_jamaica.type = areatype_country
    session.add(area_jamaica)

    artistmeta_5 = ArtistMeta()
    session.add(artistmeta_5)

    artisttype_group = ArtistType()
    artisttype_group.id = 2
    artisttype_group.name = u'Group'
    session.add(artisttype_group)

    artist_the_crystalites = Artist()
    artist_the_crystalites.id = 134514
    artist_the_crystalites.gid = '41ee41ff-cec6-46a6-8e67-5991a8ebc2ed'
    artist_the_crystalites.name = u'The Crystalites'
    artist_the_crystalites.sort_name = u'Crystalites, The'
    artist_the_crystalites.comment = u'JM reggae group, studio group with prod. Derrick Harriott'
    artist_the_crystalites.edits_pending = 0
    artist_the_crystalites.last_updated = datetime.datetime(2011, 8, 10, 9, 0, 11, 778408)
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
    artistcredit_the_crystalites.ref_count = 84
    artistcredit_the_crystalites.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_concentration_version_3.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    track_evil_dub.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_evil_dub.artist_credit = artistcredit_trentemoller
    track_evil_dub.recording = recording_evil_dub
    session.add(track_evil_dub)

    area_coventry = Area()
    area_coventry.id = 3917
    area_coventry.gid = 'aab979a4-b106-4baa-a4a3-fc45f775cff9'
    area_coventry.name = u'Coventry'
    area_coventry.sort_name = u'Coventry'
    area_coventry.edits_pending = 0
    area_coventry.last_updated = datetime.datetime(2013, 6, 5, 12, 26, 16, 645060)
    area_coventry.ended = False
    area_coventry.comment = u''
    area_coventry.type = areatype_subdivision
    session.add(area_coventry)

    artistisni_2 = ArtistISNI()
    artistisni_2.isni = u'0000000122859471'
    artistisni_2.edits_pending = 0
    artistisni_2.created = datetime.datetime(2013, 5, 26, 12, 0, 11, 791620)
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
    artist_the_specials.last_updated = datetime.datetime(2013, 10, 11, 18, 0, 23, 807561)
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
    artistcredit_the_specials.ref_count = 1886
    artistcredit_the_specials.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    track_ghost_town = Track()
    track_ghost_town.id = 5918620
    track_ghost_town.gid = 'ea027835-8081-36fc-a8d7-1f9fc9406f65'
    track_ghost_town.position = 10
    track_ghost_town.number = u'10'
    track_ghost_town.name = u'Ghost Town'
    track_ghost_town.length = 311986
    track_ghost_town.edits_pending = 0
    track_ghost_town.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_ghost_town.artist_credit = artistcredit_the_specials
    track_ghost_town.recording = recording_ghost_town
    session.add(track_ghost_town)

    artistmeta_7 = ArtistMeta()
    session.add(artistmeta_7)

    artist_businessman = Artist()
    artist_businessman.id = 455235
    artist_businessman.gid = 'ac6eaeb6-a855-41a1-a461-f23dd292513c'
    artist_businessman.name = u'Businessman'
    artist_businessman.sort_name = u'Businessman'
    artist_businessman.comment = u''
    artist_businessman.edits_pending = 0
    artist_businessman.ended = False
    artist_businessman.meta = artistmeta_7
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
    artistcredit_businessman.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_dubby_games.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    track_nightwalker.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_nightwalker.artist_credit = artistcredit_trentemoller
    track_nightwalker.recording = recording_nightwalker
    session.add(track_nightwalker)

    medium_1 = Medium()
    medium_1.id = 291054
    medium_1.position = 1
    medium_1.edits_pending = 0
    medium_1.last_updated = datetime.datetime(2012, 5, 27, 13, 5, 54, 679406)
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
    track_moan_feat_ane_trolle.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_moan_feat_ane_trolle.artist_credit = artistcredit_trentemoller
    track_moan_feat_ane_trolle.recording = recording_moan_feat_ane_trolle
    session.add(track_moan_feat_ane_trolle)

    area_los_angeles = Area()
    area_los_angeles.id = 7703
    area_los_angeles.gid = '1f40c6e1-47ba-4e35-996f-fe6ee5840e62'
    area_los_angeles.name = u'Los Angeles'
    area_los_angeles.sort_name = u'Los Angeles'
    area_los_angeles.edits_pending = 0
    area_los_angeles.last_updated = datetime.datetime(2013, 5, 29, 2, 9, 20, 794559)
    area_los_angeles.ended = False
    area_los_angeles.comment = u''
    area_los_angeles.type = areatype_city
    session.add(area_los_angeles)

    artistisni_3 = ArtistISNI()
    artistisni_3.isni = u'0000000115160232'
    artistisni_3.edits_pending = 0
    artistisni_3.created = datetime.datetime(2013, 7, 24, 5, 45, 1, 534835)
    session.add(artistisni_3)

    artistmeta_8 = ArtistMeta()
    artistmeta_8.rating = 85
    artistmeta_8.rating_count = 16
    session.add(artistmeta_8)

    artist_the_doors = Artist()
    artist_the_doors.id = 1757
    artist_the_doors.gid = '9efff43b-3b29-4082-824e-bc82f646f93d'
    artist_the_doors.name = u'The Doors'
    artist_the_doors.sort_name = u'Doors, The'
    artist_the_doors.begin_date_year = 1965
    artist_the_doors.end_date_year = 1972
    artist_the_doors.comment = u''
    artist_the_doors.edits_pending = 0
    artist_the_doors.last_updated = datetime.datetime(2013, 7, 24, 5, 45, 1, 534835)
    artist_the_doors.ended = True
    artist_the_doors.area = area_united_states
    artist_the_doors.begin_area = area_los_angeles
    artist_the_doors.isnis = [
        artistisni_3,
    ]
    artist_the_doors.meta = artistmeta_8
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
    artistcredit_the_doors.ref_count = 7893
    artistcredit_the_doors.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_break_on_through_dark_ride_dub_mix.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_break_on_through_dark_ride_dub_mix.artist_credit = artistcredit_the_doors
    track_break_on_through_dark_ride_dub_mix.recording = recording_break_on_through_dark_ride_dub_mix
    session.add(track_break_on_through_dark_ride_dub_mix)

    area_glasgow = Area()
    area_glasgow.id = 3855
    area_glasgow.gid = 'c279f805-01f8-46f5-99cf-51f165a1adad'
    area_glasgow.name = u'Glasgow'
    area_glasgow.sort_name = u'Glasgow'
    area_glasgow.edits_pending = 0
    area_glasgow.last_updated = datetime.datetime(2013, 5, 24, 2, 2, 38, 336242)
    area_glasgow.ended = False
    area_glasgow.comment = u''
    area_glasgow.type = areatype_city
    session.add(area_glasgow)

    artistmeta_9 = ArtistMeta()
    artistmeta_9.rating = 88
    artistmeta_9.rating_count = 12
    session.add(artistmeta_9)

    artist_franz_ferdinand = Artist()
    artist_franz_ferdinand.id = 117968
    artist_franz_ferdinand.gid = 'aa7a2827-f74b-473c-bd79-03d065835cf7'
    artist_franz_ferdinand.name = u'Franz Ferdinand'
    artist_franz_ferdinand.sort_name = u'Franz Ferdinand'
    artist_franz_ferdinand.begin_date_year = 2001
    artist_franz_ferdinand.comment = u''
    artist_franz_ferdinand.edits_pending = 0
    artist_franz_ferdinand.last_updated = datetime.datetime(2013, 6, 16, 0, 24, 22, 502874)
    artist_franz_ferdinand.ended = False
    artist_franz_ferdinand.area = area_united_kingdom
    artist_franz_ferdinand.begin_area = area_glasgow
    artist_franz_ferdinand.meta = artistmeta_9
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
    artistcredit_franz_ferdinand.ref_count = 1947
    artistcredit_franz_ferdinand.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    track_the_fallen_justice_remix = Track()
    track_the_fallen_justice_remix.id = 5918645
    track_the_fallen_justice_remix.gid = '0291a4dd-f5c0-3fce-aea0-516755e75a1f'
    track_the_fallen_justice_remix.position = 3
    track_the_fallen_justice_remix.number = u'3'
    track_the_fallen_justice_remix.name = u'The Fallen (Justice remix)'
    track_the_fallen_justice_remix.length = 97973
    track_the_fallen_justice_remix.edits_pending = 0
    track_the_fallen_justice_remix.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_the_fallen_justice_remix.artist_credit = artistcredit_franz_ferdinand
    track_the_fallen_justice_remix.recording = recording_the_fallen_justice_remix
    session.add(track_the_fallen_justice_remix)

    area_new_york_1 = Area()
    area_new_york_1.id = 7020
    area_new_york_1.gid = '74e50e58-5deb-4b99-93a2-decbb365c07f'
    area_new_york_1.name = u'New York'
    area_new_york_1.sort_name = u'New York'
    area_new_york_1.edits_pending = 0
    area_new_york_1.last_updated = datetime.datetime(2013, 5, 28, 11, 35, 43, 54898)
    area_new_york_1.ended = False
    area_new_york_1.comment = u''
    area_new_york_1.type = areatype_city
    session.add(area_new_york_1)

    artistmeta_10 = ArtistMeta()
    session.add(artistmeta_10)

    artist_le_tigre = Artist()
    artist_le_tigre.id = 51
    artist_le_tigre.gid = '2d67239c-aa40-4ad5-a807-9052b66857a6'
    artist_le_tigre.name = u'Le Tigre'
    artist_le_tigre.sort_name = u'Tigre, Le'
    artist_le_tigre.begin_date_year = 1998
    artist_le_tigre.comment = u''
    artist_le_tigre.edits_pending = 0
    artist_le_tigre.last_updated = datetime.datetime(2013, 7, 26, 11, 14, 16, 631116)
    artist_le_tigre.ended = False
    artist_le_tigre.area = area_united_states
    artist_le_tigre.begin_area = area_new_york_1
    artist_le_tigre.meta = artistmeta_10
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
    artistcredit_le_tigre.ref_count = 365
    artistcredit_le_tigre.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_nanny_nanny_boo_boo_junior_senior_remix.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_nanny_nanny_boo_boo_junior_senior_remix.artist_credit = artistcredit_le_tigre
    track_nanny_nanny_boo_boo_junior_senior_remix.recording = recording_nanny_nanny_boo_boo_junior_senior_remix
    session.add(track_nanny_nanny_boo_boo_junior_senior_remix)

    artistmeta_11 = ArtistMeta()
    session.add(artistmeta_11)

    artist_james_white_and_the_blacks = Artist()
    artist_james_white_and_the_blacks.id = 107002
    artist_james_white_and_the_blacks.gid = '4e303fcf-0f7e-42f4-b84e-454a7922e725'
    artist_james_white_and_the_blacks.name = u'James White and The Blacks'
    artist_james_white_and_the_blacks.sort_name = u'White, James and The Blacks'
    artist_james_white_and_the_blacks.comment = u''
    artist_james_white_and_the_blacks.edits_pending = 0
    artist_james_white_and_the_blacks.last_updated = datetime.datetime(2010, 7, 25, 6, 44, 13, 723447)
    artist_james_white_and_the_blacks.ended = False
    artist_james_white_and_the_blacks.meta = artistmeta_11
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
    artistcredit_james_white_and_the_blacks.ref_count = 125
    artistcredit_james_white_and_the_blacks.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_contort_yourself.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_contort_yourself.artist_credit = artistcredit_james_white_and_the_blacks
    track_contort_yourself.recording = recording_contort_yourself
    session.add(track_contort_yourself)

    area_sweden = Area()
    area_sweden.id = 202
    area_sweden.gid = '23d10872-f5ae-3f0c-bf55-332788a16ecb'
    area_sweden.name = u'Sweden'
    area_sweden.sort_name = u'Sweden'
    area_sweden.edits_pending = 0
    area_sweden.last_updated = datetime.datetime(2013, 5, 27, 15, 49, 3, 298388)
    area_sweden.ended = False
    area_sweden.comment = u''
    area_sweden.type = areatype_country
    session.add(area_sweden)

    artistmeta_12 = ArtistMeta()
    session.add(artistmeta_12)

    artist_revl9n = Artist()
    artist_revl9n.id = 226950
    artist_revl9n.gid = 'f07c698b-f559-4dd0-a65b-b7fddd30355b'
    artist_revl9n.name = u'Revl9n'
    artist_revl9n.sort_name = u'Revl9n'
    artist_revl9n.comment = u''
    artist_revl9n.edits_pending = 0
    artist_revl9n.last_updated = datetime.datetime(2011, 12, 6, 21, 27, 11, 764329)
    artist_revl9n.ended = False
    artist_revl9n.area = area_sweden
    artist_revl9n.meta = artistmeta_12
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
    artistcredit_revl9n.ref_count = 73
    artistcredit_revl9n.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_someone_like_you.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_someone_like_you.artist_credit = artistcredit_revl9n
    track_someone_like_you.recording = recording_someone_like_you
    session.add(track_someone_like_you)

    area_germany = Area()
    area_germany.id = 81
    area_germany.gid = '85752fda-13c4-31a3-bee5-0e5cb1f51dad'
    area_germany.name = u'Germany'
    area_germany.sort_name = u'Germany'
    area_germany.edits_pending = 0
    area_germany.last_updated = datetime.datetime(2013, 5, 27, 14, 44, 37, 529747)
    area_germany.ended = False
    area_germany.comment = u''
    area_germany.type = areatype_country
    session.add(area_germany)

    artistmeta_13 = ArtistMeta()
    artistmeta_13.rating = 100
    artistmeta_13.rating_count = 1
    session.add(artistmeta_13)

    artist_thomas_schumacher = Artist()
    artist_thomas_schumacher.id = 43060
    artist_thomas_schumacher.gid = '25fdd039-edad-466e-b150-d7405c4da995'
    artist_thomas_schumacher.name = u'Thomas Schumacher'
    artist_thomas_schumacher.sort_name = u'Schumacher, Thomas'
    artist_thomas_schumacher.comment = u''
    artist_thomas_schumacher.edits_pending = 0
    artist_thomas_schumacher.last_updated = datetime.datetime(2011, 6, 17, 16, 28, 33, 602591)
    artist_thomas_schumacher.ended = False
    artist_thomas_schumacher.area = area_germany
    artist_thomas_schumacher.gender = gender_male
    artist_thomas_schumacher.meta = artistmeta_13
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
    artistcredit_thomas_schumacher.ref_count = 643
    artistcredit_thomas_schumacher.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_high_on_you.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_high_on_you.artist_credit = artistcredit_thomas_schumacher
    track_high_on_you.recording = recording_high_on_you
    session.add(track_high_on_you)

    areatype_district = AreaType()
    areatype_district.id = 5
    areatype_district.name = u'District'
    session.add(areatype_district)

    area_manhattan = Area()
    area_manhattan.id = 10862
    area_manhattan.gid = '261962ea-d8c2-4eaf-a80c-f14376ffadb0'
    area_manhattan.name = u'Manhattan'
    area_manhattan.sort_name = u'Manhattan'
    area_manhattan.edits_pending = 0
    area_manhattan.last_updated = datetime.datetime(2013, 8, 28, 15, 49, 3, 230143)
    area_manhattan.ended = False
    area_manhattan.comment = u''
    area_manhattan.type = areatype_district
    session.add(area_manhattan)

    artistipi_2 = ArtistIPI()
    artistipi_2.ipi = u'00232910003'
    artistipi_2.edits_pending = 0
    artistipi_2.created = datetime.datetime(2013, 1, 23, 18, 0, 16, 122251)
    session.add(artistipi_2)

    artistipi_3 = ArtistIPI()
    artistipi_3.ipi = u'00232910101'
    artistipi_3.edits_pending = 0
    artistipi_3.created = datetime.datetime(2013, 1, 23, 18, 0, 16, 122251)
    session.add(artistipi_3)

    artistisni_4 = ArtistISNI()
    artistisni_4.isni = u'0000000078243206'
    artistisni_4.edits_pending = 0
    artistisni_4.created = datetime.datetime(2013, 8, 30, 7, 1, 40, 485286)
    session.add(artistisni_4)

    artistmeta_14 = ArtistMeta()
    artistmeta_14.rating = 78
    artistmeta_14.rating_count = 12
    session.add(artistmeta_14)

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
    artist_moby.last_updated = datetime.datetime(2013, 8, 30, 7, 1, 40, 485286)
    artist_moby.ended = False
    artist_moby.area = area_united_states
    artist_moby.begin_area = area_manhattan
    artist_moby.gender = gender_male
    artist_moby.ipis = [
        artistipi_2,
        artistipi_3,
    ]
    artist_moby.isnis = [
        artistisni_4,
    ]
    artist_moby.meta = artistmeta_14
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
    artistcredit_moby.ref_count = 8108
    artistcredit_moby.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    track_go_trentemoller_remix = Track()
    track_go_trentemoller_remix.id = 5918650
    track_go_trentemoller_remix.gid = '9aa04088-f04b-3b98-8aa6-0d579de621fd'
    track_go_trentemoller_remix.position = 8
    track_go_trentemoller_remix.number = u'8'
    track_go_trentemoller_remix.name = u'Go! (Trentem\xf8ller remix)'
    track_go_trentemoller_remix.length = 392373
    track_go_trentemoller_remix.edits_pending = 0
    track_go_trentemoller_remix.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_go_trentemoller_remix.artist_credit = artistcredit_moby
    track_go_trentemoller_remix.recording = recording_go_trentemoller_remix
    session.add(track_go_trentemoller_remix)

    area_stockholm = Area()
    area_stockholm.id = 5114
    area_stockholm.gid = '1127ddc2-eab3-4662-8718-6adbdeea3b10'
    area_stockholm.name = u'Stockholm'
    area_stockholm.sort_name = u'Stockholm'
    area_stockholm.edits_pending = 0
    area_stockholm.last_updated = datetime.datetime(2013, 5, 24, 22, 30, 8, 523187)
    area_stockholm.ended = False
    area_stockholm.comment = u''
    area_stockholm.type = areatype_city
    session.add(area_stockholm)

    artistmeta_15 = ArtistMeta()
    artistmeta_15.rating = 100
    artistmeta_15.rating_count = 2
    session.add(artistmeta_15)

    artist_the_knife = Artist()
    artist_the_knife.id = 61967
    artist_the_knife.gid = 'bf710b71-48e5-4e15-9bd6-96debb2e4e98'
    artist_the_knife.name = u'The Knife'
    artist_the_knife.sort_name = u'Knife, The'
    artist_the_knife.begin_date_year = 1999
    artist_the_knife.comment = u'Swedish indie electronic duo'
    artist_the_knife.edits_pending = 0
    artist_the_knife.last_updated = datetime.datetime(2013, 8, 10, 2, 29, 13, 786964)
    artist_the_knife.ended = False
    artist_the_knife.area = area_sweden
    artist_the_knife.begin_area = area_stockholm
    artist_the_knife.meta = artistmeta_15
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
    artistcredit_the_knife.ref_count = 1074
    artistcredit_the_knife.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    track_silent_shout_trente_short_edit = Track()
    track_silent_shout_trente_short_edit.id = 5918651
    track_silent_shout_trente_short_edit.gid = '88d0b720-1aca-3513-8ab3-50d2a1293743'
    track_silent_shout_trente_short_edit.position = 9
    track_silent_shout_trente_short_edit.number = u'9'
    track_silent_shout_trente_short_edit.name = u'Silent Shout (Trente short edit)'
    track_silent_shout_trente_short_edit.length = 14986
    track_silent_shout_trente_short_edit.edits_pending = 0
    track_silent_shout_trente_short_edit.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_silent_shout_trente_short_edit.artist_credit = artistcredit_the_knife
    track_silent_shout_trente_short_edit.recording = recording_silent_shout_trente_short_edit
    session.add(track_silent_shout_trente_short_edit)

    artistmeta_16 = ArtistMeta()
    session.add(artistmeta_16)

    artist_jokke_ilsoe = Artist()
    artist_jokke_ilsoe.id = 362912
    artist_jokke_ilsoe.gid = 'e1c79c85-44ed-4483-8ec6-28cfe6440345'
    artist_jokke_ilsoe.name = u'Jokke Ils\xf8e'
    artist_jokke_ilsoe.sort_name = u'Ils\xf8e, Jokke'
    artist_jokke_ilsoe.comment = u''
    artist_jokke_ilsoe.edits_pending = 0
    artist_jokke_ilsoe.ended = False
    artist_jokke_ilsoe.meta = artistmeta_16
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
    artistcredit_jokke_ilsoe.ref_count = 40
    artistcredit_jokke_ilsoe.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    track_feelin_good_trentemoller_remix = Track()
    track_feelin_good_trentemoller_remix.id = 5918652
    track_feelin_good_trentemoller_remix.gid = '8a14c288-f753-3c2b-9cb0-306b3eca70dc'
    track_feelin_good_trentemoller_remix.position = 10
    track_feelin_good_trentemoller_remix.number = u'10'
    track_feelin_good_trentemoller_remix.name = u"Feelin' Good (Trentem\xf8ller remix)"
    track_feelin_good_trentemoller_remix.length = 383320
    track_feelin_good_trentemoller_remix.edits_pending = 0
    track_feelin_good_trentemoller_remix.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_feelin_good_trentemoller_remix.artist_credit = artistcredit_jokke_ilsoe
    track_feelin_good_trentemoller_remix.recording = recording_feelin_good_trentemoller_remix
    session.add(track_feelin_good_trentemoller_remix)

    artistmeta_17 = ArtistMeta()
    session.add(artistmeta_17)

    artist_isolee = Artist()
    artist_isolee.id = 57862
    artist_isolee.gid = '4c99c0b4-5d46-44d2-8c49-ba47a522b016'
    artist_isolee.name = u'Isol\xe9e'
    artist_isolee.sort_name = u'Isol\xe9e'
    artist_isolee.comment = u''
    artist_isolee.edits_pending = 0
    artist_isolee.last_updated = datetime.datetime(2012, 8, 18, 11, 0, 20, 310734)
    artist_isolee.ended = False
    artist_isolee.area = area_germany
    artist_isolee.gender = gender_male
    artist_isolee.meta = artistmeta_17
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
    artistcredit_isolee.ref_count = 513
    artistcredit_isolee.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    track_beau_mot_plage_freeform_five_remix_re_edit = Track()
    track_beau_mot_plage_freeform_five_remix_re_edit.id = 5918653
    track_beau_mot_plage_freeform_five_remix_re_edit.gid = 'e23716f6-6900-356a-bb73-b1b0e5e26b4d'
    track_beau_mot_plage_freeform_five_remix_re_edit.position = 11
    track_beau_mot_plage_freeform_five_remix_re_edit.number = u'11'
    track_beau_mot_plage_freeform_five_remix_re_edit.name = u'Beau Mot Plage (Freeform Five remix re-edit)'
    track_beau_mot_plage_freeform_five_remix_re_edit.length = 144373
    track_beau_mot_plage_freeform_five_remix_re_edit.edits_pending = 0
    track_beau_mot_plage_freeform_five_remix_re_edit.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    track_always_something_better_feat_richard_davis.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    recording_we_share_our_mothers_health_trentemoller_remix.last_updated = datetime.datetime(2012, 5, 28, 22, 0, 13, 371964)
    recording_we_share_our_mothers_health_trentemoller_remix.video = False
    recording_we_share_our_mothers_health_trentemoller_remix.artist_credit = artistcredit_the_knife
    recording_we_share_our_mothers_health_trentemoller_remix.meta = recordingmeta_25
    session.add(recording_we_share_our_mothers_health_trentemoller_remix)

    track_we_share_our_mother_s_health_trentemoller_remix = Track()
    track_we_share_our_mother_s_health_trentemoller_remix.id = 5918655
    track_we_share_our_mother_s_health_trentemoller_remix.gid = '7d3c3101-db47-34dd-807f-a125afba6631'
    track_we_share_our_mother_s_health_trentemoller_remix.position = 13
    track_we_share_our_mother_s_health_trentemoller_remix.number = u'13'
    track_we_share_our_mother_s_health_trentemoller_remix.name = u"We Share Our Mother's Health (Trentem\xf8ller remix)"
    track_we_share_our_mother_s_health_trentemoller_remix.length = 356160
    track_we_share_our_mother_s_health_trentemoller_remix.edits_pending = 0
    track_we_share_our_mother_s_health_trentemoller_remix.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_we_share_our_mother_s_health_trentemoller_remix.artist_credit = artistcredit_the_knife
    track_we_share_our_mother_s_health_trentemoller_remix.recording = recording_we_share_our_mothers_health_trentemoller_remix
    session.add(track_we_share_our_mother_s_health_trentemoller_remix)

    medium_2 = Medium()
    medium_2.id = 291059
    medium_2.position = 2
    medium_2.edits_pending = 0
    medium_2.last_updated = datetime.datetime(2012, 5, 27, 13, 5, 54, 679406)
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
    releasemeta_1.date_added = datetime.datetime(2007, 7, 24, 6, 30, 26, 1888)
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
    session.add(releasegroupsecondarytype_compilation)

    releasegroupsecondarytypejoin_1 = ReleaseGroupSecondaryTypeJoin()
    releasegroupsecondarytypejoin_1.created = datetime.datetime(2012, 5, 15, 2, 0)
    releasegroupsecondarytypejoin_1.secondary_type = releasegroupsecondarytype_compilation
    session.add(releasegroupsecondarytypejoin_1)

    releasegroupprimarytype_album = ReleaseGroupPrimaryType()
    releasegroupprimarytype_album.id = 1
    releasegroupprimarytype_album.name = u'Album'
    session.add(releasegroupprimarytype_album)

    releasegroup_trentemoller_the_polar_mix = ReleaseGroup()
    releasegroup_trentemoller_the_polar_mix.id = 633232
    releasegroup_trentemoller_the_polar_mix.gid = 'baca4e84-aa67-3ef9-adbe-0dfebe7b6a82'
    releasegroup_trentemoller_the_polar_mix.name = u'Trentem\xf8ller: The P\xf8lar Mix'
    releasegroup_trentemoller_the_polar_mix.comment = u''
    releasegroup_trentemoller_the_polar_mix.edits_pending = 0
    releasegroup_trentemoller_the_polar_mix.last_updated = datetime.datetime(2012, 5, 15, 21, 1, 58, 718541)
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
    session.add(releasestatus_promotion)

    release_trentemoller_the_polar_mix = Release()
    release_trentemoller_the_polar_mix.id = 291054
    release_trentemoller_the_polar_mix.gid = '89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149'
    release_trentemoller_the_polar_mix.name = u'Trentem\xf8ller: The P\xf8lar Mix'
    release_trentemoller_the_polar_mix.comment = u''
    release_trentemoller_the_polar_mix.edits_pending = 0
    release_trentemoller_the_polar_mix.quality = -1
    release_trentemoller_the_polar_mix.last_updated = datetime.datetime(2012, 10, 11, 8, 53, 15, 922324)
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

    artistmeta_18 = ArtistMeta()
    artistmeta_18.rating = 78
    artistmeta_18.rating_count = 18
    session.add(artistmeta_18)

    artisttype_other = ArtistType()
    artisttype_other.id = 3
    artisttype_other.name = u'Other'
    session.add(artisttype_other)

    artist_various_artists = Artist()
    artist_various_artists.id = 1
    artist_various_artists.gid = '89ad4ac3-39f7-470e-963a-56509c546377'
    artist_various_artists.name = u'Various Artists'
    artist_various_artists.sort_name = u'Various Artists'
    artist_various_artists.comment = u'add compilations to this artist'
    artist_various_artists.edits_pending = 9
    artist_various_artists.last_updated = datetime.datetime(2013, 10, 18, 18, 0, 20, 936389)
    artist_various_artists.ended = False
    artist_various_artists.meta = artistmeta_18
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
    artistcredit_various_artists.ref_count = 239850
    artistcredit_various_artists.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    labeltype_publisher = LabelType()
    labeltype_publisher.id = 7
    labeltype_publisher.name = u'Publisher'
    session.add(labeltype_publisher)

    label_universal_music = Label()
    label_universal_music.id = 36455
    label_universal_music.gid = '13a464dc-b9fd-4d16-a4f4-d4316f6a46c7'
    label_universal_music.name = u'Universal Music'
    label_universal_music.sort_name = u'Universal Music'
    label_universal_music.label_code = 7340
    label_universal_music.comment = u''
    label_universal_music.edits_pending = 0
    label_universal_music.last_updated = datetime.datetime(2012, 9, 28, 13, 4, 21, 712883)
    label_universal_music.ended = False
    label_universal_music.area = area_united_states
    label_universal_music.meta = labelmeta_2
    label_universal_music.type = labeltype_publisher
    session.add(label_universal_music)

    releaselabel_2 = ReleaseLabel()
    releaselabel_2.id = 533902
    releaselabel_2.last_updated = datetime.datetime(2011, 5, 16, 17, 59, 0, 785958)
    releaselabel_2.label = label_universal_music
    session.add(releaselabel_2)

    artistmeta_19 = ArtistMeta()
    session.add(artistmeta_19)

    artist_lawrence = Artist()
    artist_lawrence.id = 168462
    artist_lawrence.gid = '819a9744-627b-4bf5-92e9-f894b0f252e6'
    artist_lawrence.name = u'Lawrence'
    artist_lawrence.sort_name = u'Lawrence'
    artist_lawrence.comment = u'Electronic artist Peter M. Kersten'
    artist_lawrence.edits_pending = 0
    artist_lawrence.ended = False
    artist_lawrence.meta = artistmeta_19
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
    artistcredit_lawrence.ref_count = 354
    artistcredit_lawrence.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_daydream.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_daydream.artist_credit = artistcredit_lawrence
    track_daydream.recording = recording_daydream
    session.add(track_daydream)

    artistmeta_20 = ArtistMeta()
    session.add(artistmeta_20)

    artist_takeo_toyama = Artist()
    artist_takeo_toyama.id = 299529
    artist_takeo_toyama.gid = 'b2d731d0-252d-4842-9707-4f5c5247ee34'
    artist_takeo_toyama.name = u'Takeo Toyama'
    artist_takeo_toyama.sort_name = u'Toyama, Takeo'
    artist_takeo_toyama.comment = u''
    artist_takeo_toyama.edits_pending = 0
    artist_takeo_toyama.ended = False
    artist_takeo_toyama.meta = artistmeta_20
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
    artistcredit_takeo_toyama.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_lithium.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_lithium.artist_credit = artistcredit_takeo_toyama
    track_lithium.recording = recording_lithium
    session.add(track_lithium)

    artistmeta_21 = ArtistMeta()
    session.add(artistmeta_21)

    artist_hauschka = Artist()
    artist_hauschka.id = 299525
    artist_hauschka.gid = '767026a6-9e39-463b-9d04-ed0f86ac5ee7'
    artist_hauschka.name = u'Hauschka'
    artist_hauschka.sort_name = u'Hauschka'
    artist_hauschka.begin_date_year = 1966
    artist_hauschka.comment = u''
    artist_hauschka.edits_pending = 0
    artist_hauschka.last_updated = datetime.datetime(2012, 6, 1, 10, 2, 3, 517903)
    artist_hauschka.ended = False
    artist_hauschka.area = area_germany
    artist_hauschka.gender = gender_male
    artist_hauschka.meta = artistmeta_21
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
    artistcredit_hauschka.ref_count = 281
    artistcredit_hauschka.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_zuhause.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_zuhause.artist_credit = artistcredit_hauschka
    track_zuhause.recording = recording_zuhause
    session.add(track_zuhause)

    area_france = Area()
    area_france.id = 73
    area_france.gid = '08310658-51eb-3801-80de-5a0739207115'
    area_france.name = u'France'
    area_france.sort_name = u'France'
    area_france.edits_pending = 0
    area_france.last_updated = datetime.datetime(2013, 5, 27, 14, 50, 32, 702645)
    area_france.ended = False
    area_france.comment = u''
    area_france.type = areatype_country
    session.add(area_france)

    artistmeta_22 = ArtistMeta()
    session.add(artistmeta_22)

    artist_sylvain_chauveau = Artist()
    artist_sylvain_chauveau.id = 139706
    artist_sylvain_chauveau.gid = 'e0443586-8830-4b7a-91c1-d6876c16d669'
    artist_sylvain_chauveau.name = u'Sylvain Chauveau'
    artist_sylvain_chauveau.sort_name = u'Chauveau, Sylvain'
    artist_sylvain_chauveau.begin_date_year = 1971
    artist_sylvain_chauveau.comment = u''
    artist_sylvain_chauveau.edits_pending = 0
    artist_sylvain_chauveau.last_updated = datetime.datetime(2012, 1, 25, 18, 2, 35, 401552)
    artist_sylvain_chauveau.ended = False
    artist_sylvain_chauveau.area = area_france
    artist_sylvain_chauveau.gender = gender_male
    artist_sylvain_chauveau.meta = artistmeta_22
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
    artistcredit_sylvain_chauveau.ref_count = 355
    artistcredit_sylvain_chauveau.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_il_fait_nuit_noire_a_berlin.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_il_fait_nuit_noire_a_berlin.artist_credit = artistcredit_sylvain_chauveau
    track_il_fait_nuit_noire_a_berlin.recording = recording_il_fait_nuit_noire_a_berlin
    session.add(track_il_fait_nuit_noire_a_berlin)

    artistmeta_23 = ArtistMeta()
    session.add(artistmeta_23)

    artist_alva_noto_ryuichi_sakamoto = Artist()
    artist_alva_noto_ryuichi_sakamoto.id = 127630
    artist_alva_noto_ryuichi_sakamoto.gid = '6edc70bb-c340-4ae6-bdd4-d5fb0c7411de'
    artist_alva_noto_ryuichi_sakamoto.name = u'Alva Noto + Ryuichi Sakamoto'
    artist_alva_noto_ryuichi_sakamoto.sort_name = u'Noto, Alva + Sakamoto, Ryuichi'
    artist_alva_noto_ryuichi_sakamoto.comment = u''
    artist_alva_noto_ryuichi_sakamoto.edits_pending = 0
    artist_alva_noto_ryuichi_sakamoto.last_updated = datetime.datetime(2013, 1, 23, 20, 0, 17, 638468)
    artist_alva_noto_ryuichi_sakamoto.ended = False
    artist_alva_noto_ryuichi_sakamoto.meta = artistmeta_23
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
    artistcredit_alva_noto_ryuichi_sakamoto.ref_count = 94
    artistcredit_alva_noto_ryuichi_sakamoto.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_moon.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_moon.artist_credit = artistcredit_alva_noto_ryuichi_sakamoto
    track_moon.recording = recording_moon
    session.add(track_moon)

    artistmeta_24 = ArtistMeta()
    artistmeta_24.rating = 100
    artistmeta_24.rating_count = 1
    session.add(artistmeta_24)

    artist_gas = Artist()
    artist_gas.id = 51632
    artist_gas.gid = '054b0483-eeb8-48ce-bb72-f1cb57ff44f9'
    artist_gas.name = u'Gas'
    artist_gas.sort_name = u'Gas'
    artist_gas.comment = u'German electronic producer Wolfgang Voigt'
    artist_gas.edits_pending = 0
    artist_gas.last_updated = datetime.datetime(2012, 3, 11, 20, 9, 29, 240384)
    artist_gas.ended = False
    artist_gas.area = area_germany
    artist_gas.meta = artistmeta_24
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
    artistcredit_gas.ref_count = 236
    artistcredit_gas.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_zauberberg_iv.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_zauberberg_iv.artist_credit = artistcredit_gas
    track_zauberberg_iv.recording = recording_zauberberg_iv
    session.add(track_zauberberg_iv)

    area_canada = Area()
    area_canada.id = 38
    area_canada.gid = '71bbafaa-e825-3e15-8ca9-017dcad1748b'
    area_canada.name = u'Canada'
    area_canada.sort_name = u'Canada'
    area_canada.edits_pending = 0
    area_canada.last_updated = datetime.datetime(2013, 5, 27, 15, 15, 52, 179105)
    area_canada.ended = False
    area_canada.comment = u''
    area_canada.type = areatype_country
    session.add(area_canada)

    artistmeta_25 = ArtistMeta()
    session.add(artistmeta_25)

    artist_final_fantasy = Artist()
    artist_final_fantasy.id = 238993
    artist_final_fantasy.gid = 'dcbd7e51-de76-47d6-aadc-7e38b779f82d'
    artist_final_fantasy.name = u'Final Fantasy'
    artist_final_fantasy.sort_name = u'Final Fantasy'
    artist_final_fantasy.begin_date_year = 2004
    artist_final_fantasy.end_date_year = 2009
    artist_final_fantasy.comment = u'Canadian indie pop, Owen Pallett'
    artist_final_fantasy.edits_pending = 0
    artist_final_fantasy.last_updated = datetime.datetime(2012, 9, 25, 23, 0, 14, 891477)
    artist_final_fantasy.ended = True
    artist_final_fantasy.area = area_canada
    artist_final_fantasy.meta = artistmeta_25
    artist_final_fantasy.type = artisttype_group
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
    artistcredit_final_fantasy.ref_count = 293
    artistcredit_final_fantasy.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    recording_he_poos_clouds.length = 211000
    recording_he_poos_clouds.comment = u''
    recording_he_poos_clouds.edits_pending = 0
    recording_he_poos_clouds.last_updated = datetime.datetime(2013, 8, 8, 15, 0, 42, 88409)
    recording_he_poos_clouds.video = False
    recording_he_poos_clouds.artist_credit = artistcredit_final_fantasy
    recording_he_poos_clouds.meta = recordingmeta_32
    session.add(recording_he_poos_clouds)

    track_he_poos_clouds = Track()
    track_he_poos_clouds.id = 10364141
    track_he_poos_clouds.gid = '59b034d9-1bcb-32be-8890-f1f555a279aa'
    track_he_poos_clouds.position = 7
    track_he_poos_clouds.number = u'7'
    track_he_poos_clouds.name = u'He Poos Clouds'
    track_he_poos_clouds.length = 211000
    track_he_poos_clouds.edits_pending = 0
    track_he_poos_clouds.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_he_poos_clouds.artist_credit = artistcredit_final_fantasy
    track_he_poos_clouds.recording = recording_he_poos_clouds
    session.add(track_he_poos_clouds)

    area_luxembourg = Area()
    area_luxembourg.id = 124
    area_luxembourg.gid = '563d21b7-4a8e-35e2-83a7-7804baefbfa7'
    area_luxembourg.name = u'Luxembourg'
    area_luxembourg.sort_name = u'Luxembourg'
    area_luxembourg.edits_pending = 0
    area_luxembourg.last_updated = datetime.datetime(2013, 5, 27, 15, 51, 12, 674706)
    area_luxembourg.ended = False
    area_luxembourg.comment = u''
    area_luxembourg.type = areatype_country
    session.add(area_luxembourg)

    artistmeta_26 = ArtistMeta()
    session.add(artistmeta_26)

    artist_francesco_tristano = Artist()
    artist_francesco_tristano.id = 314969
    artist_francesco_tristano.gid = 'c2de59ca-07b1-431f-b946-e3e5421ede63'
    artist_francesco_tristano.name = u'Francesco Tristano'
    artist_francesco_tristano.sort_name = u'Tristano, Francesco'
    artist_francesco_tristano.comment = u''
    artist_francesco_tristano.edits_pending = 0
    artist_francesco_tristano.last_updated = datetime.datetime(2012, 9, 16, 20, 36, 44, 436508)
    artist_francesco_tristano.ended = False
    artist_francesco_tristano.area = area_luxembourg
    artist_francesco_tristano.gender = gender_male
    artist_francesco_tristano.meta = artistmeta_26
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
    artistcredit_francesco_tristano.ref_count = 78
    artistcredit_francesco_tristano.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_andover.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_andover.artist_credit = artistcredit_francesco_tristano
    track_andover.recording = recording_andover
    session.add(track_andover)

    area_baltimore = Area()
    area_baltimore.id = 5148
    area_baltimore.gid = '2fb5445d-3987-49fe-957a-f730a7acc4a2'
    area_baltimore.name = u'Baltimore'
    area_baltimore.sort_name = u'Baltimore'
    area_baltimore.edits_pending = 0
    area_baltimore.last_updated = datetime.datetime(2013, 5, 24, 22, 36, 45, 29411)
    area_baltimore.ended = False
    area_baltimore.comment = u''
    area_baltimore.type = areatype_city
    session.add(area_baltimore)

    artistipi_4 = ArtistIPI()
    artistipi_4.ipi = u'00012034058'
    artistipi_4.edits_pending = 0
    artistipi_4.created = datetime.datetime(2013, 3, 26, 18, 40, 13, 338175)
    session.add(artistipi_4)

    artistipi_5 = ArtistIPI()
    artistipi_5.ipi = u'00125609583'
    artistipi_5.edits_pending = 0
    artistipi_5.created = datetime.datetime(2013, 3, 26, 18, 40, 13, 338175)
    session.add(artistipi_5)

    artistisni_5 = ArtistISNI()
    artistisni_5.isni = u'0000000121367029'
    artistisni_5.edits_pending = 0
    artistisni_5.created = datetime.datetime(2013, 10, 12, 18, 52, 44, 358667)
    session.add(artistisni_5)

    artistmeta_27 = ArtistMeta()
    artistmeta_27.rating = 95
    artistmeta_27.rating_count = 8
    session.add(artistmeta_27)

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
    artist_philip_glass.last_updated = datetime.datetime(2013, 10, 12, 18, 52, 44, 358667)
    artist_philip_glass.ended = False
    artist_philip_glass.area = area_united_states
    artist_philip_glass.begin_area = area_baltimore
    artist_philip_glass.gender = gender_male
    artist_philip_glass.ipis = [
        artistipi_4,
        artistipi_5,
    ]
    artist_philip_glass.isnis = [
        artistisni_5,
    ]
    artist_philip_glass.meta = artistmeta_27
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
    artistcredit_philip_glass.ref_count = 5106
    artistcredit_philip_glass.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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

    track_abdulmajid = Track()
    track_abdulmajid.id = 10364143
    track_abdulmajid.gid = 'ae3a985f-835a-3c42-9b25-c1d7a56082e2'
    track_abdulmajid.position = 9
    track_abdulmajid.number = u'9'
    track_abdulmajid.name = u'Abdulmajid'
    track_abdulmajid.length = 531000
    track_abdulmajid.edits_pending = 0
    track_abdulmajid.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
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
    track_maiz.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_maiz.artist_credit = artistcredit_murcof
    track_maiz.recording = recording_maiz
    session.add(track_maiz)

    artistmeta_28 = ArtistMeta()
    session.add(artistmeta_28)

    artist_slowcream = Artist()
    artist_slowcream.id = 775683
    artist_slowcream.gid = '27bc6454-5046-4066-8fe6-977190211880'
    artist_slowcream.name = u'Slowcream'
    artist_slowcream.sort_name = u'Slowcream'
    artist_slowcream.comment = u''
    artist_slowcream.edits_pending = 0
    artist_slowcream.last_updated = datetime.datetime(2011, 1, 1, 22, 3, 35, 272282)
    artist_slowcream.ended = False
    artist_slowcream.meta = artistmeta_28
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
    artistcredit_slowcream.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_suburb_novel.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_suburb_novel.artist_credit = artistcredit_slowcream
    track_suburb_novel.recording = recording_suburb_novel
    session.add(track_suburb_novel)

    artistipi_6 = ArtistIPI()
    artistipi_6.ipi = u'00269472428'
    artistipi_6.edits_pending = 0
    artistipi_6.created = datetime.datetime(2013, 3, 14, 9, 40, 55, 93741)
    session.add(artistipi_6)

    artistmeta_29 = ArtistMeta()
    artistmeta_29.rating = 100
    artistmeta_29.rating_count = 3
    session.add(artistmeta_29)

    artist_max_richter = Artist()
    artist_max_richter.id = 152260
    artist_max_richter.gid = '509f20b2-5df3-4aec-9bbc-002131fb3f99'
    artist_max_richter.name = u'Max Richter'
    artist_max_richter.sort_name = u'Richter, Max'
    artist_max_richter.begin_date_year = 1966
    artist_max_richter.comment = u''
    artist_max_richter.edits_pending = 0
    artist_max_richter.last_updated = datetime.datetime(2013, 3, 14, 9, 40, 55, 93741)
    artist_max_richter.ended = False
    artist_max_richter.area = area_united_kingdom
    artist_max_richter.gender = gender_male
    artist_max_richter.ipis = [
        artistipi_6,
    ]
    artist_max_richter.meta = artistmeta_29
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
    artistcredit_max_richter.ref_count = 782
    artistcredit_max_richter.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_arboretum.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_arboretum.artist_credit = artistcredit_max_richter
    track_arboretum.recording = recording_arboretum
    session.add(track_arboretum)

    artistmeta_30 = ArtistMeta()
    session.add(artistmeta_30)

    artist_akira_rabelais = Artist()
    artist_akira_rabelais.id = 127886
    artist_akira_rabelais.gid = '22af9f10-e260-43dd-80ae-24f74ac04c95'
    artist_akira_rabelais.name = u'Akira Rabelais'
    artist_akira_rabelais.sort_name = u'Rabelais, Akira'
    artist_akira_rabelais.begin_date_year = 1966
    artist_akira_rabelais.comment = u''
    artist_akira_rabelais.edits_pending = 0
    artist_akira_rabelais.last_updated = datetime.datetime(2011, 12, 12, 22, 22, 45, 74149)
    artist_akira_rabelais.ended = False
    artist_akira_rabelais.meta = artistmeta_30
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
    artistcredit_akira_rabelais.ref_count = 184
    artistcredit_akira_rabelais.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_1382_wyclif_gen_ii_7.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_1382_wyclif_gen_ii_7.artist_credit = artistcredit_akira_rabelais
    track_1382_wyclif_gen_ii_7.recording = recording_1382_wyclif_gen_ii_7
    session.add(track_1382_wyclif_gen_ii_7)

    artistmeta_31 = ArtistMeta()
    session.add(artistmeta_31)

    artist_ryan_teague = Artist()
    artist_ryan_teague.id = 249985
    artist_ryan_teague.gid = '5b922398-d7de-4f9c-94e4-59871430c002'
    artist_ryan_teague.name = u'Ryan Teague'
    artist_ryan_teague.sort_name = u'Teague, Ryan'
    artist_ryan_teague.comment = u''
    artist_ryan_teague.edits_pending = 0
    artist_ryan_teague.ended = False
    artist_ryan_teague.meta = artistmeta_31
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
    artistcredit_ryan_teague.ref_count = 98
    artistcredit_ryan_teague.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_prelude_iii.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_prelude_iii.artist_credit = artistcredit_ryan_teague
    track_prelude_iii.recording = recording_prelude_iii
    session.add(track_prelude_iii)

    artistmeta_32 = ArtistMeta()
    session.add(artistmeta_32)

    artist_greg_haines = Artist()
    artist_greg_haines.id = 366648
    artist_greg_haines.gid = '062b9fb1-4bb9-40b2-80a1-9bbf2be2d2cd'
    artist_greg_haines.name = u'Greg Haines'
    artist_greg_haines.sort_name = u'Haines, Greg'
    artist_greg_haines.comment = u''
    artist_greg_haines.edits_pending = 0
    artist_greg_haines.ended = False
    artist_greg_haines.meta = artistmeta_32
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
    artistcredit_greg_haines.ref_count = 80
    artistcredit_greg_haines.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_snow_airport.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_snow_airport.artist_credit = artistcredit_greg_haines
    track_snow_airport.recording = recording_snow_airport
    session.add(track_snow_airport)

    artistipi_7 = ArtistIPI()
    artistipi_7.ipi = u'00065393756'
    artistipi_7.edits_pending = 0
    artistipi_7.created = datetime.datetime(2012, 5, 15, 21, 4, 48, 684349)
    session.add(artistipi_7)

    artistmeta_33 = ArtistMeta()
    session.add(artistmeta_33)

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
    artist_gavin_bryars.last_updated = datetime.datetime(2012, 7, 10, 1, 8, 22, 712737)
    artist_gavin_bryars.ended = False
    artist_gavin_bryars.area = area_united_kingdom
    artist_gavin_bryars.gender = gender_male
    artist_gavin_bryars.ipis = [
        artistipi_7,
    ]
    artist_gavin_bryars.meta = artistmeta_33
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
    artistcredit_gavin_bryars.ref_count = 430
    artistcredit_gavin_bryars.created = datetime.datetime(2011, 5, 16, 18, 32, 11, 963929)
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
    track_tramp_with_orchestra_iii.last_updated = datetime.datetime(2011, 5, 16, 18, 8, 20, 288158)
    track_tramp_with_orchestra_iii.artist_credit = artistcredit_gavin_bryars
    track_tramp_with_orchestra_iii.recording = recording_tramp_with_orchestra_iii
    session.add(track_tramp_with_orchestra_iii)

    medium_3 = Medium()
    medium_3.id = 785487
    medium_3.position = 1
    medium_3.edits_pending = 0
    medium_3.last_updated = datetime.datetime(2011, 5, 16, 16, 57, 6, 530063)
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
    releasemeta_2.date_added = datetime.datetime(2011, 1, 1, 22, 34, 7, 280802)
    releasemeta_2.info_url = u'http://www.amazon.de/gp/product/B002JP1LCK'
    releasemeta_2.amazon_asin = u'B002JP1LCK'
    releasemeta_2.cover_art_presence = 'present'
    session.add(releasemeta_2)

    releasepackaging_digipak = ReleasePackaging()
    releasepackaging_digipak.id = 3
    releasepackaging_digipak.name = u'Digipak'
    session.add(releasepackaging_digipak)

    releasegroupmeta_2 = ReleaseGroupMeta()
    releasegroupmeta_2.release_count = 1
    releasegroupmeta_2.first_release_date_year = 2009
    session.add(releasegroupmeta_2)

    releasegroupsecondarytypejoin_2 = ReleaseGroupSecondaryTypeJoin()
    releasegroupsecondarytypejoin_2.created = datetime.datetime(2012, 5, 15, 2, 0)
    releasegroupsecondarytypejoin_2.secondary_type = releasegroupsecondarytype_compilation
    session.add(releasegroupsecondarytypejoin_2)

    releasegroup_xvi_reflections_on_classical_music = ReleaseGroup()
    releasegroup_xvi_reflections_on_classical_music.id = 1029754
    releasegroup_xvi_reflections_on_classical_music.gid = '8650e20f-39cc-45e2-b4fa-a5bb6de349ad'
    releasegroup_xvi_reflections_on_classical_music.name = u'XVI Reflections on Classical Music'
    releasegroup_xvi_reflections_on_classical_music.comment = u''
    releasegroup_xvi_reflections_on_classical_music.edits_pending = 0
    releasegroup_xvi_reflections_on_classical_music.last_updated = datetime.datetime(2012, 5, 15, 21, 1, 58, 718541)
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
    session.add(releasestatus_official)

    release_xvi_reflections_on_classical_music = Release()
    release_xvi_reflections_on_classical_music.id = 785487
    release_xvi_reflections_on_classical_music.gid = '7643ee96-fe19-4b76-aa9a-e8af7d0e9d73'
    release_xvi_reflections_on_classical_music.name = u'XVI Reflections on Classical Music'
    release_xvi_reflections_on_classical_music.barcode = u'0028948022205'
    release_xvi_reflections_on_classical_music.comment = u''
    release_xvi_reflections_on_classical_music.edits_pending = 0
    release_xvi_reflections_on_classical_music.quality = -1
    release_xvi_reflections_on_classical_music.last_updated = datetime.datetime(2013, 10, 6, 11, 39, 8, 511181)
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

    area_westminster = Area()
    area_westminster.id = 3906
    area_westminster.gid = '48d08ee1-db45-4566-bb1d-c47ab6dbaf98'
    area_westminster.name = u'Westminster'
    area_westminster.sort_name = u'Westminster'
    area_westminster.edits_pending = 0
    area_westminster.last_updated = datetime.datetime(2013, 5, 21, 16, 51, 57, 923559)
    area_westminster.ended = False
    area_westminster.comment = u''
    area_westminster.type = areatype_subdivision
    session.add(area_westminster)

    placetype_studio = PlaceType()
    placetype_studio.id = 1
    placetype_studio.name = u'Studio'
    session.add(placetype_studio)

    place_abbey_road_studios = Place()
    place_abbey_road_studios.id = 775
    place_abbey_road_studios.gid = 'bd55aeb7-19d1-4607-a500-14b8479d3fed'
    place_abbey_road_studios.name = u'Abbey Road Studios'
    place_abbey_road_studios.address = u"3 Abbey Road, St John's Wood, London"
    place_abbey_road_studios.coordinates = (51.53192, -0.17835)
    place_abbey_road_studios.comment = u''
    place_abbey_road_studios.edits_pending = 0
    place_abbey_road_studios.last_updated = datetime.datetime(2013, 10, 18, 17, 0, 17, 553196)
    place_abbey_road_studios.begin_date_year = 1931
    place_abbey_road_studios.ended = False
    place_abbey_road_studios.area = area_westminster
    place_abbey_road_studios.type = placetype_studio
    session.add(place_abbey_road_studios)

    area_japan = Area()
    area_japan.id = 107
    area_japan.gid = '2db42837-c832-3c27-b4a3-08198f75693c'
    area_japan.name = u'Japan'
    area_japan.sort_name = u'Japan'
    area_japan.edits_pending = 0
    area_japan.last_updated = datetime.datetime(2013, 5, 27, 14, 29, 56, 162248)
    area_japan.ended = False
    area_japan.comment = u''
    area_japan.type = areatype_country
    session.add(area_japan)

    labelipi_1 = LabelIPI()
    labelipi_1.ipi = u'00173517959'
    labelipi_1.edits_pending = 0
    labelipi_1.created = datetime.datetime(2013, 9, 20, 11, 17, 40, 201068)
    session.add(labelipi_1)

    labelipi_2 = LabelIPI()
    labelipi_2.ipi = u'00473554732'
    labelipi_2.edits_pending = 0
    labelipi_2.created = datetime.datetime(2013, 9, 20, 11, 17, 40, 201068)
    session.add(labelipi_2)

    labelisni_1 = LabelISNI()
    labelisni_1.isni = u'000000011781560X'
    labelisni_1.edits_pending = 0
    labelisni_1.created = datetime.datetime(2013, 9, 20, 11, 17, 40, 201068)
    session.add(labelisni_1)

    labelmeta_3 = LabelMeta()
    session.add(labelmeta_3)

    label_studio_ghibli = Label()
    label_studio_ghibli.id = 83683
    label_studio_ghibli.gid = 'ecc049d0-88a6-4806-a5b7-0f1367a7d6e1'
    label_studio_ghibli.name = u'\u30b9\u30bf\u30b8\u30aa\u30b8\u30d6\u30ea'
    label_studio_ghibli.sort_name = u'Studio Ghibli'
    label_studio_ghibli.begin_date_year = 1985
    label_studio_ghibli.begin_date_month = 6
    label_studio_ghibli.comment = u''
    label_studio_ghibli.edits_pending = 0
    label_studio_ghibli.last_updated = datetime.datetime(2013, 9, 20, 11, 17, 40, 201068)
    label_studio_ghibli.ended = False
    label_studio_ghibli.area = area_japan
    label_studio_ghibli.ipis = [
        labelipi_1,
        labelipi_2,
    ]
    label_studio_ghibli.isnis = [
        labelisni_1,
    ]
    label_studio_ghibli.meta = labelmeta_3
    label_studio_ghibli.type = labeltype_production
    session.add(label_studio_ghibli)

    session.commit()
