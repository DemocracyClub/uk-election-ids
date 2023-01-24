import datetime
import json
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
        for id_part in ids_with_defaults:
            if self.election_id.startswith(id_part):
                return (id_part, self.DATA["defaults"][id_part])

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

            if self.date >= start:
                if self.date < end:
                    return value
        raise ValueError("No date for range")


class VotingSystemMatcher(MetaDataMatcher):
    path = Path(__file__).parent / "data" / "voting_systems.json"
    DATA = json.load(path.open())

    def get_voting_system(self):
        id_part, data = self.match_id()
        if self.nation:
            if self.nation in data.get("nations", {}):
                data = data["nations"][self.nation]

        if data.get("dates"):
            data = self.match_dates(data["dates"])

        default = data.get("default", None)
        if not default:
            required_keys = data.keys()
            raise ValueError(f"{id_part} requires {' or '.join(required_keys)}")

        return data["default"]
