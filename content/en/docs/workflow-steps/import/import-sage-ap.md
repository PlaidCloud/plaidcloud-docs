---
title: Import Sage AP
slug: import-sage-ap
weight: 21.0
description: Import Sage Intacct Accounts Payable bill headers into PlaidCloud as a workflow step using a configured Sage Intacct REST connection.
date: 2026-04-28T00:00:00
---


## Description

Import Accounts Payable bill headers from Sage Intacct via the Sage Intacct REST API. Each row is one AP bill, with the vendor, GL date, due date, totals, and status fields needed for downstream reporting.

Use a configured [Sage Intacct REST Connector](../../../connectors/rest-connections/sage-intacct-connector/) as the source. To pull line-level detail at the same grain as the bill lines, pair this step with [Import Sage AP Lines](../import-sage-ap-lines/).


## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

* **Connection** — the Sage Intacct REST connection to read from.
* **Date Range** — restrict the import to bills whose GL date falls in the selected window. Leave blank to pull all available history.
* **Entity Filter** — limit the import to a specific Intacct entity. Useful in multi-entity tenants.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
