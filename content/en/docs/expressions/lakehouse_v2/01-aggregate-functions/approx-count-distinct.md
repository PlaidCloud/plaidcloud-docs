---
title: APPROX_COUNT_DISTINCT
---

Returns an approximate count of distinct values using HyperLogLog.

## Analyze Syntax

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Analyze Examples

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## SQL Syntax

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## SQL Examples

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
