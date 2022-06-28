---
title: Table Upsert
slug: table-upsert
description: Perform an update of existing records or append new ones
date: 2022-01-25T07:40:19
---

## Description

Performs an update of existing records and append new ones.

## Source and Target Table Selection

![Upsert Tables](/images/table_upsert_1.png)

### Source Table

Specify the source data table by selecting it from the dropdown menu.

### Target Table

To establish the target table select either an existing table as the target table using the **Target Table** dropdown or click on the green **"+"** sign to create a new table as the target. 

{{< note >}}
For an Upsert the target table must be a table and not a view.
{{< /note >}}



### Source Table Data Selection

![Upsert Key](/images/table_upsert_2.png)

#### Inspection and Populating the Mapper

Using the **Inspect Source** menu button provides additional ways to map columns from source to target:

* Populate Both Mapping Tables: Propagates all values from the source data table into the target data table. This is done by default.
* Populate Source Mapping Table Only: Maps all values in the source data table only. This is helpful when modifying an existing workflow when source column structure has changed.
* Populate Target Mapping Table Only: Propagates all values into the target data table only.

If the source and target column options aren’t enough, other columns can be added into the target data table in several different ways:

* **Propagate All** will insert all source columns into the target data table, whether they already existed or not.
* **Propagate Selected** will insert selected source column(s) only.
* Right click on target side and select **Insert Row** to insert a row immediately above the currently selected row.
* Right click on target side and select **Append Row** to insert a row at the bottom (far right) of the target data table.

{{< warning >}}
Selecting *Propagate All* will duplicate columns if they already exist in the target list
{{< /warning >}}

#### Update Key

In order for the Upsert to update the existing and append new records you need to select the columns in the data that create a unique key.


