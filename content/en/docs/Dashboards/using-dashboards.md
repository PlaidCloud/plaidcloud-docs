---
title: Using Dashboards
slug: using-dashboards
description: Create and edit data tables within dashboard and explore the data
date: 2022-01-25T07:39:48
weight: 2.0
---


## Description


Usually, members will have access to multiple workspaces and projects. Having this data in multiple spots, however, may not always be desirable. This is why PlaidCloud allows the ability to view all of the accessible data in a single location through the use of dashboards and highly intuitive data exploration. PlaidCloud Dashboards (where the dashboards and data exploration are integrated) provides a rich pallet of visualization and data exploration tools that can operate on virtually any size dataset. This setup also makes it possible to create dashboards and other visualizations that combine information across projects and workspaces, including Ad-hoc analysis.



## Editing a Table


The message you receive after creating a new table also directs you to edit the table configuration. While there are more advanced features to edit the configuration, we will start with a limited and more simple portion. To edit table configuration:


1. Click on the edit icon of the desired table
2. Click the “List Columns” tab
3. Arrange the columns as desired
4. Click “Save”

This allows you to define the way you want to use specific columns of your table when exploring your data.


* **Groupable:** If you want users to group metrics by a specific field
* **Filterable:** If you need to filter on a specific field
* **Count Distinct:** If you want want to get the distinct count of this field
* **Sum:** If this is a metric you want to sum
* **Min:** If this is a metric you want to gather basic summary statistics for
* **Max:** If this is a metric you want to gather basic summary statistics for
* **Is temporal:** This should be checked for any date or time fields

## Exploring Your Data


To start exploring your data, simply click on the desired table. By default, you’ll be presented with a Table View.



### Getting a Data Count


To get a the count of all your records in the table:


1. Change the filter to “Since”
2. Enter the desired since filter


	* You can use simple phrases such as “3 years ago”
3. Enter the desired until filter


	* The upper limit for time defaults is “now”
4. Select the “Group By” header
5. Type “Count” into the metrics section
6. Select “COUNT(*)”
7. Click the “Query” button

You should then see your results in the table.

**If you want to find the count of a specific field or restriction:**

1. Type in the desired restriction(s) in the “Group By” field
2. Run the query

{{< note >}}
When using “measurement” in a restriction it will refer to the value of the measurement taken which depends on the type of measurement. Therefore you should ensure the measurement types are the same under the “filter section (e.g. weather_description and Maximum temperature.)”
{{< /note >}}

### Restricting Result Number

If you only need a certain number of results, such as the top 10:

1. Select “Options”
2. Type in the desired max result count in the “Row Limit” section
3. Click “Query”

### Additional Visualization Tools

To expand abbreviated values to their full length:

1. Select “Edit Table Config”
2. Click “List Sql Metric”
3. Click “Edit Metric”
4. Click “D3Format”

To edit the unit of measurement:


1. Select “Edit Table Config”
2. Click “List Sql Metric”
3. Click “Edit Metric”
4. Click “SQL Expression”

To change the chart type:


1. Scroll to “Chart Options”
2. Fill in the required fields
3. Click “Query”

From here you are able to set axis labels, margins, ticks, etc.
