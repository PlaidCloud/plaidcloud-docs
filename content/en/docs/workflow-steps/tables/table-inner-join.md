---
title: Table Inner Join
slug: table-inner-join
description: Use this function to perform an inner join between two data tables
date: 2022-01-25T07:39:49
---


## Description


Use, as you might have expected, to perform an inner join operation on 2 data tables, combining them into a single data table based upon the specified join key(s).


For more details on inner join methodology, see here: [Wikipedia SQL Inner Join](http://en.wikipedia.org/wiki/Join_%28SQL%29#Inner_join)



## Table 1 Data Selection

![Table Inner Join 1](/images/table_inner_join_1.png)

### Table Source


Specify the source data table by selecting it from the dropdown menu.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.




### Source Columns and Replacements


Specify any columns to be included in the Inner Join here. Selecting the **Inspect Source** and **Populate Source Mapping Table** buttons will make these columns available for the join operation.



## Table 2 Data Selection


### Table Source


Specify the source data table by selecting it from the dropdown menu.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions)


for more details and examples.


### Source Columns and Replacements


Specify any columns to be included in the Inner Join here. Selecting the **Inspect Source** and **Populate Source Mapping Table** buttons will make these columns available for the join operation.


## Table Output

![Table Anti Join 2](/images/table_anti_join_2.png)
### Target Table

{{< include "common-target-table-creation.md" >}}




### Join Map


Specify join conditions. Using the **Guess** button will find all matching columns from both **Table 1** as well as **Table 2**. To add additional columns manually, right click anywhere in the section and select either **Insert Row** or **Append Row**, to add a row prior to the currently selected row or to add a row at the end, respectively. Then, type the column names to match from **Table 1** to **Table 2**. To remove a field from the **Join Map**, simply right-click and select **Delete**.



### Target Output Columns


Specify the columns to appear in the target data table. Selecting the **Propagate** button will insert all columns listed in the **Source Columns and Replacements** section of both **Table 1** and **Table 2**. Any columns included in the **Join Map** will only be listed a single time.



To add additional columns manually, right click anywhere in the section and select either **Insert Row** or **Append Row**, to add a row prior to the currently selected row or to add a row at the end, respectively. Then, type the column name. To remove a field, simply right-click and select **Delete**.



## Select Subset Of Data Based On Aggregations


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.



### Final Data Table Slicing (Limit)


To limit the data, simply check the **Apply Row Slicer** box and then specify the following:


* **Initial Rows to Skip:** Rows of data to skip (column header row is not included in count)
* **End at Row:** Last row of data to include. This is different from simply counting rows at the end to drop








## Examples


### Join Automobile Manufacturers with Models


In this example, consider the following source data tables. First is a list of automobile manufacturers.



| Mfg_ID | Manufacturer |
| 1 | Aston Martin |
| 2 | Porsche |
| 3 | Lamborghini |
| 4 | Ferrari |
| 5 | Koenigsegg |

Next is a list of automobile models with a manufacturer ID. Note that there are several models with no manufacturer.




| ModelName | Mfg_ID |
| Aventador | 3 |
| Countach | 3 |
| DBS | 1 |
| Enzo | 4 |
| One-77 | 1 |
| Optimus Prime |  |
| Batmobile |  |
| Agera | 5 |
| Lightning McQueen |  |

To get a list of models by manufacturer, it makes sense to join on *Mfg_ID*.


First, specify parameters for **Table 1 Data Selection**. The source data table is selected and all columns are listed.



Next, specify parameters for **Table 2 Data Selection**. Once again, the source data table is selected and all columns are listed.



Finally, the join conditions are set in the **Table Output** tab. Using the **Guess** button, Analyze properly identifies the *Mfg_ID* column to use as the **Join Key**. Lastly, the 


**Target Output Columns** are specified automatically using the **Propagate** button. This effectively includes all columns from all tables, with all join columns included only a single time. Note that the columns are sorted alphabetically, first by *Manufacturer* and next by *ModelName*.



As expected, the final output only includes values which had a match in both tables. As such, *Porsche* does not show up because it had no models. Likewise, the 


*Batmobile* had no manufacturer (it was a custom job), so it’s not included.
