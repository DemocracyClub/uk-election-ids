from unittest import TestCase

from uk_election_ids.metadata_tools import VotingSystemMatcher


class TestVotingSystemMatcher(TestCase):
    def test_valid(self):
        test_cases = [
            [["local.stroud.2022-05-04"], {"nation": "ENG"}, "FPTP"],
            [["local.belfast.2022-05-04"], {"nation": "NIR"}, "STV"],
            [["mayor.stroud.2022-05-04"], {}, "sv"],
            [["mayor.stroud.2024-05-04"], {}, "FPTP"],
            [["pcc.gloucestershire.2022-05-04"], {}, "sv"],
            [["pcc.gloucestershire.2024-05-04"], {}, "FPTP"],
            [["senedd.r.mid-and-west-wales.2021-05-06"], {}, "AMS"],
            [["senedd.r.2021-05-06"], {}, "AMS"],
            [["senedd.c.swansea-east.2021-05-06"], {}, "FPTP"],
            [["senedd.c.2021-05-06"], {}, "FPTP"],
            [["senedd.pen-y-bont-bro-morgannwg.2026-05-07"], {}, "PR-CL"],
            [["senedd.2026-05-07"], {}, "PR-CL"],
            [["sp.c.aberdeen-central.2021-05-06"], {}, "FPTP"],
            [["sp.c.2021-05-06"], {}, "FPTP"],
            [["gla.c.barnet-and-camden.2024-05-02"], {}, "FPTP"],
            [["gla.c.2024-05-02"], {}, "FPTP"],
            [["sp.r.central-scotland.2021-05-06"], {}, "AMS"],
            [["sp.r.2021-05-06"], {}, "AMS"],
            [["gla.a.2024-05-02"], {}, "AMS"],
        ]
        for args, kwargs, expected in test_cases:
            with self.subTest(args=args, kwargs=kwargs, expected=expected):
                self.assertEqual(
                    VotingSystemMatcher(*args, **kwargs).get_voting_system(),
                    expected,
                )

    def test_invalid(self):
        invalid_ids = (
            [
                # Local elections may contain a mix of voting systems
                "local.2022-05-04",
            ]
            + [
                # Senedd subtype elections after 2026-05-07 doesn't make sense
                "senedd.r.mid-and-west-wales.2026-05-07",
                "senedd.r.2026-05-07",
                "senedd.c.swansea-east.2026-05-07",
                "senedd.c.2026-05-07",
            ]
            + [
                # Senedd elections without subtype before 2026-05-07 doesn't make sense
                "senedd.pen-y-bont-bro-morgannwg.2021-05-06",
            ]
            + [
                # Contain a mix of AMS and FPTP
                "senedd.2021-05-06",
                "sp.2021-05-06",
                "gla.2024-05-02",
            ]
        )
        for id_ in invalid_ids:
            with self.subTest(id_=id_), self.assertRaises(ValueError):
                VotingSystemMatcher(id_).get_voting_system()
