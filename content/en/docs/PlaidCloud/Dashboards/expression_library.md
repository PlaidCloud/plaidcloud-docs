---
title: Expression Library
slug: Expression_Library
weight: 6.0
description: A reference library of all expressions that can be used in PlaidCloud
date: 2022-06-07T07:39:48
---

## Description

An expression is a basic function that does a conversion, calculation, cast to another data type, or other action on data in a column or in a dashboard chart object. Examples are `startswith`, `max`, or `current_date`. For a full list of core expressions, see: [Standard Expressions](/docs/plaidcloud/analyze/expressions/). PlaidCloud expressions are based on PostgreSQL. For a more in depth tutorial or reference guide, please see: [tutorial](https://www.postgresqltutorial.com/)

There are three primary areas to apply expressions - metrics and calculated columns in datasets, and chart objects in dashboards.

## Navigating to a dataset
In order to view and edit metrics and calculated expressions:
1.  Sign into plaidcloud.com and navigate to Dasboards. Select the dashboard you want to work in.
2.  Select Data > Datasets from the menu.
3.  Search for a dataset to view or modify
4.  Hover over the dataset with the cursor and you will see icons in the actions column.
5.  Click the `edit` icon beneath `Actions`

## Viewing a chart object and adding an expression
You can add expressions to chart objects. For example, if you want to add an expression to a table object (a calculated column), you can:
1. Open the chart object by opening a dashboard, clicking on the three dot icon, and selecting "View chart in Explore".
2. Now that you are editing the chart, you can add a new Dimension or Metric, and do a `SIMPLE` expression, or a `CUSTOM SQL` expression

Now that you have located where you want to add an expression, you can use the table below as a guide to determining what expression you are looking for.

|Category&nbsp;&nbsp;&nbsp;&nbsp;|Expression|Structure|Example|Description|
|-----------|----------|---------|-------|-----------|
|Conditional|[case](/docs/plaidcloud/analyze/expressions/general-usage-conditionals/#the-case-operation)|case((expression, truevalue), else_ = falsevalue)|case((table.first_name.isnot(None), func.concat(table.first_name, table.last_name)), else_ = table.last_name)|a switch or a conditional control structure that allows the program to evaluate an expression and perform different actions based on the value of that expression|
|Conditional|[coalesce](/docs/plaidcloud/analyze/expressions/general-usage-conditionals/#coalesce)|func.coalesce(column1, column2, ...)|func.coalesce(table.nickname, table.first_name)|Returns the first non-null value in a set of columns. In the example, if there is a nickname it returns that, otherwise it returns the first name.|
|Conversion|[cast](/docs/plaidcloud/analyze/expressions/general-usage-data-type-expressions/#func-cast-type-conversions)|func.cast(value, datatype)|func.cast(123, Text)|Converts the value to a specific data type. In the example, it takes an Integer (123) and returns it as a string "123". For a full list of data types, see: [General Usage Data Type Expressions](/docs/plaidcloud/analyze/expressions/general-usage-data-type-expressions/)|
|Conversion|[to_char](/docs/plaidcloud/analyze/expressions/general-usage-data-type-expressions/#func-cast-type-conversions)|func.to_char(timestamp, text)|func.to_char(current_timestamp, 'HH12:MI:S S')|Converts a timestamp to text|
|Conversion|[to_char](/docs/plaidcloud/analyze/expressions/general-usage-data-type-expressions/#func-cast-type-conversions)|func.to_char(interval, text)|to_char(interval '15h 2m 12s', 'HH24:MI:S S')|Converts an interval to text|
|Conversion|[to_char](/docs/plaidcloud/analyze/expressions/general-usage-data-type-expressions/#func-cast-type-conversions)|func.to_char(integer, text)|func.to_char(125, '999')|Converts an integer to text|
|Conversion|[to_char](/docs/plaidcloud/analyze/expressions/general-usage-data-type-expressions/#func-cast-type-conversions)|func.to_char(bigfloat, text)|func.to_char(125.8::real, ‘999D9’)|Converts a bigfloat to text|
|Conversion|[to_char](/docs/plaidcloud/analyze/expressions/general-usage-data-type-expressions/#func-cast-type-conversions)|func.to_char(numeric, text)|func.to_char(-125.8, ‘999D99S’)|Converts a numeric object to text|
|Conversion|to_date|func.to_date(text, format)|func.to_date(table.Created_on, 'DD-MM-YYYY')|Convert a text field into a date formatted how you like|
|Conversion|to_number|func.to_number(text, format)|func.to_number ('12,454.8 -', '99G999D9S')|Convert a string to a numeric value|
|Conversion|to_timestamp|func.to_timestamp(text, format)|func.to_timestamp('05 Dec 2000', 'DD Mon YYYY')|Convert a string to a timestamp|
|Conversion|to_timestamp|func.to_timestamp(bigfloat)|func.to_timestamp(200120400)|Convert a bigfloat to a timestamp|
|Time|age|func.age(timestamp, timestamp)|func.age(return_date,rental_date)|Subtracts the second timestamp from the first one and returns an interval as a result|
|Time|age|func.age(timestamp)|func.age(birth_date)|Returns the interval between the current date and the argument provided|
|Time|clock_timestamp|func.clock_timestamp()|func.clock_timestamp()|Returns a timestamp for the current date and time which changes during execution|
|Time|current_date|func.current_date()|func.current_date()|Returns the a date object with the current date|
|Time|current_time|func.current_time()|func.current_time()|Returns a time object with the current time and timezone|
|Time|current_timestamp|func.current_timestamp()|func.current_timestamp()|Returns a timestamp object with the current date and time at the beginning of execution|
|Time|date_part|func.date_part(text, timestamp)|func.date_part('hour', timestamp '2001-02-1 6 20:38:40')|Returns the part of the timestamp you are looking for (month, year, etc.)|
|Time|date_part|func.date_part(text, interval)|func.date_part('month', interval '2 years 3 months')|Returns the part of the interval you are looking for (month, year, etc.)|
|Time|date_trunc|func.date_trunc(text, timestamp)|func.date_trunc('hour', timestamp '2001-02-1 6 20:38:40')|Truncate to specified precision
|Time|extract|func.extract(field from timestamp)|func.extract(hour from timestamp ‘2001-02-1 6 20:38:40’)|Get a field of a timestamp or an interval e.g., year, month, day, etc.|
|Time|extract|func.extract(field from interval)|func.extract(month from interval ‘2 years 3 months’)|Get a field of a timestamp or an interval e.g., year, month, day, etc.|
|Time|isfinite|func.isfinite(timestamp)|func.isfinite(timestamp ‘2001-02-1 6 21:28:30’)|Check if a date, a timestamp, or an interval is finite or not (not +/-infinity)|
|Time|isfinite|func.isfinite(interval)|func.isfinite(interval ‘4 hours’)|Check if a date, a timestamp, or an interval is finite or not (not +/-infinity)|
|Time|justify_days|func.justify_days(interval)|func.justify_days(interval ‘30 days’)|Adjust interval so 30-day time periods are represented as months|
|Time|justify_hours|func.justify_hours(interval)|func.justify_hours(interval ‘24 hours’)|Adjust interval so 24-hour time periods are represented as days|
|Time|justify_interval|func.justify_interval(interval)|func.justify_interval(interval ‘1 mon -1 hour’)|Adjust interval using justify_days and justify_hours, with additional sign adjustments|
|Time|now|func.now()|func.now()|Return the date and time with time zone at which the current transaction start|		
|Time|statement_timestamp|func.statement_timestamp()|func.statement_timestamp()|Return the current date and time at which the current statement executes|		
|Time|timeofday|func.timeofday()|func.timeofday()|Return the current date and time, like clock_timestamp, as a text string|
|Time|transaction_timestamp|func.transaction_timestamp()|func.transaction_timestamp()|Return the date and time with time zone at which the current transaction start|
