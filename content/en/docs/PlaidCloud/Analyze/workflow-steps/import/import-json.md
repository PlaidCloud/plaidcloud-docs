---
title: Import JSON
slug: import-json
weight: 10.0
description: Import JSON text files from PlaidCloud Document
date: 2022-01-25T07:39:57
---


## Description

Import JSON text files from PlaidCloud Document.

For more details on JSON files, see the JSON official website here: <http://json.org/>.

JSON files do *not* retain column order. The column order in the source file does not necessarily reflect the column order in the imported data table.


## Examples

No examples yet...

---

## Unique Configuration Items

### JSON Data Orientation

Consider the following data set:

| ID | Name | Gender | State |
| 1 | Jack | M | MO |
| 2 | Jill | F | MO |
| 3 | George | M | VA |
| 4 | Abe | M | KY |

JSON files can be imported from one of three data formats:

* Records: Data is stored in Python dictionary sets, with each row stored in {Column -> Value, …} format. For example:


```json
[{ "ID": 1, "Name": "Jack", "Gender": "M", "State": "MO" }, { "ID": 2, "Name": "Jill", "Gender": "F", "State": "MO" }, { "ID": 3, "Name": "George", "Gender": "M", "State": "VA" }, { "ID": 4, "Name": "Abe", "Gender": "M", "State": "KY" }]
```

* Index: Data is stored in nested Python dictionary sets, with each row stored in {Index -> {Column -> Value, …},…} format. For example:


```json
{ "0": { "ID": 1, "Name": "Jack", "Gender": "M", "State": "MO" }, "1": { "ID": 2, "Name": "Jill", "Gender": "F", "State": "MO" }, "2": { "ID": 3, "Name": "George", "Gender": "M", "State": "VA" }, "3": { "ID": 4, "Name": "Abe", "Gender": "M", "State": "KY" } }
```

* Split: Data is stored in a single Python dictionary set, values stored in lists. For example:


```json
{ "columns": ["ID", "Name", "Gender", "State"], "index": [0, 1, 2, 3], "data": [ [1, "Jack", "M", "MO"], [2, "Jill", "F", "MO"], [3, "George", "M", "VA"], [4, "Abe", "M", "KY"] ] }
```

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-file-selection" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
