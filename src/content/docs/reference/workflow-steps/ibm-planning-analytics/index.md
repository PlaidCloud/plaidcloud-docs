---
title: IBM TM1 / Planning Analytics Steps
description: Workflow steps that read from an IBM TM1 / Planning Analytics server over your TM1 connection — cube data by saved view or MDX, and dimension hierarchies — cloud-direct or through an on-premises PlaidLink agent.
---

Workflow steps that read from IBM **TM1 / Planning Analytics** over your [TM1 connection](/guides/connections/tm1/): cube data by saved view or MDX with an optional point-of-view slice, and dimension hierarchies loaded into a PlaidCloud dimension. Reach TM1 cloud-direct, or, for a server only reachable from inside your own network, through an on-premises PlaidLink agent.

## Steps

- [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — read a cube by saved view or MDX, with a point-of-view slice and a pre-save preview. Cloud-direct.
- [TM1 Query (Agent)](/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — the on-prem twin of TM1 Query, dispatched through an installed PlaidLink agent.
- [TM1 Dimension Read](/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — load a TM1 hierarchy into a PlaidCloud dimension. Cloud-direct.

## Related

- [Connect to TM1 (guide)](/guides/connections/tm1/)
- [TM1 Connector](/reference/connectors/rest/tm1/)
