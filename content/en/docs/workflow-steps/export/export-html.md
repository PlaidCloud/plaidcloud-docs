---
title: Export to HTML
slug: export-html
weight: 6.0
description: Export data as HTML files from a PlaidCloud workflow step for web-ready table output and browser-compatible data presentation.
date: 2022-01-25T07:39:58
---


## Description


Export an Analyze data table to PlaidCloud Document as an HTML file. The resultant HTML file will simply contain a table.



## Export Parameters

{{< include "common-export-file-selection">}}
![Export HTML](/images/export_file_html.png)






### Bold Rows


Select this checkbox to make the first row (header row) bold font.



### Escape


This option is enabled by default. When the checkbox is selected, the export process will convert the characters *<*, *>*, and *&* to HTML-safe sequences.



### Double Precision


See details here:



### Output File Type


All exported files are uncompressed, but the following compression options are available:


* Zip
* GZip
* BZip2


## Table Data Selection

{{< include "common-data-mapper" >}}







## Data Filters


{{< include "common-data-filter" >}}

## Examples


No examples yet...
