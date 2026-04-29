---
title: Import DB2 Extract
slug: import-db2-extract
weight: 23.0
description: Import a DB2 extract file from PlaidCloud Document storage into a project table as a workflow step.
date: 2026-04-28T00:00:00
---


## Description

Import an IBM DB2 extract file from PlaidCloud Document storage. This is useful when the DB2 server is reachable only from on-premises infrastructure: an external process pushes the extract into PlaidCloud Document storage, and this step reads it from there into a project table.

For live DB2 access (no extract file), connect via the standard [IBM DB2](../../../connectors/database-connections/ibm-db2/) connection and use [Import External Database Tables](../import-external-database-tables/).


## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

None

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-file-selection" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
