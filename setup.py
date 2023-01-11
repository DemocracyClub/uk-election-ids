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
    version="0.5.1",
    author="chris48s",
    license="MIT",
    url="https://github.com/DemocracyClub/uk-election-ids/",
    packages=["uk_election_ids"],
    description="Create Democracy Club Election Identifiers",
    long_description=_get_description(),
    long_description_content_type="text/markdown",
    extras_require={
        "testing": ["coveralls"],
        "development": ["sphinx", "sphinx_rtd_theme", "ghp-import"],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    project_urls={
        "Documentation": "https://democracyclub.github.io/uk-election-ids/",
        "Source": "https://github.com/DemocracyClub/uk-election-ids/",
    },
)
