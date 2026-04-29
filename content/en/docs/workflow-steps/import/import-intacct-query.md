---
title: Import Sage Intacct Query
slug: import-intacct-query
weight: 24.0
description: Run a generic Sage Intacct query against any object type and import the results into PlaidCloud, with field discovery, server-side filters, and automatic paging.
date: 2026-04-28T00:00:00
---


## Description

Run an ad-hoc query against any Sage Intacct object type and import the results. Unlike the dedicated [Sage AP](../import-sage-ap/) and [Sage AP Lines](../import-sage-ap-lines/) steps, this step lets you target any Intacct object — General Ledger, projects, customers, vendors, custom objects, etc. — and pick the fields and filters you need.

Paging is handled automatically, so the step works for result sets larger than a single Intacct API page.


## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

* **Sage Connection** — the Sage Intacct REST connection to read from. Sage connections are managed in **Tools > Connections**.
* **Company ID** — the Intacct company to query.
* **Entity ID(s) (comma-separated)** — restrict the query to one or more Intacct entities. Leave blank for every entity.
* **Object Name** — the Intacct object to query, e.g. `GLACCOUNT`, `CUSTOMER`, `PROJECT`, or any custom object name.
* **Fields to import** — table of Intacct field names with an Enabled checkbox. Click `Lookup Object Fields` to populate the list from the Intacct schema, then use `Select All` or `Select None` to bulk-toggle.
* **Filters** — table of filter rows. Each row is `Field`, `Filter Type`, `Value`. Filter types include `Equal To`, `Not Equal To`, `Less Than`, `Less Than or Equal To`, `Greater Than`, `Greater Than or Equal To`, `Is Null`, and `Is Not Null`. Filters apply server-side, before paging.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
