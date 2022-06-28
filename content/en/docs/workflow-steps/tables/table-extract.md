---
title: Table Extract
slug: table-extract
description: This function helps to extract data from one table and place it in another
date: 2022-01-25T07:39:50
---


## Description


Use to extract data from an existing Analyze data table into another data table. Examples include, but are not limited to, the following:


* Sort
* Group
* Summarization
* Filter/Subset Rows
* Drop Extra Columns
* Math Operations
* String Operations

{{< note >}}
There is no functions exclusive to this transform. All sorting, grouping, filtering, etc. can be performed in any other transform with the **Table Data Selection** and **Data Filters** tabs.
{{< /note >}}


## Extract Parameters

![Extract Parameters](/images/extract_parameters.png)

{{< include "common-table_selection-creation.md" >}}
### Table Data Selection
![Table Data Selection](/images/table_data_selection.png)

The Table Data Selection tab is used to map columns from the source data table to the target data table. All source columns on the left side of the window are automatically mapped to the target data table depicted on the right side of the window. Using the **Inspect Source** menu button, there are a few additional ways to map columns from source to target:


* Populate Both Mapping Tables: Propagates all values from the source data table into the target data table.
* Populate Source Mapping Table Only: Maps all values in the source data table only. This is helpful when modifying an existing workflow when source column structure has changed.
* Populate Target Mapping Table Only: Propagates all values into the target data table only.

In addition to each of these options, each choice offers the ability to preview the source data.



If the source and target column options aren’t enough, other columns can be added into the target data table in several different ways:


* **Propagate All** will insert all source columns into the target data table, whether they already existed or not.
* **Propagate Selected** will insert selected source column(s) only.
* Right click on target side and select **Insert Row** to insert a row immediately above the currently selected row.
* Right click on target side and select **Append Row** to insert a row at the bottom (far right) of the target data table.


{{< warning >}}
Selecting **Propagate All** may effectively create a duplicate of every column. Analyze does not check to see if the columns are already mapped. Make sure duplicate column names do not exist.
{{< /warning >}}




To delete columns from the target data table, select the desired column(s), then right click and select **Delete**.



To rearrange columns in the target data table, select the desired column(s), then right click and select **Move to Top**, **Move Up**, **Move Down**, or **Move to Bottom**.



To return only distinct options, select the **Distinct** menu option. This will toggle a set of checkboxes for each column in the source. Simply check any box next to the corresponding column to return distinct results only.


{{< warning >}}
When the target data table contains only a subset of the source data table, only select the check box next to the columns which **are** to be included in the target data table. Selecting all checkboxes could provide output that does not appear to be distinct.
{{< /warning >}}




To aggregate results, select the **Summarize** menu option. This will toggle a set of drop down boxes for each column in the target data table. The following summarization options are available:


* Group by (set as default)
* Sum
* Min
* Max
* First
* Last
* Count
* Mean
* Median
* Mode
* Std Dev
* Variance
* Product
* Absolute Val
* Quantile
* Skew
* Kurtosis
* Mean Abs Dev
* Cumulative Sum
* Cumulative Min
* Cumulative Max
* Cumulative Product


For more aggregation details, see the Analyze overview page [here](/docs/workflow-steps/common/aggregation).



### Data Filters
![Data Filters](/images/table_data_filters.png)

To allow for maximum flexibility, data filters are available on the source data and the target data. For larger data sets, it can be especially beneficial to filter out rows on the source so the remaining operations are performed on a smaller data set.



### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions)


for more details and examples.







### Select Subset of Final Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.



## **Examples**


### Data Filter – Temperature


In this example, the **Source Table**, *Import Google Spreadsheet*, is filtered to include only results in which the temperature was listed at 75 degrees Fahrenheit or above. As such, the **Target Table** is named *Filter Results Temp 75+*. 



All columns are mapped from source to target. No grouping, sorting, or summarization options are specified. 



In the **Data Filters** tab, the source data is subset with the following expression: *row[‘TemperatureF’] >= 75*. 



This expression only keeps rows which have a value in the *TemperatureF* column equal to 75 or higher. 



As expected on an Ohio summer day, the temperature first climbs above 75 degrees around noon and then remains there until nearly 10 PM.




### Table Data Selection – Unique Values


In this example, the same **Source Table**, *Import Google Spreadsheet*, is used, but in this case, it will be used to identify distinct conditions reported throughout the day. Accordingly, the **Target Table** is named *Distinct Conditions*. 



In this case, only a single column from the source data table is mapped to the target data table. Additionally, the **Make Distinct** button has been selected and applied only to the *Conditions* column. This should return only distinct values found in the source data table. 


{{< note >}}
When the target data table contains only a subset of the source data table, select the check box next to only the columns which **are** to be included in the target data table. Selecting all checkboxes could provide output that does not appear to be distinct.
{{< /note >}}




Since this example is looking for distinct values, it may be helpful to also identify non-distinct duplicate values. As such, any values which exist as duplicates will be added to the *duplicate values from raw data input*
data table. 


On this day, there were 4 unique conditions reported throughout the day. 
