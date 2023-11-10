---
title: Advanced Data Mapper Usage
slug: advanced-data-mapper-usage
weight: 1.0
description: Using the advanced features of the Data Mapper
date: 2022-01-25T07:39:53
---

## Review

Before jumping into the advanced usage capabilities of the Data Mapper, a brief review of the basic functionality will help.

### Data Mapper Configuration

The Data Mapper is used to map columns from the source data to the target data table.

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
Selecting **Propagate All** may create a duplicate of every column. Analyze does not check to see if the columns are already mapped. Make sure duplicate column names do not exist.
{{< /warning >}}

#### Deleting Columns

To delete columns from the target data table, select the desired column(s), then right click and select **Delete**.

#### Chaging Column Order

To rearrange columns in the target data table, select the desired column(s).  You can use either:
* **Bulk Move Arrows**: Select the desired move option from the arrows in the upper right
* **Context Menu**: Right clikc and select **Move to Top**, **Move Up**, **Move Down**, or **Move to Bottom**.

#### Reduce Result to Distinct Records Only

To return only distinct options, select the **Distinct** menu option. This will toggle a set of checkboxes for each column in the source. Simply check any box next to the corresponding column to return only distinct results.

{{< warning >}}
When the target data table contains only a subset of the source data table, only select the check box next to the columns which **are** to be included in the target data table. Selecting all checkboxes could provide output that does not appear to be distinct.
{{< /warning >}}

#### Aggregation and Grouping

To aggregate results, select the **Summarize** menu option. This will toggle a set of select boxes for each column in the target data table. Choose an appropriate summarization method for each column.

{{< note >}}
When using aggregation, all columns **must** have a summarization type specified
{{< /note >}}

## Advanced Usage

### Aggregation Options

To aggregate results, select the **Summarize** menu option. This will toggle a set of select boxes for each column in the target data table. The following summarization options are available:

| Function | Description |
|----------|-------------|
| Group By | Groups results by the value |
| Count | Number of non-null observations in group |
| Count (including nulls) | Number of observations in group |
| Sum | Sum of values in group |
| Mean | Mean of values in group |
| Median | Median of values in group |
| Mode | Mode of values in group |
| Min | Minimum of values in group |
| Max | Maximum of values in group |
| First | First value of values in group using the sorted order |
| Last | Last value of values in group using the sorted order |
| Standard Deviation | Unbiased standard deviation in group |
| Sample Standard Deviation | Sample standard deviation in group |
| Population Standard Deviation | Population standard deviation in group |
| Variance | Unbiased variance in group |
| Sample Variance | Sample Variance in group |
| Population Variance | Population Variance in group |
| Advanced Non-Group-By | Special aggregation selection when using window functions |


Pick the appropriate summarization method for the column.

{{< note >}}
When using aggregation, all columns **must** have a summarization type specified
{{< /note >}}

When using a [Window Function](/docs/workflow-steps/common/window-functions), select **Advanced Non-Group-By** as the aggregation method.  This special selection is required
due to the aggregation inherent in the window function already.

### Constants

Specifying a value in the *Constant* column will override the source column value, if specified, and populate the column with the constant value specified.

### Cleaners

The Data Mapper provides a convenient point-and-click cleaner capability to apply conversions to the data within a column.

The cleaning operations include the following categories:
 * Text Trimming
 * Text Formatting
 * Text Transformations
 * Converting to and from NULL values
 * Number Formatting
 * Date Parsing

The result of the cleaner selections are converted into a consolidated expression which is viewable in the Expression information.

{{< note >}}
If you edit the generated expression, the cleaner form will no longer be connected to the expression.  Viewing the expression will not disconnect it though.
{{< /note >}}

### Expressions

[Expressions](/docs/expressions) in the Data Mapper are one of the most powerful and flexible concepts in PlaidCloud.  They provide nearly unlimited flexibility while being exceptionally performant, even on extremely large data.

[Expressions](/docs/expressions) are written using [Python SQLAlchemy](https://www.sqlalchemy.org/) syntax along with a few additional helper functions available in PlaidCloud. 
This allows PlaidCloud to expose the full set of capabilities of the underlying data warehouse (e.g. Greenplum, SAP HANA, Redshift, etc...) directly.  In addition, there are many resources available publicly that provide quick
references for use of SQLAlchemy operations.  By using standard SQLAlchemy syntax, PlaidCloud avoids the common pitfall of creating yet another domain specific syntax.

The expression editor is opened by double-clicking on the expression cell for the column.  Once open, the list of columns are shown on the left while an extensive library of functions are shown on the right.

While it is entirely possible to type the expression directly into the editor, it is normally easier to use the point-and-click function and column selection to get started.  The library of functions include the following groups:

 * Conditions
 * Column Specific Conditions
 * Conversions
 * Dates
 * Math
 * Text
 * Summarizations
 * Window Function Operations
 * Arrays
 * JSON
 * PostGIS (Geospatial)
 * Trigonmetry

Once you have completed the expression, save the expression so it will be applied to the column.

View examples and expression functions in the [Expressions](/docs/expressions) area.

{{< note >}}
Expressions are validated when the transform step is saved
{{< /note >}}
