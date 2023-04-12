import json
from pathlib import Path

ELECTION_TYPES = {
    "parl": {
        "name": "UK Parliament elections",
        "subtypes": [],
        "can_have_orgs": False,
        "can_have_divs": True,
    },
    "nia": {
        "name": "Northern Ireland Assembly elections",
        "subtypes": [],
        "can_have_orgs": False,
        "can_have_divs": True,
    },
    "europarl": {
        "name": "European Parliament (UK) elections",
        "subtypes": [],
        "can_have_orgs": False,
        "can_have_divs": True,
    },
    "naw": {
        "name": "National Assembly for Wales elections",
        "subtypes": [
            {"name": "Constituencies", "election_subtype": "c"},
            {"name": "Regions", "election_subtype": "r"},
        ],
        "can_have_orgs": False,
        "can_have_divs": True,
    },
    "senedd": {
        "name": "Senedd Cymru elections",
        "subtypes": [
            {"name": "Constituencies", "election_subtype": "c"},
            {"name": "Regions", "election_subtype": "r"},
        ],
        "can_have_orgs": False,
        "can_have_divs": True,
    },
    "sp": {
        "name": "Scottish Parliament elections",
        "subtypes": [
            {"name": "Constituencies", "election_subtype": "c"},
            {"name": "Regions", "election_subtype": "r"},
        ],
        "can_have_orgs": False,
        "can_have_divs": True,
    },
    "gla": {
        "name": "Greater London Assembly elections",
        "subtypes": [
            {
                "name": "Constituencies",
                "election_subtype": "c",
                "can_have_divs": True,
            },
            {
                "name": "Additional",
                "election_subtype": "a",
                "can_have_divs": False,
            },
        ],
        "can_have_orgs": False,
    },
    "local": {
        "name": "Local elections",
        "subtypes": [],
        "can_have_orgs": True,
        "can_have_divs": True,
    },
    "pcc": {
        "name": "Police and Crime Commissioner elections",
        "subtypes": [],
        "can_have_orgs": True,
        "can_have_divs": False,
    },
    "mayor": {
        "name": "Mayoral elections",
        "subtypes": [],
        "can_have_orgs": True,
        "can_have_divs": False,
    },
    "ref": {
        "name": "Referendum elections",
        "subtypes": [],
        "can_have_orgs": True,
        "can_have_divs": False,
    },
}

voting_system_data = Path(__file__).parent / "data/voting_systems.json"
VOTING_SYSTEMS = json.load(voting_system_data.open())["voting_systems"]
id_requirements_data = Path(__file__).parent / "data/id_requirements.json"
ID_REQUIREMENTS = json.load(id_requirements_data.open())["id_type"]
