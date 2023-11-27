---
title: Table Union Distinct
slug: table-union-distinct
weight: 17.0
description: Consolidate data tables
date: 2022-01-25T07:39:49
---


## Description


Use to combine multiple data tables with the same column structure into a single data table. For example, time series data is a prime candidate for this transform. The result is always the distinct set of records after combining the data.

{{< note >}}
**Union Distinct** removes duplicates. If you want to keep all records, use **Union All** instead.
{{< /note >}}


## Sources


The **Sources** section serves as a collection of all data tables to append together. Typically, all of the data tables will have the same (or similar) column structure. There are two buttons available to add a data table to the list:


* **Insert Row**
* **Append Row**

Additionally, right-clicking in the **Select Source to Edit** window will display the same options. Right-clicking on a table already added will also display the **Delete** option.


To execute the transform properly, there will need to be one entry in the **Sources** section for every source data table to append together. These entries are listed in the order in which they will be appended. To adjust the order, right-clicking on a table will display the following options:


* **Move Down** (if applicable)
* **Move To Bottom** (if applicable)
* **Move Up** (if applicable)
* **Move To Top** (if applicable)

By default, each source is named *New Table*, but the modeler is encouraged to provide descriptive names by double-clicking the name and renaming accordingly.


{{< note >}}
It is important to remember that the text shown is **not** related to the source data table’s name. We recommend that the modeler provides a name that is descriptive, often the same as the source data table, but keep in mind that there is no tie whatsoever between the names.
{{< /note >}}


## Target Table


By default, the **Target Table** is left blank. Before naming, note that data tables must follow Linux naming conventions. As such, we recommend that names only consist of alphanumeric characters. Analyze will automatically scrub any invalid characters from the name. Additionally, it will limit the length to 256 characters, so be concise!

{{< include "common-target-table-creation.md" >}}



### Table Data Selection Tab

{{< note >}}
Remember to configure **Table Data Selection** conditions for each data table listed in **Sources**.
{{< /note >}}




### Source Table


{{< include "common-table-selection-dynamic.md" >}}



### Source Columns


{{< include "common-data-mapper.md" >}}



### Data Filters

{{< include "common-data-filter.md" >}}

{{< note >}}
Remember to configure **Data Filters** conditions for each data table listed in **Sources**.
{{< /note >}}




