from unittest import TestCase

from uk_election_ids.metadata_tools import VotingSystemMatcher


class TestVotingSystemMatcher(TestCase):
    def test_local(self):
        self.assertEqual(
            VotingSystemMatcher(
                "local.stroud.2022-05-04", nation="ENG"
            ).get_voting_system(),
            "FPTP",
        )
        self.assertEqual(
            VotingSystemMatcher(
                "local.belfast.2022-05-04", nation="NIR"
            ).get_voting_system(),
            "STV",
        )
        with self.assertRaises(ValueError):
            VotingSystemMatcher("local.2022-05-04").get_voting_system()

    def test_mayor(self):
        self.assertEqual(
            VotingSystemMatcher("mayor.stroud.2022-05-04").get_voting_system(),
            "sv",
        )
        self.assertEqual(
            VotingSystemMatcher("mayor.stroud.2024-05-04").get_voting_system(),
            "FPTP",
        )

    def test_pcc(self):
        self.assertEqual(
            VotingSystemMatcher(
                "pcc.gloucestershire.2022-05-04"
            ).get_voting_system(),
            "sv",
        )
        self.assertEqual(
            VotingSystemMatcher(
                "pcc.gloucestershire.2024-05-04"
            ).get_voting_system(),
            "FPTP",
        )

    def test_senedd_with_subtypes(self):
        for id_ in [
            "senedd.r.mid-and-west-wales.2021-05-06",
            "senedd.r.2021-05-06",
        ]:
            self.assertEqual(
                VotingSystemMatcher(id_).get_voting_system(),
                "AMS",
            )
        for id_ in [
            "senedd.c.swansea-east.2021-05-06",
            "senedd.c.2021-05-06",
        ]:
            self.assertEqual(
                VotingSystemMatcher(id_).get_voting_system(),
                "FPTP",
            )

        for id_ in [
            "senedd.r.mid-and-west-wales.2026-05-07",
            "senedd.r.2026-05-07",
        ]:
            with self.assertRaises(ValueError):
                VotingSystemMatcher(id_).get_voting_system()
        for id_ in [
            "senedd.c.swansea-east.2026-05-07",
            "senedd.c.2026-05-07",
        ]:
            with self.assertRaises(ValueError):
                VotingSystemMatcher(id_).get_voting_system()

    def test_senedd_without_subtypes(self):
        for id_ in [
            "senedd.pen-y-bont-bro-morgannwg.2026-05-07",
            "senedd.2026-05-07",
        ]:
            self.assertEqual(
                VotingSystemMatcher(id_).get_voting_system(),
                "PR-CL",
            )

        for id_ in [
            "senedd.pen-y-bont-bro-morgannwg.2021-05-06",
            "senedd.2021-05-06",
        ]:
            with self.assertRaises(ValueError):
                VotingSystemMatcher(id_).get_voting_system()

    def test_ams(self):
        for id_ in [
            "sp.c.aberdeen-central.2021-05-06",
            "sp.c.2021-05-06",
            "gla.c.barnet-and-camden.2024-05-02",
            "gla.c.2024-05-02",
        ]:
            self.assertEqual(
                VotingSystemMatcher(id_).get_voting_system(),
                "FPTP",
            )

        for id_ in [
            "sp.r.central-scotland.2021-05-06",
            "sp.r.2021-05-06",
            "gla.a.2024-05-02",
        ]:
            self.assertEqual(
                VotingSystemMatcher(id_).get_voting_system(),
                "AMS",
            )
        for id_ in [
            "sp.2021-05-06",
            "gla.2024-05-02",
        ]:
            with self.assertRaises(ValueError):
                VotingSystemMatcher(id_).get_voting_system()
