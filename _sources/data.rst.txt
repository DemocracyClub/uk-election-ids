Data Sources
============

Election Types and Subtypes
---------------------------

Valid Election types and subtypes are defined in the `reference
definition <https://elections.democracyclub.org.uk/reference_definition>`__.

Organisation Names
------------------

For compatibility, organisation segments must use official names.
Organisation names can be sourced from `gov.uk
registers <https://www.registers.service.gov.uk/>`__. Short form
versions of names should be used i.e: add an organisation segment with
``myid.with_organisation('Birmingham')`` not
``myid.with_organisation('Birmingham City Council')``

-  `Local authorities in
   England <https://www.registers.service.gov.uk/registers/local-authority-eng/download>`__:
   use the 'name' column/key
-  `Principal local authorities in
   Wales <https://www.registers.service.gov.uk/registers/principal-local-authority/download>`__:
   use the 'name' column/key
-  `Local authorities in
   Scotland <https://www.registers.service.gov.uk/registers/local-authority-sct/download>`__:
   use the 'name' column/key
-  `Local authorities in Northern
   Ireland <https://www.registers.service.gov.uk/registers/local-authority-nir/download>`__

Alternatively organisation names can be sourced from the `Every Election
API <https://elections.democracyclub.org.uk/api/organisations/>`__. Use
the ``common_name`` key.

Division Names
--------------

For compatibility, division segments must use official names. For
boundaries that are already in use, names of parliamentary
constituencies, district wards and county electoral divisions should be
sourced from `OS Boundary
Line <https://www.ordnancesurvey.co.uk/business-and-government/products/boundary-line.html>`__.
New boundaries must be extracted from legislation. We also maintain a
`parser <https://github.com/DemocracyClub/eco-parser>`__ which can help
with extracting this data from Electoral Change Orders.
