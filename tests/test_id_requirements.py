import json
from pathlib import Path
from unittest import TestCase

from uk_election_ids.metadata_tools import IDRequirementsMatcher


class TestIDRequirementsJson(TestCase):
    def test_defaults_valid_id_requirements(self):
        with Path("uk_election_ids/data/id_requirements.json").open() as f:
            id_requirements = json.load(f)

        def iter_defaults(data: dict, parent=None):
            default = data.get("default", "")
            if default == "" and parent not in ["dates", "nations"]:
                self.assertTrue(
                    any(key in ["nations", "dates"] for key in data),
                    msg=f"{data} requires either a `default`, `nations` or `dates` key",
                )
            for key, value in data.items():
                if isinstance(value, dict):
                    iter_defaults(value, parent=key)

        for key, top_level_data in id_requirements["defaults"].items():
            iter_defaults(top_level_data)


class TestIDRequirementsMatcher(TestCase):
    def test_matcher_england(self):
        # Local election pre 2022 legislation
        result = IDRequirementsMatcher("local.stroud.2022-05-04", nation="ENG")
        assert result.get_id_requirements() is None

        # Local election post 2022 legislation
        result = IDRequirementsMatcher("local.stroud.2023-05-04", nation="ENG")
        assert result.get_id_requirements() == "EA-2022"

        # UK parliamentary election pre 2022 legislation
        result = IDRequirementsMatcher("parl.2023-05-04", nation="ENG")
        assert result.get_id_requirements() is None

        # UK parliamentary election post 2022 legislation
        result = IDRequirementsMatcher("parl.2023-10-03", nation="ENG")
        assert result.get_id_requirements() == "EA-2022"

        # UK parliamentary by-election post 2022 legislation
        result = IDRequirementsMatcher(
            "parl.stroud.by.2023-05-04", nation="ENG"
        )
        assert result.get_id_requirements() == "EA-2022"

        # Local election on 2018 pilot scheme
        result = IDRequirementsMatcher("local.woking.2018-05-03", nation="ENG")
        assert result.get_id_requirements() == "pilot-2018"

        # Local election not on 2018 pilot scheme
        result = IDRequirementsMatcher("local.stroud.2018-05-03", nation="ENG")
        assert result.get_id_requirements() is None

        # Local election on 2019 pilot scheme
        result = IDRequirementsMatcher("local.woking.2019-05-02", nation="ENG")
        assert result.get_id_requirements() == "pilot-2019"

        # Local election not on 2019 pilot scheme
        result = IDRequirementsMatcher("local.stroud.2019-05-02", nation="ENG")
        assert result.get_id_requirements() is None

        # GLA pre-2022 legislation
        result = IDRequirementsMatcher(
            "gla.c.brent-and-harrow.2016-05-05", nation="ENG"
        )
        assert result.get_id_requirements() is None

        # GLA post 2022 legislation
        result = IDRequirementsMatcher(
            "gla.c.brent-and-harrow.2023-05-04", nation="ENG"
        )
        assert result.get_id_requirements() == "EA-2022"

        # City of London Local elections (Common Councilman)
        result = IDRequirementsMatcher(
            "local.city-of-london.bishopsgate.2025-03-20", nation="ENG"
        )
        assert result.get_id_requirements() is None

        # City of London Local elections (Alderman)
        result = IDRequirementsMatcher(
            "local.city-of-london-alder.bishopsgate.2025-03-20", nation="ENG"
        )
        assert result.get_id_requirements() is None

    def test_matcher_scotland(self):
        # Local election pre 2022 legislation
        result = IDRequirementsMatcher("local.stroud.2022-05-04", nation="SCT")
        assert result.get_id_requirements() is None

        # Local election post 2022 legislation
        result = IDRequirementsMatcher("local.stroud.2023-05-04", nation="SCT")
        assert result.get_id_requirements() is None

        # UK parliamentary election post 2022 legislation
        result = IDRequirementsMatcher("parl.2023-10-03", nation="SCT")
        assert result.get_id_requirements() == "EA-2022"

        # Scottish parliamentary election post 2022 legislation
        result = IDRequirementsMatcher("sp.c.2023-10-03", nation="SCT")
        assert result.get_id_requirements() is None

        # UK parliamentary by-election post 2022 legislation
        result = IDRequirementsMatcher(
            "parl.stroud.by.2023-05-04", nation="SCT"
        )
        assert result.get_id_requirements() == "EA-2022"

    def test_matcher_wales(self):
        # Local election pre 2022 legislation
        result = IDRequirementsMatcher("local.stroud.2022-05-04", nation="WLS")
        assert result.get_id_requirements() is None

        # Local election post 2022 legislation
        result = IDRequirementsMatcher("local.stroud.2023-05-04", nation="WLS")
        assert result.get_id_requirements() is None

        # UK parliamentary election post 2022 legislation
        result = IDRequirementsMatcher("parl.2023-10-03", nation="WLS")
        assert result.get_id_requirements() == "EA-2022"

        # Senedd post 2022 legislation
        result = IDRequirementsMatcher("senedd.r.2023-05-04", nation="WLS")
        assert result.get_id_requirements() is None

        # NAW election post 2022 legislation
        result = IDRequirementsMatcher("naw.2023-05-04", nation="WLS")
        assert result.get_id_requirements() is None

        # PCC election post 2022 legislation
        result = IDRequirementsMatcher("pcc.2023-05-04", nation="WLS")
        assert result.get_id_requirements() == "EA-2022"

        # UK parliamentary by-election post 2022 legislation
        result = IDRequirementsMatcher(
            "parl.stroud.by.2023-05-04", nation="WLS"
        )
        assert result.get_id_requirements() == "EA-2022"

    def test_matcher_ni(self):
        # Parliamentary election pre 2022 legislation
        result = IDRequirementsMatcher("parl.2022-05-04", nation="NIR")
        assert result.get_id_requirements() == "EFA-2002"

        # Parliamentary election post 2022 legislation
        result = IDRequirementsMatcher("parl.2023-10-03", nation="NIR")
        assert result.get_id_requirements() == "EFA-2002"

        # Parliamentary election pre 2002 legislation
        result = IDRequirementsMatcher("parl.2001-11-28", nation="NIR")
        assert result.get_id_requirements() is None

        # NIA election pre 2002 legislation
        result = IDRequirementsMatcher("nia.2001-11-28", nation="NIR")
        assert result.get_id_requirements() is None

        # NIA election post 2002 legislation
        result = IDRequirementsMatcher("nia.2002-11-28", nation="NIR")
        assert result.get_id_requirements() == "EFA-2002"

        # UK parliamentary by-election post 2022 legislation
        result = IDRequirementsMatcher(
            "parl.stroud.by.2023-05-04", nation="NIR"
        )
        assert result.get_id_requirements() == "EFA-2002"
