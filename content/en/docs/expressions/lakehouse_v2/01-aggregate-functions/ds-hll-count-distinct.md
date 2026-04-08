---
title: DS_HLL_COUNT_DISTINCT
description: "Use the DS_HLL_COUNT_DISTINCT aggregate function in PlaidCloud Lakehouse. Returns an approximate distinct count using DataSketches HLL algorithm. More."
---

Returns an approximate distinct count using DataSketches HLL algorithm. More accurate than `APPROX_COUNT_DISTINCT`.

## Analyze Syntax

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Analyze Examples

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## SQL Syntax

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## SQL Examples

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
