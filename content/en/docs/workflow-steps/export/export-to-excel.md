---
title: Export to Excel
slug: export-to-excel
weight: 2.0
description: Export data as Excel spreadsheet files from a PlaidCloud workflow step with formatting, sheet naming, and layout options.
date: 2022-01-25T07:39:58
---


## Description


Export an Analyze data table to PlaidCloud Document as a Microsoft Excel file. PlaidCloud Analyze supports modern versions of Microsoft Excel (2007-2016) as well as legacy versions (2000/2003).



## Export Parameters

{{< include "common-export-file-selection">}}



#### Target Sheet Name
Specify the target sheet name, the default is ***Sheet1***


#### Selecting File Compression

All exported files are uncompressed, but the following compression options are available:

* No Compression
* Zip
* GZip
* BZip2

#### Write Header To First Row
If this checkbox is selected the table headers will be exported to the first row. If it is not there will be no headers in the exported file.

## Table Data Selection

{{< include "common-data-mapper" >}}






## Data Filters

{{< include "common-data-filter" >}}


## Examples


No examples yet...
