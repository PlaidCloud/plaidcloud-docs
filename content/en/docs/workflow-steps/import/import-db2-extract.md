---
title: Import DB2 Extract
slug: import-db2-extract
weight: 23.0
description: Import data from an IBM DB2 extract into PlaidCloud as a workflow step, using either a direct DB2 connection or a previously generated extract file.
date: 2026-04-28T00:00:00
---


## Description

Import data from an IBM DB2 source. Two source modes are supported:

* **Live DB2 connection** — read directly via a configured [IBM DB2](../../../connectors/database-connections/ibm-db2/) connection.
* **Extract file** — read a DB2 extract file from a Document account. Useful when the DB2 server is reachable only from on-premises infrastructure and the extract has been pushed to PlaidCloud Document storage.


## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

* **Source Mode** — `Connection` or `Extract File`.
* **Connection** — required when source mode is `Connection`. Selects the IBM DB2 connection to read from.
* **Schema / Table** — required when source mode is `Connection`. Picks the DB2 object to extract.
* **Extract File** — required when source mode is `Extract File`. Selects the DB2 extract file in Document storage.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-file-selection" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
