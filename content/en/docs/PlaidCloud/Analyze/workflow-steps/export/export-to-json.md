---
title: Export to JSON
slug: export-to-json
weight: 7.0
description: Export an Analyze data table to PlaidCloud Document as a JSON file
date: 2022-01-25T07:39:58
---


## Description


Export an Analyze data table to PlaidCloud Document as a JSON file. There are several options (shown below) for data orientation.



For more details on JSON files, see the JSON official website here: <http://json.org/>.


{{< note >}}
JSON files do *not* retain column order. The column order in the source data table does not necessarily reflect the column order in the exported file.
{{< /note >}}




## Export Parameters

{{< include "common-export-file-selection">}}



### JSON Orientation


Consider the following data set:




| ID |  Name  | Gender | State |
|----|--------|--------|-------|
| 1  | Jack   |   M    |   MO  |
| 2  | Jill   |   F    |   MO  |
| 3  | George |   M    |   VA  |
| 4  | Abe    |   M    |   KY  |

JSON files can be exported into one of four data formats:


* Records: Data is stored in Python dictionary sets, with each row stored in {Column -> Value, …} format. For example: **[{“ID”:1,”Name”:”Jack”,”Gender”:”M”,”State”:”MO”},{“ID”:2,”Name”:”Jill”,”Gender”:”F”,”State”:”MO”},{“ID”:3,”Name”:”George”,”Gender”:”M”,”State”:”VA”},{“ID”:4,”Name”:”Abe”,”Gender”:”M”,”State”:”KY”}]**
* Index: Data is stored in nested Python dictionary sets, with each row stored in {Index -> {Column -> Value, …},…} format. For example: **{“0”:{“ID”:1,”Name”:”Jack”,”Gender”:”M”,”State”:”MO”},”1”:{“ID”:2,”Name”:”Jill”,”Gender”:”F”,”State”:”MO”},”2”:{“ID”:3,”Name”:”George”,”Gender”:”M”,”State”:”VA”},”3”:{“ID”:4,”Name”:”Abe”,”Gender”:”M”,”State”:”KY”}}**
* Split: Data is stored in a single Python dictionary set, values are stored in lists. For example: **{“columns”:[“ID”,”Name”,”Gender”,”State”],”index”:[0,1,2,3],”data”:[[1,”Jack”,”M”,”MO”],[2,”Jill”,”F”,”MO”],[3,”George”,”M”,”VA”],[4,”Abe”,”M”,”KY”]]}**
* Values: Data is stored in multiple Python lists. For example: **[[1,”Jack”,”M”,”MO”],[2,”Jill”,”F”,”MO”],[3,”George”,”M”,”VA”],[4,”Abe”,”M”,”KY”]]**


### Date Handling


Specify **Date Format** using the dropdown menu. Choose from the following formats:


* **Epoch (Unix Timestamp – Seconds since 1/1/1970)**
* **ISO 8601 Format (YYYY-MM-DD HH:MM:SS with timeproject offset)**

Specify **Date Unit** using the dropdown menu. Choose from the following formats, listed in order of increasing precision:


* **Seconds (s)**
* **Milliseconds (ms)**
* **Microseconds (us)**
* **Nanoseconds (ns)**

### Force ASCII


Select this checkbox to ensure that all strings are encoded in proper ASCII format. This is enabled by default.



### Output File Type


All exported files are uncompressed, but the following compression options are available:


* Zip
* GZip
* BZip2


## Table Data Selection

{{< include "common-data-mapper" >}}




For more aggregation details, see the Analyze overview page [here](/docs/workflow-steps/common/aggregation).


## Data Filters

{{< include "common-data-filter" >}}

## Examples


No examples yet...
