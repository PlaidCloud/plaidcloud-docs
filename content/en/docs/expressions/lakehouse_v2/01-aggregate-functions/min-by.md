---
title: MIN_BY
description: "Learn how to use the MIN_BY aggregate function in PlaidCloud Lakehouse. Returns the value of one column associated with the minimum value of another column."
---

Returns the value of one column associated with the minimum value of another column.

## Analyze Syntax

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyze Examples

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## SQL Syntax

```sql
MIN_BY(<name>, <salary>)
```

## SQL Examples

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
