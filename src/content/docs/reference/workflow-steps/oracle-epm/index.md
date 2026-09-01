---
title: Oracle EPM (HFM / FCCS) Steps
description: Workflow steps that self-serve an ad-hoc data slice from Oracle FCCS over your HFM/FCCS connection — build a point of view, run it, and land the result as a table.
---

Workflow steps that read from Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) over your [HFM/FCCS connection](/guides/connections/hfm-fccs/). A finance user builds a point of view in the step form, runs it, and the returned grid lands automatically as a project table — no ticket to the HFM team, and no consolidation knowledge required.

## Steps

- [HFM/FCCS: Read Data (Ad-hoc)](/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — self-serve a data slice with a point-of-view picker; caches repeat pulls, is row-level-security-ready, and can be promoted to a scheduled recurring load.

## Related

- [Extract from HFM / FCCS (guide)](/guides/connections/hfm-fccs/)
- [HFM / FCCS Connector](/reference/connectors/rest/hfm-fccs/)
