---
title: MULTI_DISTINCT_COUNT
description: MULTI_DISTINCT_COUNT — returns the count of distinct values. Equivalent to COUNT(DISTINCT).
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
