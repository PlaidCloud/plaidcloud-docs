---
title: func.first_value
slug: func-first-value
description: FIRST_VALUE is a function that returns the first value in an ordered set of values
date: 2022-01-25T07:40:02
---

FIRST_VALUE is a function that returns the first value in an ordered set of values

## Syntax
```python
func.first_value(field).over(partition_by=field, order_by=field)
```

## Examples
This is an example of using the `first_value()` capability to calculate the running time of the time series data where each event is on a distinct row.

This assumes you have a table of time series data that looks like this:

| location   | employee | timestamp           |
|------------|----------|---------------------|
| Building A | John Doe | 2022-01-05 15:34:31 |
| Building A | John Doe | 2022-01-05 15:44:31 |
| Building A | John Doe | 2022-01-05 15:46:41 |

```python
table.timestamp - func.first_value(table.timestamp, 1).over(partition_by=[table.location, table.employee], order_by=table.timestamp)
```

Adding the expression above to an **Interval** column called `run_time` would result in an output table like this:

| location   | employee | timestamp           | run_time  |
|------------|----------|---------------------|-----------|
| Building A | John Doe | 2022-01-05 15:34:31 | 00:00:00  |
| Building A | John Doe | 2022-01-05 15:44:31 | 00:10:00  |
| Building A | John Doe | 2022-01-05 15:46:41 | 00:12:10  |
