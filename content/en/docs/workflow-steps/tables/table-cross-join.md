---
title: Table Cross Join
slug: table-cross-join
description: Use this function to perform an cross join between two data tables
date: 2022-05-10T14:00:00
---


## Description


Use, as you might have expected, to perform a cross join operation on 2 data tables, combining them into a single data table without join key(s).


For more details on cross join methodology, see here: [Wikipedia SQL Cross Join](https://en.wikipedia.org/wiki/Join_%28SQL%29#Cross_join)



## Table 1 Data Selection


### Table Source


Specify the source data table by selecting it from the dropdown menu.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.

### Source Columns and Replacements


Specify any columns to be included in the Inner Join here. Selecting the **Inspect Source** and **Populate Source Mapping Table** buttons will make these columns available for the join operation.

![Source Table Cross Join Selection](/images/table_cross_join_1.png)

## Table 2 Data Selection


### Table Source


Specify the source data table by selecting it from the dropdown menu.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions)


for more details and examples.

### Source Columns and Replacements


Specify any columns to be included in the Inner Join here. Selecting the **Inspect Source** and **Populate Source Mapping Table** buttons will make these columns available for the join operation.



## Table Output


{{< include "common-target-table-creation.md" >}}



### Target Output Columns


Specify the columns to appear in the target data table. Selecting the **Propagate** button will insert all columns listed in the **Source Columns and Replacements** section of both **Table 1** and **Table 2**. Any columns included in the **Join Map** will only be listed a single time.



To add additional columns manually, right click anywhere in the section and select either **Insert Row** or **Append Row**, to add a row prior to the currently selected row or to add a row at the end, respectively. Then, type the column name. To remove a field, simply right-click and select **Delete**.

![Target Table Cross Join Selection](/images/table_cross_join_output.png)

### Select Subset of Data Based On Aggregations


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.



### Final Data Table Slicing (Limit)


To limit the data, simply check the **Apply Row Slicer** box and then specify the following:


* **Initial Rows to Skip:** Rows of data to skip (column header row is not included in count)
* **End at Row:** Last row of data to include. This is different from simply counting rows at the end to drop


