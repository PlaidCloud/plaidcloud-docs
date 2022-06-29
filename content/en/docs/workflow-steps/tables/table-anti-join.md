---
title: Table Anti Join
slug: table-anti-join
description: This function provides an unmatched set of data between two tables
date: 2022-01-25T07:39:50
---


## Description


Table Anti Join provides the unmatched set of items between two tables. This will return the list of items in the first table without matches in the second table. This can be quite useful for determining which records are present in one table but not another.



This operation could be accomplished by using outer joins and filtering on null values for the join; however, the Anti Join transform will perform this in a more efficient and obvious way.



## Table 1 Data Selection

![Table Anti Join 1](/images/table_anti_join_1.png)

### Table Source


Specify the source data table by selecting it from the dropdown menu.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.




### Source Columns and Replacements


Specify any columns to be included in the Anti Join here. Selecting the **Inspect Source** and **Populate Source Mapping Table** buttons will make these columns available for the join operation.



## Table 2 Data Selection


### Table Source


Specify the source data table by selecting it from the dropdown menu.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.





### Source Columns and Replacements


Specify any columns to be included in the Anti Join here. Selecting the **Inspect Source** and **Populate Source Mapping Table** buttons will make these columns available for the join operation.


## Table Output


### Target Table

![Table Anti Join 2](/images/table_anti_join_2.png)


{{< include "common-target-table-creation.md" >}}


### Join Map


Specify join conditions. Using the **Guess** button will find all matching columns from both **Table 1** as well as **Table 2**. To add additional columns manually, right click anywhere in the section and select either **Insert Row** or **Append Row**, to add a row prior to the currently selected row or to add a row at the end, respectively. Then, type the column names to match from **Table A** to **Table B**. To remove a field from the **Join Map**, simply right-click and select **Delete**.



### Target Output Columns


Specify the columns to appear in the target data table. Selecting the **Propagate** button will insert all columns listed in the **Source Columns and Replacements** section of both **Table 1** and **Table 1**. Any columns included in the **Join Map** will only be listed a single time.



To add additional columns manually, right click anywhere in the section and select either **Insert Row** or **Append Row**, to add a row prior to the currently selected row or to add a row at the end, respectively. Then, type the column name. To remove a field, simply right-click and select **Delete**.



### Select Subset Of Data Based On Aggregations


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples






### Final Data Table Slicing (Limit)


To limit the data, simply check the **Apply Row Slicer** box and then specify the following:


* **Initial Rows to Skip:** Rows of data to skip (column header row is not included in count)
* **End at Row:** Last row of data to include. This is different from simply counting rows at the end to drop



