---
title: Import Sage Intacct Query
slug: import-intacct-query
weight: 24.0
description: Run a generic Sage Intacct query against any object type and import the results into PlaidCloud, with paging, filtering, and column selection.
date: 2026-04-28T00:00:00
---


## Description

Run an ad-hoc query against any Sage Intacct object type and import the results. Unlike the dedicated [Sage AP](../import-sage-ap/) and [Sage AP Lines](../import-sage-ap-lines/) steps, this step lets you target any Intacct object — General Ledger, projects, customers, vendors, custom objects, etc. — and pick the fields you need.

Paging is automatic, so the step works for result sets larger than a single Intacct API page.


## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

* **Connection** — the Sage Intacct REST connection to read from.
* **Object** — the Intacct object name to query (e.g. `GLACCOUNT`, `CUSTOMER`, `PROJECT`).
* **Fields** — the list of fields to return. Use `Select All` to include every available field, or `Select None` to start from a clean slate. The GL account number is included by default for GL queries.
* **Filter** — optional predicate applied server-side, in Intacct query syntax.
* **Page Size** — number of records to fetch per page. Defaults to a value that balances throughput with API rate limits.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
