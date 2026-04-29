---
title: Import Sage AP
slug: import-sage-ap
weight: 21.0
description: Import Sage Intacct Accounts Payable bill headers into PlaidCloud as a workflow step using a configured Sage Intacct REST connection.
date: 2026-04-28T00:00:00
---


## Description

Import Accounts Payable bill headers from Sage Intacct via the Sage Intacct REST API. Each row is one AP bill, with the vendor, GL date, due date, totals, and status fields needed for downstream reporting.

Use a configured [Sage Intacct REST Connector](../../../connectors/rest-connections/sage-intacct-connector/) as the source. To pull line-level detail at the same time, pair this step with [Import Sage AP Lines](../import-sage-ap-lines/).


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
