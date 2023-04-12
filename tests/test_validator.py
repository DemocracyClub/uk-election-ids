from unittest import TestCase

from uk_election_ids.election_ids import validate


class TestValidator(TestCase):
    def test_valid_ids(self):
        self.assertTrue(validate("naw.2016-05-05"))
        self.assertTrue(validate("naw.r.2016-05-05"))
        self.assertTrue(validate("naw.r.mid-and-west-wales.2016-05-05"))
        self.assertTrue(validate("naw.r.mid-and-west-wales.by.2016-05-05"))
        self.assertTrue(validate("sp.2019-08-29"))
        self.assertTrue(validate("sp.c.2019-08-29"))
        self.assertTrue(validate("sp.c.shetland-islands.2019-08-29"))
        self.assertTrue(validate("sp.c.shetland-islands.by.2019-08-29"))
        self.assertTrue(validate("nia.2017-03-02"))
        self.assertTrue(validate("nia.fermanagh-and-south-tyrone.2017-03-02"))
        self.assertTrue(
            validate("nia.fermanagh-and-south-tyrone.by.2017-03-02")
        )
        self.assertTrue(validate("parl.2017-06-08"))
        self.assertTrue(validate("parl.aberdeen-south.2017-06-08"))
        self.assertTrue(validate("parl.aberdeen-south.by.2017-06-08"))
        self.assertTrue(validate("local.2019-08-22"))
        self.assertTrue(validate("local.rugby.2019-08-22"))
        self.assertTrue(validate("local.rugby.rokeby-and-overslade.2019-08-22"))
        self.assertTrue(
            validate("local.rugby.rokeby-and-overslade.by.2019-08-22")
        )
        self.assertTrue(validate("mayor.2019-05-02"))
        self.assertTrue(validate("mayor.bedford.2019-05-02"))
        self.assertTrue(validate("mayor.bedford.by.2019-05-02"))
        self.assertTrue(validate("pcc.2019-07-18"))
        self.assertTrue(validate("pcc.northumbria.2019-07-18"))
        self.assertTrue(validate("pcc.northumbria.by.2019-07-18"))
        self.assertTrue(validate("gla.2016-05-05"))
        self.assertTrue(validate("gla.c.2016-05-05"))
        self.assertTrue(validate("gla.c.barnet-and-camden.2016-05-05"))
        self.assertTrue(validate("gla.c.barnet-and-camden.by.2016-05-05"))
        self.assertTrue(validate("europarl.2014-05-22"))
        self.assertTrue(validate("europarl.uk-wales.2014-05-22"))
        self.assertTrue(validate("ref.croydon.2021-10-07"))
        self.assertTrue(validate("ref.2021-10-07"))

    def test_invalid_ids(self):
        self.assertFalse(validate(7))  # not string
        self.assertFalse(validate(False))  # not string
        self.assertFalse(validate({}))  # not string
        self.assertFalse(validate([]))  # not string
        self.assertFalse(validate("foobar.2019-01-10"))  # not an id type
        self.assertFalse(validate("foobar"))  # random string
        self.assertFalse(validate("foo.bar"))  # doesn't end with a date
        self.assertFalse(validate("local.2019-02-31"))  # not a real date
        self.assertFalse(validate("local.chips"))  # not even slightly a date
        self.assertFalse(
            validate("local.we$tward-ho!.2019-01-10")
        )  # invalid chars
        self.assertFalse(
            validate("parl.c.aberavon.2019-01-01")
        )  # should not have a subtype
        self.assertFalse(
            validate("naw.aberavon.2019-01-01")
        )  # should have a subtype
        self.assertFalse(
            validate("gla.r.barnet-and-camden.2016-05-05")
        )  # invalid subtype
        self.assertFalse(validate("naw.x.2019-01-01"))  # invalid subtype
        self.assertFalse(
            validate("ref.croydon.by.2021-10-07")
        )  # there is no such thing as a by-referendum
        # too many clauses
        self.assertFalse(
            validate("naw.r.mid-and-west-wales.something-else.2016-05-05")
        )
        self.assertFalse(
            validate("sp.c.shetland-islands.something-else.2019-08-29")
        )
        self.assertFalse(
            validate("nia.fermanagh-and-south-tyrone.something-else.2017-03-02")
        )
        self.assertFalse(
            validate("parl.aberdeen-south.something-else.2017-06-08")
        )
        self.assertFalse(
            validate(
                "local.rugby.rokeby-and-overslade.something-else.2019-08-22"
            )
        )
        self.assertFalse(validate("mayor.bedford.something-else.2019-05-02"))
        self.assertFalse(validate("pcc.northumbria.something-else.2019-07-18"))
        self.assertFalse(
            validate("gla.c.barnet-and-camden.something-else.2016-05-05")
        )
        self.assertFalse(
            validate("europarl.uk-wales.something-else.2014-05-22")
        )
        self.assertFalse(
            validate("ref.croydon.some-division.something-else.2021-10-07")
        )
