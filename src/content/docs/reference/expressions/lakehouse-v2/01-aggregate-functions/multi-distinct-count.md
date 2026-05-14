---
title: MULTI_DISTINCT_COUNT
description: "Learn how to use the MULTI_DISTINCT_COUNT aggregate function in PlaidCloud Lakehouse. Returns the count of distinct values. Equivalent to COUNT(DISTINCT)."
---

Returns the count of distinct values. Equivalent to COUNT(DISTINCT).

## Analyze Syntax

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Analyze Examples

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## SQL Syntax

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## SQL Examples

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
