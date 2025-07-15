from unittest import TestCase

from uk_election_ids.metadata_tools import (
    PostalVotingRequirementsMatcher,
)


class TestPostalVotingRequirements(TestCase):
    def test_ea_2022(self):
        ids = [
            [["parl.division.2024-05-02"], {"nation": "SCT"}],
            [["parl.division.2024-05-02"], {"nation": "ENG"}],
            [["parl.division.2024-05-02"], {"nation": "WLS"}],
            [["parl.division.by.2024-05-02"], {"nation": "SCT"}],
            [["parl.division.by.2024-05-02"], {"nation": "ENG"}],
            [["parl.division.by.2024-05-02"], {"nation": "WLS"}],
            [["local.division.2024-05-02"], {"nation": "ENG"}],
            [["gla.a.2024-05-02"], {}],
            [["gla.c.division.2024-05-02"], {}],
            [["pcc.organisation.2024-05-02"], {}],
            [["mayor.organisation.2024-05-02"], {}],
        ]
        for args, kwargs in ids:
            with self.subTest(args=args, kwargs=kwargs):
                matcher = PostalVotingRequirementsMatcher(*args, **kwargs)
                self.assertEqual(
                    matcher.get_postal_voting_requirements(),
                    "EA-2022",
                )

    def test_rpa2000(self):
        ids = [
            [["local.division.2024-05-02"], {"nation": "SCT"}],
            [["local.division.2024-05-02"], {"nation": "WLS"}],
            [["local.division.2019-05-02"], {"nation": "ENG"}],
            [["parl.division.by.2023-10-30"], {"nation": "SCT"}],
            [["parl.division.by.2023-10-30"], {"nation": "ENG"}],
            [["parl.division.by.2023-10-30"], {"nation": "WLS"}],
            [["parl.division.by.2002-08-30"], {"nation": "NIR"}],
            [["gla.a.2019-05-02"], {}],
            [["gla.c.division.2019-05-02"], {}],
            [["pcc.organisation.2019-05-02"], {}],
            [["mayor.organisation.2019-05-02"], {}],
        ]
        for args, kwargs in ids:
            with self.subTest(args=args, kwargs=kwargs):
                matcher = PostalVotingRequirementsMatcher(*args, **kwargs)
                self.assertEqual(
                    matcher.get_postal_voting_requirements(),
                    "RPA2000",
                )

    def test_efa2002(self):
        ids = [
            [["parl.division.2019-05-02"], {"nation": "NIR"}],
            [["parl.division.by.2019-05-02"], {"nation": "NIR"}],
            [["local.division.2019-05-02"], {"nation": "NIR"}],
            [["nia.2019-05-02"], {}],
            [["nia.division.2019-05-02"], {}],
        ]
        for args, kwargs in ids:
            with self.subTest(args=args, kwargs=kwargs):
                matcher = PostalVotingRequirementsMatcher(*args, **kwargs)
                self.assertEqual(
                    matcher.get_postal_voting_requirements(),
                    "EFA-2002",
                )

    def test_null(self):
        ids = [
            [["parl.division.2002-08-30"], {"nation": "NIR"}],
            [["local.division.2002-08-30"], {"nation": "NIR"}],
            [["nia.2002-08-30"], {}],
            [["nia.division.2002-08-30"], {}],
        ]
        for args, kwargs in ids:
            with self.subTest(args=args, kwargs=kwargs):
                matcher = PostalVotingRequirementsMatcher(*args, **kwargs)
                self.assertIsNone(matcher.get_postal_voting_requirements())

    def test_errors(self):
        ids = [
            [["parl.division.2024-05-02"], {}],
            [["parl.division.by.2024-05-02"], {}],
            [["local.division.2024-05-02"], {}],
        ]
        for args, kwargs in ids:
            matcher = PostalVotingRequirementsMatcher(*args, **kwargs)
            with self.assertRaises(ValueError):
                matcher.get_postal_voting_requirements()
