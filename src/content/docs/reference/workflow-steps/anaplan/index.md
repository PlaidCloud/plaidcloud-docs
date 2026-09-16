---
title: Anaplan Steps
description: Workflow steps that read from Anaplan over your Anaplan connection — a saved view, a pre-existing export action, or one or more lists loaded into a PlaidCloud dimension — cloud-direct.
---

Workflow steps that read from **Anaplan** over your [Anaplan connection](/guides/connections/anaplan/): a saved view through the large-volume read-request path, a pre-existing export action through the Bulk API, or one or more lists loaded into a PlaidCloud dimension. Anaplan is reached **cloud-direct** over its Integration API — there is no on-premises agent path for these steps, and none of them ever writes back to Anaplan.

## Steps

- [Anaplan: Read View](/reference/workflow-steps/anaplan/anaplan-read-view/) — read a saved view exactly as saved. Cloud-direct.
- [Anaplan: Read Export](/reference/workflow-steps/anaplan/anaplan-read-export/) — run a pre-existing export action and land its file. Cloud-direct.
- [Anaplan: Read List](/reference/workflow-steps/anaplan/anaplan-read-list/) — read one or more lists into a PlaidCloud dimension. Cloud-direct.

## Related

- [Connect to Anaplan (guide)](/guides/connections/anaplan/)
