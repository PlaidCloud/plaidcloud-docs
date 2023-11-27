---
title: func.lag
slug: func-lag
description: This function lets you query more than one row in a table at a time without having to join the table to itself
date: 2022-01-25T07:40:02
---

This function lets you query more than one row in a table at a time without having to join the table to itself

## Syntax
```python
func.lag(field, 1).over(partition_by=field, order_by=field)
```

## Examples
This is an example of using the `lag()` capability to calculate the time interval in time series data where each event is on a distinct row.

This assumes you have a table of time series data that looks like this:

| location   | employee | timestamp           |
|------------|----------|---------------------|
| Building A | John Doe | 2022-01-05 15:34:31 |
| Building A | John Doe | 2022-01-05 15:44:31 |
| Building A | John Doe | 2022-01-05 15:46:41 |

```python
table.timestamp - func.lag(table.timestamp, 1).over(partition_by=[table.location, table.employee], order_by=table.timestamp)
```

Adding the expression above to an **Interval** column called `delta` would result in an output table like this:

| location   | employee | timestamp           | delta    |
|------------|----------|---------------------|----------|
| Building A | John Doe | 2022-01-05 15:34:31 | *null*   |
| Building A | John Doe | 2022-01-05 15:44:31 | 00:10:00 |
| Building A | John Doe | 2022-01-05 15:46:41 | 00:02:10 |
