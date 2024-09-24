from pathlib import Path
from typing import Dict, Optional

from pydantic import BaseModel, HttpUrl, root_validator


class VotingSystem(BaseModel):
    name: str
    description: str
    uses_party_lists: bool
    wikipedia_url: HttpUrl


class SingleVotingSystemRule(BaseModel):
    default: Optional[str]
    nations: Optional[dict]
    dates: Optional[dict]


class VotingSystemSchema(BaseModel):
    voting_systems: Dict[str, VotingSystem]
    defaults: Dict[str, SingleVotingSystemRule]

    @root_validator(pre=False)
    def validate(cls, values):
        if isinstance(values, cls):
            values = values.__dict__
        voting_system_slugs = values["voting_systems"].keys()

        def _recurse_defaults(d: dict):
            if (value := d.get("default")) and value not in voting_system_slugs:
                raise ValueError(f"'{value}' is not a valid voting system")
            for k, v in d.items():
                if isinstance(v, dict):
                    _recurse_defaults(v)
                if hasattr(v, "__dict__"):
                    _recurse_defaults(v.__dict__)

        _recurse_defaults(values["defaults"])
        return values


if __name__ == "__main__":
    data = Path(__file__).parent.parent / "uk_election_ids" / "data" /"voting_systems.json"
    schema = VotingSystemSchema.parse_file(data)
    VotingSystemSchema.validate(schema)
