from unittest import TestCase
from uk_election_ids.metadata_tools import IDRequirementsMatcher


class TestMetaDataMatcher(TestCase):
    def test_meta_data_matcher_regex(self):
        matcher = IDRequirementsMatcher("parl.corby.2022-05-04", nation="ENG")
        assert matcher.match_id()[0] == "parl"

        matcher = IDRequirementsMatcher("parl.stroud.by.2022-05-04", nation="ENG")
        assert matcher.match_id()[0] == "parl.*.by"

        matcher = IDRequirementsMatcher("parl.reading.tilehurst.by.2022-05-04", nation="ENG")
        assert matcher.match_id()[0] == "parl.*.by"

        matcher = IDRequirementsMatcher("nonsense.parl.stroud.by.2022-05-04", nation="ENG")
        assert matcher.match_id()[0] is None
