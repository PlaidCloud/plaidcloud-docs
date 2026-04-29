---
title: Import Sage AP Lines
slug: import-sage-ap-lines
weight: 22.0
description: Import Sage Intacct Accounts Payable line-level detail into PlaidCloud as a workflow step using a configured Sage Intacct REST connection.
date: 2026-04-28T00:00:00
---


## Description

Import line-level detail for Accounts Payable bills from Sage Intacct via the Sage Intacct REST API. Each row is one bill line, including the GL account, dimensions, line amount, and the bill key linking back to the parent header.

Pair this step with [Import Sage AP](../import-sage-ap/) to load both grains for downstream allocation, reporting, or reconciliation.


## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

* **Sage Connection** — the Sage Intacct REST connection to read from. Sage connections are managed in **Tools > Connections**.
* **Company ID** — the Intacct company to query. Required if your sender credentials cover more than one company.
* **Entity ID(s) (comma-separated)** — restrict the import to one or more Intacct entities. Leave blank to pull every entity the user has access to.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
