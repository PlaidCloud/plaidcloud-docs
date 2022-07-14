---
title: Table Lookup
slug: table-lookup
description: Similar to Microsoft Excel, this workflow function also increases process performance
date: 2022-01-25T07:39:49
---


## Description


If you are a regular user of the vlookup function in Microsoft Excel, the Table Lookup transform should feel very familiar. It’s used to perform essentially the same function. Unlike the Microsoft Excel version, the PlaidCloud Analyze Table Lookup transform offers greater flexibility, especially allowing for matching on and returning multiple columns.



## Table Data Selection




{{< include "common-table-source-selection.md" >}}


## Table Output




{{< include "common-target-table-creation.md" >}}


### Join Map

{{< include "common-table-join-map.md" >}}

### Target Output Columns


{{< include "common-data-mapper.md" >}}


## Output Filters


{{< include "common-data-filter.md" >}}



## Examples


### Lookup Product Dimension Information


In this example, the modeler needs information from the product dimension table to make sense of the order fact table. As such, the *Import Order Fact* table is selected as the **Source Table**. The *Import Product Dim* table contains the desired lookup information, so it’s selected as the **Lookup Table Source**. Although available, no filters are applied to the lookup data table (nor any other data tables, for that matter).



In the **Table Data Selection** section, all columns are mapped from the source data table to the target data table. 



No **Data Filters** are applied to either source or target data. 



Lastly, the source data table is matched to the lookup data table using the *Product_ID* field found in each table. Only the *Product_Description* and *Unit_Cost* columns are appended to the target data table, with *Unit_Cost* being renamed to *Retail_Unit_Cost* in the process. 



In the resulting target data table, the *Product_Description* and *Retail_Unit_Cost* columns have been added, based on matching values in the *Product_ID* column. 
