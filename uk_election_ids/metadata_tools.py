import datetime
import json
import re
from pathlib import Path
from typing import Optional


class MetaDataMatcher:
    """
    Given an election ID and optional nation, match to
    a data file to get additional properties about the ID.

    The data file is in the election ID metadata format specified in test/data_schema.py
    """

    def __init__(
        self,
        election_id: str,
        nation: Optional[str] = None,
    ) -> None:
        self.nation = nation
        self.election_id = election_id
        self.parts = self.election_id.split(".")
        self.date = self._parse_date(self.parts[-1])

    DATA = {"defaults": {}}

    def _escape_id_part(self, id_part: str) -> str:
        r"""
        Allow use of our slightly modified patterns in the ID requirements json file
        by escaping operator literals and appending additional operators to patterns where needed.

        In our use case, '*' represents 0-many wildcards and '.' represents a string literal.
        Additionally, if wildcard is empty, regex needs reduced '.' literals .

        i.e. 'parl.*.by' becomes the slightly more esoteric 'parl(\..*)?\.by' where:
        \. represents a literal '.', always present at the start of a wildcard
        (\..*) captures a sequence of "[any characters]."
        ? captures a group between 0-1 times
        """
        id_part = id_part.replace(
            "-", r"\-"
        )  # prevent '-' from being interpreted as range indicator
        return id_part.replace(".*.", r"\.(.*\.)?")

    def match_id(self):
        """
        Match the most specific key to this ID

        """
        ids_with_defaults = self.DATA["defaults"].keys()
        ids_with_defaults = sorted(
            ids_with_defaults,
            key=lambda identifier: identifier.count("."),
            reverse=True,
        )
        matched_id_pattern = None
        matched_default_value = None

        for id_part in ids_with_defaults:
            pattern = re.compile(
                rf"""
                ^                                   # String begins with id_part
                ({self._escape_id_part(id_part)})   # e.g. parl.*.by, local, etc. - the bit we're interested in matching
                (\..*|$)                            # id_part is followed by '.[any characters]' or nothing
            """,
                re.VERBOSE,
            )

            if bool(pattern.search(self.election_id)):
                matched_id_pattern = id_part
                matched_default_value = self.DATA["defaults"].get(id_part)
                break

        return (matched_id_pattern, matched_default_value)

    def _parse_date(self, date: Optional[str]) -> datetime.date:
        if not date:
            return None
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()

    def match_dates(self, data):
        for key, value in data.items():
            start, end = [self._parse_date(x) for x in key.split(":")]
            if not start:
                start = datetime.date(year=1, month=1, day=1)
            if not end:
                end = datetime.date(year=9999, month=12, day=31)

            if self.date >= start and self.date < end:
                return value
        raise ValueError("No date for range")


class VotingSystemMatcher(MetaDataMatcher):
    path = Path(__file__).parent / "data" / "voting_systems.json"
    DATA = json.load(path.open())

    def get_voting_system(self):
        id_part, data = self.match_id()
        if self.nation and self.nation in data.get("nations", {}):
            data = data["nations"][self.nation]

        if data.get("dates"):
            data = self.match_dates(data["dates"])

        default = data.get("default", None)
        if not default:
            required_keys = data.keys()
            raise ValueError(f"{id_part} requires {' or '.join(required_keys)}")

        return data["default"]


class IDRequirementsMatcher(MetaDataMatcher):
    path = Path(__file__).parent / "data" / "id_requirements.json"
    DATA = json.load(path.open())

    def get_id_requirements(self):
        id_part, data = self.match_id()
        if self.nation and self.nation in data.get("nations", {}):
            data = data["nations"][self.nation]

        if data.get("dates"):
            data = self.match_dates(data["dates"])

        default = data.get("default", "")
        if default == "":
            required_keys = data.keys()
            raise ValueError(f"{id_part} requires {' or '.join(required_keys)}")

        return data["default"]


class PostalVotingRequirementsMatcher(MetaDataMatcher):
    path = Path(__file__).parent / "data" / "postal_votes.json"
    DATA = json.load(path.open())

    def get_postal_voting_requirements(self):
        id_part, data = self.match_id()
        if self.nation and self.nation in data.get("nations", {}):
            data = data["nations"][self.nation]

        if data.get("dates"):
            data = self.match_dates(data["dates"])

        default = data.get("default", "")
        if default == "":
            required_keys = data.keys()
            raise ValueError(f"{id_part} requires {' or '.join(required_keys)}")

        return data["default"]
