---
title: Import Fixed Width
slug: import-fixed-width
weight: 5.0
description: Import Fixed Width files
date: 2022-01-25T07:39:55
---


## Description


Imports fixed-width files.



## Examples


No examples yet…

---

## Import Parameters

{{< include "common-import-file-source-target-selection.md" >}}

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

### Header

Since Excel files may or may not contain headers, PlaidCloud provides a way to either use the headers, ignore headers, or use column order to determine the column alignment.
* **No Header**: The file contains no header.  Use the source list in the *Data Mapper* to determine the column alignment
* **Has Header - Use Header and Override Field List**: The file has a header.  Use the header names specified and ignore the source list in the *Data Mapper*.
* **Has Header - Skip Header and Use Field List Instead**: The file has a header but it should be ignored.  Use the header names specified by the source list in the *Data Mapper*.

### Row Selection

For input files with extraneous records, you can specify a number of rows to skip before processing the data.  This is useful if files contain header blocks that must be skipped before arriving at the tabular data.

### Column Widths

Enter the widths of the columns seperated with commas or spaces.

## Table Data Selection

{{< include "common-data-mapper" >}}

## Data Filters

{{< include "common-data-filter" >}}

