---
title: MIN (Lakehouse v2)
description: MIN — returns the minimum value in a set of values.
---

Returns the minimum value in a set of values.

## Analyze Syntax

```python
func.min(get_column(table, 'salary'))
```

## Analyze Examples

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## SQL Syntax

```sql
MIN(<salary>)
```

## SQL Examples

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
