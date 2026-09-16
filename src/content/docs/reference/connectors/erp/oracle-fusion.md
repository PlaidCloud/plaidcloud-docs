---
title: Oracle Fusion Connector
description: Set up an Oracle Fusion Cloud connection in PlaidCloud with OAuth2 credentials to import GL balances and journal batches over OData/BIP, and post journals through FBDI.
sidebar:
  order: 1
---

## API Documentation

Oracle Fusion Cloud's [REST API (OData)](https://docs.oracle.com/en/cloud/saas/financials/) and [BI Publisher (BIP) and File-Based Data Import (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) references document the endpoints and bulk-extract/load path this connector uses.

## How Authentication Works

The connection authenticates with OAuth2 client credentials (or the basic-auth API credentials your Fusion Cloud security setup issues for integration users) against a dedicated API user. The API user's role controls both which General Ledger entities it can read and which FBDI/GL Interface functions it can post through.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Instance URL | Text | Your Fusion Cloud instance URL, e.g. `https://yourorg.fa.us2.oraclecloud.com`. |
| Client ID | Text | The API user's OAuth2 client ID (or username, for basic auth). |
| Client Secret | Text | The API user's OAuth2 client secret (or password, for basic auth). Stored encrypted. |

## Entities Available to Import

Two import steps cover different pull sizes, both against `gl_balances` and `journal_batches`:

- **Import Fusion Entity** — a direct OData/BIP call, for a routine, bounded pull.
- **Import Fusion Bulk Extract** — an asynchronous FBDI/BIP export job, for a large extract.

Both support range filters (`ge`/`le`) on date, accounting-period, and numeric balance/amount fields, plus equality filters on discrete fields like ledger or currency. See [Import Fusion Entity](/reference/workflow-steps/oracle-fusion/import-fusion-entity/) and [Import Fusion Bulk Extract](/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) for the full field reference.

## Posting Journal Entries

The **Oracle Fusion: Post Journal Entry** step posts general ledger journal batches through PlaidCloud's shared ERP write pipeline: write the batch to Oracle's GL_INTERFACE staging table as an FBDI file, submit and poll the Journal Import Launcher ESS job to a terminal state, and confirm before reporting a batch posted. A correction posts a new, debit/credit-swapped reversing entry rather than editing the original. See [Oracle Fusion: Post Journal Entry](/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) for the field reference, and [Connect to Oracle Fusion](/guides/connections/oracle-fusion/) for the full posting walkthrough.

## Known Limitations

| Limitation | What it means |
|---|---|
| ESS job latency | The Journal Import Launcher runs as a scheduled job, not a synchronous call — a posting run takes materially longer than a direct API write. |
| Bulk extract latency | `import_fusion_bulk_extract` waits on an FBDI/BIP export job — reserve it for pulls too large for `import_fusion_entity`'s direct path. |
## Related

- [Connect to Oracle Fusion (guide)](/guides/connections/oracle-fusion/) — step-by-step: create the connection, test it, import an entity, and post a journal.
- [Import Fusion Entity](/reference/workflow-steps/oracle-fusion/import-fusion-entity/)
- [Import Fusion Bulk Extract](/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)
- [Oracle Fusion: Post Journal Entry](/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
