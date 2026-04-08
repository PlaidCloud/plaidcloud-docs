---
linktitle: Selecting the Latest Record in a Large Version History Table
title: Selecting the Latest Record in a Large Version History Table
description: Learn how to efficiently select the latest record from large history tables in PlaidCloud using optimized query techniques.
weight: 1.0
---

## Challenge

A table that contains many versions of each record is available but you must use the latest version.

## Discussion

This problem could be solved by selecting the ID and MAX update date into a temporary table.  Then that temporary table could be INNER JOINED back to the history table to obtain the result.  Unfortunately, this requires two steps and storing an intermediate table that has no function other than finding the latest update.

The more elegant solution to perform this operation in a single query uses a Window Function with sort plus a filter.

## Solution

### The version history table

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### Step Setup
Using an extract step, create a window function expression in a column called `Rank` like:

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

On the filter tab in the Extract step, set a filter like:

```python
table.Rank == 1
```

### The Result

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

This approach is highly efficient and allows selection of the latest record in a multi-version history table in a single step.  This works by ranking each record within the `employee_id` group by the `update_date` and then only picking the first record.

If there are multiple columns that make up the unique row key, you can add them to the `partition_by` argument as a list like:

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

If you need to apply multi-column sorts you can apply that with a list of columns too like:

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
