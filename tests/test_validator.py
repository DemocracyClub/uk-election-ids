from unittest import TestCase

from uk_election_ids.election_ids import validate


class TestValidator(TestCase):
    def test_valid_ids(self):
        valid_ids = [
            "naw.2016-05-05",
            "naw.r.2016-05-05",
            "naw.r.mid-and-west-wales.2016-05-05",
            "naw.r.mid-and-west-wales.by.2016-05-05",
            "senedd.r.mid-and-west-wales.2021-05-06",
            "senedd.r.mid-and-west-wales.by.2021-05-06",
            "senedd.pen-y-bont-bro-morgannwg.2026-05-07",
            "senedd.pen-y-bont-bro-morgannwg.by.2026-05-07",
            "sp.2019-08-29",
            "sp.c.2019-08-29",
            "sp.c.shetland-islands.2019-08-29",
            "sp.c.shetland-islands.by.2019-08-29",
            "nia.2017-03-02",
            "nia.fermanagh-and-south-tyrone.2017-03-02",
            "nia.fermanagh-and-south-tyrone.by.2017-03-02",
            "parl.2017-06-08",
            "parl.aberdeen-south.2017-06-08",
            "parl.aberdeen-south.by.2017-06-08",
            "local.2019-08-22",
            "local.rugby.2019-08-22",
            "local.rugby.rokeby-and-overslade.2019-08-22",
            "local.rugby.rokeby-and-overslade.by.2019-08-22",
            "mayor.2019-05-02",
            "mayor.bedford.2019-05-02",
            "mayor.bedford.by.2019-05-02",
            "pcc.2019-07-18",
            "pcc.northumbria.2019-07-18",
            "pcc.northumbria.by.2019-07-18",
            "gla.2016-05-05",
            "gla.c.2016-05-05",
            "gla.c.barnet-and-camden.2016-05-05",
            "gla.c.barnet-and-camden.by.2016-05-05",
            "europarl.2014-05-22",
            "europarl.uk-wales.2014-05-22",
            "ref.croydon.2021-10-07",
            "ref.2021-10-07",
        ]
        for id_ in valid_ids:
            with self.subTest(id_=id_):
                self.assertTrue(validate(id_))

    def test_invalid_ids(self):
        invalid_ids = [
            7,  # not string
            False,  # not string
            {},  # not string
            [],  # not string
            "foobar.2019-01-10",  # not an id type
            "foobar",  # random string
            "foo.bar",  # doesn't end with a date
            "local.2019-02-31",  # not a real date
            "local.chips",  # not even slightly a date
            "local.we$tward-ho!.2019-01-10",  # invalid chars
            "parl.c.aberavon.2019-01-01",  # should not have a subtype
            "naw.aberavon.2019-01-01",  # should have a subtype
            "ref.croydon.by.2021-10-07",  # there is no such thing as a by-referendum
            # invalid subtypes
            "gla.r.barnet-and-camden.2016-05-05",
            "naw.x.2019-01-01",
            "senedd.x.mid-and-west-wales.2021-05-06",
            # too many clauses
            "naw.r.mid-and-west-wales.something-else.2016-05-05",
            "senedd.pen-y-bont-bro-morgannwg.something-else.2026-05-07",
            "sp.c.shetland-islands.something-else.2019-08-29",
            "nia.fermanagh-and-south-tyrone.something-else.2017-03-02",
            "parl.aberdeen-south.something-else.2017-06-08",
            "local.rugby.rokeby-and-overslade.something-else.2019-08-22",
            "mayor.bedford.something-else.2019-05-02",
            "pcc.northumbria.something-else.2019-07-18",
            "gla.c.barnet-and-camden.something-else.2016-05-05",
            "europarl.uk-wales.something-else.2014-05-22",
            "ref.croydon.some-division.something-else.2021-10-07",
        ]
        for id_ in invalid_ids:
            with self.subTest(id_=id_):
                self.assertFalse(validate(id_))
