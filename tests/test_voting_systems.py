from unittest import TestCase

from uk_election_ids.metadata_tools import VotingSystemMatcher


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
