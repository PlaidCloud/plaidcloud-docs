---
title: MIN
description: "Learn how to use the MIN aggregate function in PlaidCloud Lakehouse. Returns the minimum value in a set of values - see syntax, examples, and output."
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
