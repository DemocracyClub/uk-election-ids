import os

from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def _get_description():
    try:
        path = os.path.join(os.path.dirname(__file__), "README.md")
        with open(path, encoding="utf-8") as f:
            return f.read()
    except IOError:
        return ""


setup(
    name="uk_election_ids",
    version="0.9.2",
    author="chris48s",
    license="MIT",
    url="https://github.com/DemocracyClub/uk-election-ids/",
    packages=["uk_election_ids"],
    package_data={"uk_election_ids": ["data/*.json"]},
    description="Create Democracy Club Election Identifiers",
    long_description=_get_description(),
    long_description_content_type="text/markdown",
    extras_require={
        "testing": ["coveralls"],
        "docs": [
            "sphinx==7.1.2",
            "sphinx_rtd_theme==2.0.0",
            "ghp-import==2.1.0",
        ],
        "development": [
            "pydantic==1.10.18",
            "pre-commit==3.5.0",
            "ruff==0.3.7",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    project_urls={
        "Documentation": "https://democracyclub.github.io/uk-election-ids/",
        "Source": "https://github.com/DemocracyClub/uk-election-ids/",
    },
)
