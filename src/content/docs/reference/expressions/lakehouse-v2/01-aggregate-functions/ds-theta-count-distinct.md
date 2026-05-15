---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "Use the DS_THETA_COUNT_DISTINCT aggregate function in PlaidCloud Lakehouse. Returns an approximate distinct count using DataSketches Theta algorithm. Supports."
---

Returns an approximate distinct count using DataSketches Theta algorithm. Supports set operations like intersection and difference.

## Analyze Syntax

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Analyze Examples

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## SQL Syntax

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## SQL Examples

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
