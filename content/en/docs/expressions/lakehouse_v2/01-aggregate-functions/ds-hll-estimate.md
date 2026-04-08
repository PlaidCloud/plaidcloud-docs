---
title: DS_HLL_ESTIMATE
description: "Learn how to use the DS_HLL_ESTIMATE aggregate function in PlaidCloud Lakehouse. Estimates the cardinality from a DataSketches HLL sketch."
---

Estimates the cardinality from a DataSketches HLL sketch.

## Analyze Syntax

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Analyze Examples

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## SQL Syntax

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## SQL Examples

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
