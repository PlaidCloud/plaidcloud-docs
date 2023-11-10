---
title: Table Explorer
slug: table-explorer
description: Table Explorer provides powerful and readily accessible data exploration capabilities
date: 2022-01-25T07:39:48
weight: 1.0
---


Table Explorer provides a powerful and readily accessible data exploration tool with built in filtering, summarization, and other features to make
life easy for people working with large and complex data.

Table Explorer supports exploration on any size dataset so you can use the same tool no matter how much your data grows.  It also provides point-and-click 
filtering along with advanced filter capabilities to zero in on the data you need.  The best part is that anywhere in PlaidCloud with tables or views, 
you can click on those tables and views to explore with Table Explorer.  By being fully integrated, data access is only a click away.

The `Grid` view provides a tabular view of the data. The `Details` view provides a summary of each column, a count of unique values, and summary statistics for numeric columns.

Data can be exported directly from a filtered set as well as being able to save and share filters with others.  Finally, the filters and column settings 
can be saved directly as a workflow `Extract` step.


## The Grid View

The Grid view provides a tabular view of the data.


### Setting the row limit

By default, the row limit is set to 5,000 rows.  However, this can be adjusted or disabled entirely.

The rows shown along with the total size of the dataset are shown at the bottom of the table.  The information provides three key pieces of information:
 1. The current row count shown based on the row limit applied
 2. The size of the global data after filters are applied
 3. The size of the unfiltered global data

{{< caution >}}
Be careful not to disable the row limit functionality when viewing larger (e.g. millions of rows) because this could cause your browser to run slow.  Try using filters to find the data instead.
{{< /caution >}}


### Sorting locally versus globally

The Grid view provides the ability to click on the column header and sort the data based on that column.  However, this method is only sorting the dataset
that has already been retrieved and is not sorting based on the full dataset.  If your retrieved data contains the entire dataset this distinction is immaterial however if your full dataset is larger than what appears in the browser, this may not be the desired sort result.

If you desire to sort the global dataset before retrieving the limited data that will appear in your browser those sorts can be applied to the columns in the `Details` view by clicking on the `Sort` icon at the top of each column.  An additional benefit of using the global sort approach is that you can apply multiple sorts along with a mix of sort directions.


## Quick reference column list

All of the columns in the table or view are shown on the left of the Table Explorer window by default.  This column list can be toggled on and off using the 
column list toggle button.

The column list provides a number of quick access and useful features including:
 * Double clicking an item jumps to the column in the `Grid` or `Details` view
 * Control visibility of the column through the visibility checkbox
 * Use multi-select and right-click to include or exclude many columns at once
 * Quickly view the data type of each column using the data type icons
 * View the total column count


## The Details View

The `Details` view provides an efficient way to view the data at a high level and exposes tools to quickly filter down to information
with point-and-click operations.

{{< note >}}
Column summaries are not automatically generated for views.  You can click on the column refresh button to calculated the details though.
{{< /note >}}


### Column data and unique counts

Each column is shown, provided it is currently marked as visible.  The column summary displays the top 1,000 unique values by count.  The number
of unique values shown can be adjusted by selecting the `Detailed Rows Displayed` selection for a different value.


### Managing point-and-click filters

Each column provides for point-and-click filtering by activating the filter toggle at the top of the column.  Select the items in the column that you
would like to include in the resulting data.  Multi-select is supported.

Once you apply a filter, there may be items you wish to remove or to clear the entire column filter without clearing all filters.  This is accomplished
by selecting the dropdown on the column filter button and unchecking columns or selecting the clear all option at the top.


### Managing Summarization

Summarization of the data can be applied by toggling the `Summarize` button to `On`.  When the `Summarize` button is activated, each column will display
a summarization type to apply.  Adjust the summarization type desired for each column.

When the desired summarizations are complete, refresh the data and the summarizations will be applied.


### Finding Distinct Values

Activating the `Distinct` button will help reduce the data to only a set of unique records.  When the `Distinct` button is active, a *Distinct* checkbox will appear on each column.  Uncheck the columns that *DO NOT* define uniqueness of the column to the dataset.  For example, if you want to find the unique set of customers in a customer order table, you would only want to select the customer column rather than including the customer order number too.

{{< caution >}}
If you include too many columns in the unique records determination, it will appear you have many more distinct results than you should.
{{< /caution >}}


### Summary statistics for numeric columns

Integer and numeric columns automatically display summary statistics at the bottom of the column information.  This includes:
 * Min
 * Max
 * Mean
 * Sum
 * Standard Deviation
 * Variance

 These statistics are calculated on the full **filtered** dataset.


## Copying Data

It is sometimes useful to allow for copying of selected data from PlaidCloud so that it can be pasted into other applications
such as a spreadsheet.

From the Copy button in the upper right, there are several copy options available for the data:
 * Copy All - Copies all of the data to the clipboard
 * Copy Selection - Copies the selected data to the clipboard
 * Copy Cell - Copies only the contents of a single cell to the clipboard
 * Copy Column - Copies the full contents of the column to the clipboard


## Exporting Data

Exporting data from the Table Explorer interface allows exporting of the filtered data with only the columns visible.  You can export
in the following formats:
 * Microsoft Excel (xlsx)
 * CSV (Comma)
 * TSV (Tab)
 * PSV (Pipe)

The Download menu also offers the ability to download only the rows visible in the browser.  This is based on using the row limit specified.


## Additional Actions

Additional useful actions are available under the `Actions` menu.


### Save as Extract Step

When exploring data, it is often in the context of determining how to filter it for a data pipeline process.  This often consists of applying multiple filters
including advanced filters to zero in on the desired result.

Instead of attempting to replicate all the filters, columns, summarizations, and sorts in an Extract Step, you can simply save the existing Table Explorer settings
as a new Extract Step. 


### Save as View

Similar to saving the current Table Explorer settings as an Extract Step above, you can also save the settings directly as a view.

This can be particularly useful when trying to construct slices of data for reporting or other downstream processes that don't require a
a data pipeline.


### Manage Saved Filters

You never have to lose your filter work.  You can save your Table Explorer settings as a saved filter.  Saved filters also include column visibility, summarizations,
columns filters, advanced filters, and sorts.

You can also let others use a saved filter by checking the `Public` checkbox when saving the filter.

From the `Actions` menu you can also choose to delete and rename saved filters.


## Advanced Filters

While point-and-click column filters allow for quick application of filters to zero in on the desired results, sometimes filter conditions are complex and 
need more advanced specifications.

The advanced filter area provides both a pre-aggregation filter as well as a post-aggregation filter, if `Summarize` is enabled.

Any valid Python expression is acceptable to subset the data. Please see [Expressions](/docs/expressions) for more details and examples.
