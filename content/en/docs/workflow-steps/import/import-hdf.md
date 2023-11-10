---
title: Import HDF
slug: import-hdf
weight: 8.0
description: Import HDF5 files from PlaidCloud Document
date: 2022-01-25T07:39:58
---


## Description

Import HDF5 files from PlaidCloud Document.

For more details on HDF5 files, see the HDF Group’s official website here: <http://www.hdfgroup.org/HDF5/>.


## Examples

No examples yet...

---

## Unique Configuration Items


### Key Name

HDF files store data in a path structure. A key (path) is needed as the destination for the table within the HDF file. In most situations, this will be *table*.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-file-selection" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
