---
title: func.last_value
slug: func-last-value
description: The LAST_VALUE() function is a window function that returns the last value in an ordered partition of a result set
date: 2022-01-25T07:40:02
---

The LAST_VALUE() function is a window function that returns the last value in an ordered partition of a result set

## Syntax
```python
func.last_value(field).over(partition_by=field, order_by=field)
```

## Examples
This is an example of using the `last_value()` capability to calculate the time remaining in time series data where each event is on a distinct row.

This assumes you have a table of time series data that looks like this:

| location   | employee | timestamp           |
|------------|----------|---------------------|
| Building A | John Doe | 2022-01-05 15:34:31 |
| Building A | John Doe | 2022-01-05 15:44:31 |
| Building A | John Doe | 2022-01-05 15:46:41 |

```python
func.last_value(table.timestamp, 1).over(partition_by=[table.location, table.employee], order_by=table.timestamp) - table.timestamp
```

Adding the expression above to an **Interval** column called `remaining` would result in an output table like this:

| location   | employee | timestamp           | remaining |
|------------|----------|---------------------|-----------|
| Building A | John Doe | 2022-01-05 15:34:31 | 00:12:10  |
| Building A | John Doe | 2022-01-05 15:44:31 | 00:02:10  |
| Building A | John Doe | 2022-01-05 15:46:41 | 00:00:00  |
