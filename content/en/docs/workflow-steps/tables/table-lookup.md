---
title: Table Lookup
slug: table-lookup
description: Similar to Microsoft Excel, this workflow function also increases process performance
date: 2022-01-25T07:39:49
---


## Description


If you are a regular user of the vlookup function in Microsoft Excel, the Table Lookup transform should feel very familiar. It’s used to perform essentially the same function. Unlike the Microsoft Excel version, the PlaidCloud Analyze Table Lookup transform offers greater flexibility, especially allowing for matching on and returning multiple columns.



## Source Tables and Target Parameters


### Source Tables and Target
![Lookup Table 1](/images/lookup_table1.png)
### Table 1 Source
To establish the source table to be extracted from select the **Table 1** tab and using the **Source Table** dropdown menu select the desired table.
This list includes all *Project* and *Workflow* data tables.
#### Select Subset of Source Data


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions)


for more details and examples.





### Table 2 Lookup Table Source

Select the **Table 2** tab and using the **Source Table** dropdown menu select the desired table, this is the table that you will be looking up values from. 
This list includes all *Project* and *Workflow* data tables.

#### Select Subset of Lookup Data

Any valid Python expression is acceptable to subset the data. Please see the following section for more details and examples: [Expressions](/docs/expressions)

### Table Output Target Table
![Lookup Table Output](/images/lookup_output.png)

Select the **Table Output** tab and using the **Target Table** dropdown either select an existing table or click on the green **"+"** sign to create a new table as the target. 

#### Table Creation
When creating a new table you will have the option to either create it as a **View** or as a **Table**. 
##### Views:
Views are useful in that the time required for a step to execute is significantly less than when a table is used. The downside of views is they are not a useful for data exploration in the table Details mode.

##### Tables:
When using a table as the target a step will take longer to execute but data exploration in the Details mode is much quicker than with a view.

{{< note >}}
Use tables for key steps in your workflows where data validation or the ability to perform ad-hoc analytics will be necessary. For all other steps use views to decrease the overall workflow calculation time. It's possible to change a table to a view and vice versa so you can always update the table target type at a later date.
{{< /note >}}
### Table Output Data Selection

#### Target Output Columns
The **Target Output Columns** section is used to map columns from the source data table to the target data table. All source columns on the left side of the window are automatically mapped to the target data table depicted on the right side of the window. Using the **Inspect Source** menu button, there are a few additional ways to map columns from source to target:


* Populate Both Mapping Tables: Propagates all values from the source data table into the target data table. This is done by default.
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





### Lookup Operation


### Lookup Columns and Replacements


To view the columns available in the lookup table, simply select the **Inspect Source** button and one of its options to **Populate Lookup Source Mapping Table**. If desired, options are available to preview the data in the lookup table.



By default, the lookup table returns distinct values for all columns. Since a lookup returns the first matching value, it is not necessary to leave duplicate values in the lookup table. If desired, this option can be turned off by deselecting the **Distinct** checkbox for individual columns.



### Table Relationship Join Field Map


The **Table Relationship Join Field Map** is used to specify all columns used for matching. By using the **Guess** button, Analyze will populate the relationship map with all columns from the source data table which have a matching name in the lookup data table.



Additionally, these values can be entered manually by right-clicking the mouse button and selecting either **Insert Row** or **Append Row** to insert a row prior to the selected row or to insert a row at the bottom of the list, respectively. In a similar manner, items can be removed by right-clicking and selecting the **Delete** option.



### Field Value Map


The **Field Value Map** is used to append columns of data onto the target data table based upon matching values found. By default, using the **Guess** button will add all columns which were **not** used in the **Lookup Relationship Map** section. If not all columns are desired, items can be removed by right-clicking and selecting the **Delete** option.



Additionally, there are options available to rename the mapped columns simply by clicking into the **Update/Add Data Table Field** selection and adjusting the name as desired. Column order can also be adjusted as desired by right-clicking on an item and using the **Move to Top**, **Move Up**, **Move Down**, or **Move to Bottom** options.


### Select Subset of Data Based On Aggregations


Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples






## Examples


### Lookup Product Dimension Information


In this example, the modeler needs information from the product dimension table to make sense of the order fact table. As such, the *Import Order Fact* table is selected as the **Source Table**. The *Import Product Dim* table contains the desired lookup information, so it’s selected as the **Lookup Table Source**. Although available, no filters are applied to the lookup data table (nor any other data tables, for that matter).



In the **Table Data Selection** section, all columns are mapped from the source data table to the target data table. 



No **Data Filters** are applied to either source or target data. 



Lastly, the source data table is matched to the lookup data table using the *Product_ID* field found in each table. Only the *Product_Description* and *Unit_Cost* columns are appended to the target data table, with *Unit_Cost* being renamed to *Retail_Unit_Cost* in the process. 



In the resulting target data table, the *Product_Description* and *Retail_Unit_Cost* columns have been added, based on matching values in the *Product_ID* column. 
