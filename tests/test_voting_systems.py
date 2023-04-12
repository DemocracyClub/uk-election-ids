import json
from pathlib import Path
from unittest import TestCase

from uk_election_ids.metadata_tools import VotingSystemMatcher


class TestVotingSystemJson(TestCase):
    def test_defaults_valid_voting_systems(self):
        voting_systems = json.load(
            Path("uk_election_ids/data/voting_systems.json").open()
        )

        def iter_defaults(data: dict, parent=None):
            default = data.get("default", None)
            if not default and parent not in ["dates", "nations"]:
                self.assertTrue(
                    any(
                        [key in ["nations", "dates"] for key in data]
                    ),
                    msg=f"{data} requires either a `default`, `nations` or `dates` key",
                )
            for key, value in data.items():
                if isinstance(value, dict):
                    iter_defaults(value, parent=key)

        for key, top_level_data in voting_systems["defaults"].items():
            iter_defaults(top_level_data)


class TestVotingSystemMatcher(TestCase):
    def test_basic_matcher(self):
        matcher = VotingSystemMatcher("local.stroud.2022-05-04", nation="ENG")
        self.assertEqual(matcher.get_voting_system(), "FPTP")
        matcher = VotingSystemMatcher("local.stroud.2022-05-04", nation="NIR")
        self.assertEqual(matcher.get_voting_system(), "STV")
        matcher = VotingSystemMatcher("mayor.stroud.2022-05-04")
        self.assertEqual(matcher.get_voting_system(), "sv")
        matcher = VotingSystemMatcher("mayor.stroud.2024-05-04")
        self.assertEqual(matcher.get_voting_system(), "FPTP")
