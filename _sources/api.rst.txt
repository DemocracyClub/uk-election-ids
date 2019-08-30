API Reference
=============

IdBuilder
---------

.. automodule:: uk_election_ids.election_ids
  :members: IdBuilder

Usage Examples
~~~~~~~~~~~~~~

.. code:: python

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

validate
--------

.. automodule:: uk_election_ids.election_ids
  :members: validate

Usage Examples
~~~~~~~~~~~~~~

.. code:: python

    >>> from uk_election_ids.election_ids import validate

    >>> validate('local.2018-05-03')
    True

    >>> validate('foo.bar')
    False
