---
title: Table Union Distinct
slug: table-union-distinct
description: Consolidate data tables
date: 2022-01-25T07:39:49
---


## Description


Use to combine multiple data tables with the same column structure into a single data table. For example, time series data is a prime candidate for this transform. The result is always the distinct set of records after combining the data.

{{< note >}}
**Union** removes duplicates. If you want to keep all records, use **Union All** instead.
{{< /note >}}


![Table Union All](/images/table_union_all.png)
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


To set **Source Table**, select the original data table from the dropdown list. Selecting a data table will automatically populate whether it is a *Project* or a *Workflow* table. Additionally, there is an option to preview the data table.



### Source Columns and Target Columns


Displays the columns in the source table (**Source Columns**) alongside the column to be used in the resulting new table (**target columns**).



### Data Filters Tab

{{< note >}}
Remember to configure **Data Filters** conditions for each data table listed in **Sources**.
{{< /note >}}




### Data Filters


To allow for maximum flexibility, data filters are available on the source data and the target data. For larger data sets, it can be especially beneficial to filter out rows on the source, so the remaining operations are performed on a smaller data set.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions)
for more details and examples.




### Apply Secondary Filter To Result Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples


### Final Data Table Slicing (Limit)


To limit the data, check the **Apply Row Slicer** box and then specify the following:


* **Initial Rows to Skip:** Rows of data to skip (column header row is **not** included in count)
* **End at Row:** Last row of data to include. Note that this is different from simply counting rows at the end to drop



