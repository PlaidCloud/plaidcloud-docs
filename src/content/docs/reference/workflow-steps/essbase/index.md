---
title: Oracle Essbase Steps
description: Workflow steps that read from an Oracle Essbase cube over your Essbase connection — live MDX queries and dimension outlines loaded into a PlaidCloud dimension — cloud-direct.
---

Workflow steps that read from Oracle **Essbase** over your [Oracle Essbase connection](/guides/connections/essbase/): cube data by live MDX query, and a dimension outline loaded into a PlaidCloud dimension. Essbase is reached **cloud-direct** over its REST API — there is no on-premises agent path for these steps.

## Steps

- [Essbase: Query Cube](/reference/workflow-steps/essbase/essbase-query/) — run a live MDX query against a cube and land the result grid as a table. Cloud-direct.
- [Essbase: Read Dimension](/reference/workflow-steps/essbase/essbase-dimension-read/) — load an Essbase dimension outline into a PlaidCloud dimension. Cloud-direct.

## Related

- [Connect to Oracle Essbase (guide)](/guides/connections/essbase/)
- [Oracle Essbase Connector](/reference/connectors/erp/oracle-essbase/)
