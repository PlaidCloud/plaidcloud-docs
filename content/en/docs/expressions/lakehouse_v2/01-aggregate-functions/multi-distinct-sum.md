---
title: MULTI_DISTINCT_SUM
description: "Learn how to use the MULTI_DISTINCT_SUM aggregate function in PlaidCloud Lakehouse. Returns the sum of distinct values - see syntax, examples, and output."
---

Returns the sum of distinct values.

## Analyze Syntax

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Analyze Examples

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## SQL Syntax

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## SQL Examples

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
