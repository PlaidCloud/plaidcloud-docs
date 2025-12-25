---
title: Dimension Load
slug: dimension-load
weight: 4.0
description: Load and update dimensions using data
date: 2022-01-25T07:40:18
---


## Description
Load and update dimensions using data from PlaidCloud tables.


![Dimension Load](/images/dimension_load.png)

## Dimension Selection
### Specify Dimension Dynamically
To specify a dimension dynamically you include  **project** and or **local** variables in the name.


Variables are useful when dimensions are updated on a periodic basis and retaining the historical view is desired.

An example that uses the `current_month` variable to dynamically load the dimension:

```
dimension_name_{current_month}
```
### Use Specific Dimension

To use a specific dimension select the **dimension** using the drop down menu.


### Load to Alternate Hierarchy

To load an Alternate Hierarchy fist select the dimension either dynamically or specifically, click the Load to Alternate Hierarchy checkbox and enter the name of the alternate hierarchy to be loaded.

{{< note >}}
It is often useful to have alternate views / rollups of the main dimension. For instance, cost centers usually have an accounting rollup but an alternate view based on organizational structure might be desired.
{{< /note >}}

## Source Table

### Dynamic 
To specify the source table dynamically click the **Dynamic Checkbox** and enter the table name including the **project** and or **local** variables in the name.

### Static

To use a specific **source table** select the table using the drop down menu.

## Dimension Properties And Table Layout

### Default Consolidation Type

There are three options for consolidation types:
* **"+"**: Aggregates values in the dimension.
* **"-"**: Subtracts values in the dimension.
* **"~"**: No aggregation is performed in the dimension.

{{< note >}}
In the source data table you can include **Consolidation Type** as a column so multiple consolidation types can be used within a dimension. The **Consolidation Type** column is then used in the **Column Mapping** section below.
{{< /note >}}

### Table Column Format
There are two options for fomatting the **Source Table** when loading a dimension. 
#### Parent Child
In a Parent Child table there are two columns that represent the dimensions structure, **Parent** and **Child**.

**EXAMPLE PARENT CHILD**

| PARENT    | CHILD    | Consolidation Type |
|-----------|----------|--------------------|
|Parent All | Parent 1 |        ~           |
|Parnet All | Parent 2 | ~                  |
| Parent 1  | Child 1  | +                  |
| Parent 2  | Child 2  | +                  |
| Child 1   | Child 3  | +                  |
| Child 1   | Child 4  | +                  |
| Child 2   | Child 5  | +                  |

{{< note >}}
In the Parent Child table format you can also include a **Consolidation Type** column in the table. The **Consolidation Type** is associated with the child.
{{< /note >}}

#### Flattened Levels
In a Flattend Level table there are an infinte number of columns with each column representing a level of the dimension.

**EXAMPLE FLATTENED LEVELS**

|Level 1   |Level 2 |Level 3|Level 4|
|----------|--------|-------|-------|
|Parent All|Parent 1|Child 1|Child 3|
|Parent All|Parent 1|Child 1|Child 4|
|Parent All|Parent 2|Child 2|Child 5|

## Column Mapping

Using the **Inspect Source** menu button populates the **Source Column** in the data mapper.
Once the **Source Column** has been populated use the **Kind** drop down menu to map the **Source Columns** to the appropriate column type.

