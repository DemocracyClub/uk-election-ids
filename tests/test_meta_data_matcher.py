from unittest import TestCase

from uk_election_ids.metadata_tools import (
    IDRequirementsMatcher,
    PostalVotingRequirementsMatcher,
)


class TestMetaDataMatcher(TestCase):
    def test_meta_data_matcher_regex(self):
        matcher = IDRequirementsMatcher("parl.corby.2022-05-04", nation="ENG")
        assert matcher.match_id()[0] == "parl"

        matcher = IDRequirementsMatcher(
            "parl.stroud.by.2022-05-04", nation="ENG"
        )
        assert matcher.match_id()[0] == "parl.*.by"

        matcher = IDRequirementsMatcher(
            "parl.reading.tilehurst.by.2022-05-04", nation="ENG"
        )
        assert matcher.match_id()[0] == "parl.*.by"

        matcher = IDRequirementsMatcher(
            "nonsense.parl.stroud.by.2022-05-04", nation="ENG"
        )
        assert matcher.match_id()[0] is None


class TestPostalVotingRequirements(TestCase):
    def test_postal_voting(self):
        matcher = PostalVotingRequirementsMatcher("parl.stroud.2024-05-02")
        self.assertEqual(matcher.get_postal_voting_requirements(), "EA-2022")

        matcher = PostalVotingRequirementsMatcher("parl.stroud.2019-05-02")
        self.assertEqual(matcher.get_postal_voting_requirements(), "RPA2000")

        matcher = PostalVotingRequirementsMatcher(
            "parl.stroud.2019-05-02", nation="NIR"
        )
        self.assertEqual(matcher.get_postal_voting_requirements(), "EFA-2002")
