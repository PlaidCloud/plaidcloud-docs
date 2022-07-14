---
title: Import Fixed Width
slug: import-fixed-width
description: Import Fixed Width files
date: 2022-01-25T07:39:55
---


## Description


Imports fixed-width files.



## Examples


No examples yet…

---

## Unique Configuration Items

### Inspect Selected Source File

By pressing the *Guess Settings from Source File* button, PlaidCloud will open the file and inspect it to attempt to determine the data format.  Always check
the guessed settings to make sure they seem correct.

{{< note >}}
If a directory of files is selected for import or search is used, the first file found will be used for guessing
{{< /note >}}

#### Header Type

Since CSVs may or may not contain headers, PlaidCloud provides a way to either use the headers, ignore headers, or use column order to determine the column alignment.
* **No Header**: The CSV file contains no header.  Use the source list in the *Data Mapper* to determine the column alignment
* **Has Header - Use Header and Override Field List**: The CSV file has a header.  Use the header names specified and ignore the source list in the *Data Mapper*.
* **Has Header - Skip Header and Use Field List Instead**: The CSV file has a header but it should be ignored.  Use the header names specified by the source list in the *Data Mapper*.

### Row Selection

For input files with extraneous records, you can specify a number of rows to skip before processing the data.  This is useful if files contain header blocks that must be skipped before arriving at the tabular data.

### Column Widths

Enter the widths of the columns seperated with commas or spaces.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-file-selection" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
