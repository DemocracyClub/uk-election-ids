# UK Election IDs

[![Build Status](https://travis-ci.org/DemocracyClub/uk-election-ids.svg?branch=master)](https://travis-ci.org/DemocracyClub/uk-election-ids)
[![Coverage Status](https://coveralls.io/repos/github/DemocracyClub/uk-election-ids/badge.svg?branch=master)](https://coveralls.io/github/DemocracyClub/uk-election-ids?branch=master)
![PyPI Version](https://img.shields.io/pypi/v/uk-election-ids.svg)
![License](https://img.shields.io/pypi/l/uk-election-ids.svg)
![Python Support](https://img.shields.io/pypi/pyversions/uk-election-ids.svg)

Create Democracy Club Election Identifiers.

Democracy Club defines a specification for creating reproducible unique identifiers for elections in the UK. See our [reference definition](https://elections.democracyclub.org.uk/reference_definition). If you are interested in independently producing identifiers which are compatible with those produced by our [Every Election](https://elections.democracyclub.org.uk/) platform, this python package includes a builder object, slugging logic and validation rules for creating identifiers that conform to the spec.

## Installation

```bash
pip install uk-election-ids
```

## Usage Examples

```python
>>> from uk_election_ids.election_ids import IdBuilder
>>> from datetime import date


# Chain method calls to build up an ID object
>>> myid = IdBuilder('local', date(2018, 5, 3))\
...     .with_organisation('Test Org')\
...     .with_division('Test Division')
# IdBuilder will deal with slugging strings for us
>>> myid.ballot_id
'local.test-org.test-division.2018-05-03'
>>> myid.ids
[
    'local.2018-05-03',
    'local.test-org.2018-05-03',
    'local.test-org.test-division.2018-05-03'
]


# IdBuilder only allows values defined in the Reference Definition
>>> myid = IdBuilder('gla', date(2018, 5, 3)).with_subtype('x')
ValueError: Allowed values for subtype are ('c', 'a')


# Group IDs can be created with partial information
>>> myid = IdBuilder('local', date(2018, 5, 3)).with_organisation('Test Org')
>>> myid.election_group_id
'local.2018-05-03'
>>> myid.organisation_group_id
'local.test-org.2018-05-03'
>>> myid.ballot_id
ValueError: election_type local must have a division in order to create a ballot id


# A Group ID object can be used to create multiple ballot IDs
>>> divisions = ["area1", "area2", "area3"]
>>> org_id = IdBuilder('local', date(2018, 5, 3)).with_organisation('Test Org')
>>> [org_id.with_division(d).ballot_id for d in divisions]
[
    'local.test-org.area1.2018-05-03',
    'local.test-org.area2.2018-05-03',
    'local.test-org.area3.2018-05-03'
]
```

## API Documentation

See the full [API Reference](https://democracyclub.github.io/uk-election-ids/)

## Data Sources

### Election Types and Subtypes

Valid Election types and subtypes are defined in the [reference definition](https://elections.democracyclub.org.uk/reference_definition).


### Organisation Names

For compatibility, organisation segments must use official names. Organisation names can be sourced from [gov.uk registers](https://www.registers.service.gov.uk/). Short form versions of names should be used i.e: add an organisation segment with `myid.with_organisation('Birmingham')` not `myid.with_organisation('Birmingham City Council')`

* [Local authorities in England](https://www.registers.service.gov.uk/registers/local-authority-eng/download): use the 'name' column/key
* [Principal local authorities in Wales](https://www.registers.service.gov.uk/registers/principal-local-authority/download): use the 'name' column/key
* [Local authorities in Scotland](https://www.registers.service.gov.uk/registers/local-authority-sct/download): use the 'name' column/key
* [Local authorities in Northern Ireland](https://www.registers.service.gov.uk/registers/local-authority-nir/download)

Alternatively organisation names can be sourced from the [Every Election API](https://elections.democracyclub.org.uk/api/organisations/). Use the `common_name` key.

### Division Names

For compatibility, division segments must use official names. For boundaries that are already in use, names of parliamentary constituencies, district wards and county electoral divisions should be sourced from [OS Boundary Line](https://www.ordnancesurvey.co.uk/business-and-government/products/boundary-line.html). New boundaries must be extracted from legislation. We also maintain a [parser](https://github.com/DemocracyClub/eco-parser) which can help with extracting this data from Electoral Change Orders.

## Support

To report a bug, [raise an issue](https://github.com/DemocracyClub/uk-election-ids/issues). If you are using election identifiers, [join our slack](https://slack.democracyclub.org.uk/) to ask questions or tell us about your project.

## Development

Run the tests locally:

```bash
./run_tests.py
```

Build package locally:

```bash
./build.sh
```

Build the API docs:

```bash
cd docs && make clean html
```
