---
title: Import Sage AP Lines
slug: import-sage-ap-lines
weight: 22.0
description: Import Sage Intacct Accounts Payable line-level detail into PlaidCloud as a workflow step using a configured Sage Intacct REST connection.
date: 2026-04-28T00:00:00
---


## Description

Import line-level detail for Accounts Payable bills from Sage Intacct via the Sage Intacct REST API. Each row is one bill line, including GL account, dimensions, line amount, and bill key linking back to the parent header.

Pair this step with [Import Sage AP](../import-sage-ap/) to load both grains for downstream allocation, reporting, or reconciliation.


## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

* **Connection** — the Sage Intacct REST connection to read from.
* **Date Range** — restrict the import to lines whose parent bill's GL date falls in the selected window. Leave blank to pull all available history.
* **Entity Filter** — limit the import to a specific Intacct entity.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
