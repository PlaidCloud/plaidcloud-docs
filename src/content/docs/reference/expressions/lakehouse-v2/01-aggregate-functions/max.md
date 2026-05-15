---
title: MAX
description: MAX — returns the maximum value in a set of values - see syntax, examples, and output.
---

Returns the maximum value in a set of values.

## Analyze Syntax

```python
func.max(get_column(table, 'salary'))
```

## Analyze Examples

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## SQL Syntax

```sql
MAX(<salary>)
```

## SQL Examples

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
