---
title: Allocation Source Map
---


![Allocation Source Map](/images/allocation_source_map.png)

The Allocation Source Map is used to map the columns from the **Values To Allocate Table** that will be used in the allocation step.

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

#### Role
Each column in the data mapper must be assigned a role:
- **Pass Thought** - These columns will appear in the allocation results table.
- **Value to Allocate** - This is the column that contains the values to be allocated.


#### Deleting Columns

To delete columns from the target data table, select the desired column(s), then right click and select **Delete**.

#### Changing Column Order

To rearrange columns in the target data table, select the desired column(s).  You can use either:
* **Bulk Move Arrows**: Select the desired move option from the arrows in the upper right
* **Context Menu**: Right clikc and select **Move to Top**, **Move Up**, **Move Down**, or **Move to Bottom**.

#### Reduce Result to Distinct Records Only

To return only distinct options, select the **Distinct** menu option. This will toggle a set of checkboxes for each column in the source. Simply check any box next to the corresponding column to return only distinct results.

Depending on the situation, you may want to consider use of Summarization instead.

The distinct process retains the first unique record found and discards the rest.  You may want to apply a sort on the data if it is important for consistency between runs.

{{< warning >}}
Selecting all columns to determine distincriveness might make it appear as if it isn't being applied.  Select only the columns you feel define the distictivness of the data.
{{< /warning >}}

#### Aggregation and Grouping

To aggregate results, select the **Summarize** menu option. This will toggle a set of select boxes for each column in the target data table. Choose an appropriate summarization method for each column.

- Group By
- Sum
- Min
- Max
- First
- Last
- Count
- Count (including nulls)
- Mean
- Standard Deviation
- Sample Standard Deviation
- Population Standard Deviation
- Variance
- Sample Variance
- Population Variance
- Advanced Non-Group_By


{{< note >}}
When using aggregation, all columns **must** have a summarization type specified
{{< /note >}}

For advanced data mapper usage such as expressions, cleaning, and constants, please see the [Advanced Data Mapper Usage](/docs/workflow-steps/common/advanced-data-mapper-usage)

