---
title: MAX_BY
description: "Learn how to use the MAX_BY aggregate function in PlaidCloud Lakehouse. Returns the value of one column associated with the maximum value of another column."
---

Returns the value of one column associated with the maximum value of another column.

## Analyze Syntax

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyze Examples

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## SQL Syntax

```sql
MAX_BY(<name>, <salary>)
```

## SQL Examples

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
