---
title: DS_HLL_ACCUMULATE
description: "Use the DS_HLL_ACCUMULATE aggregate function in PlaidCloud Lakehouse. Accumulates values into a DataSketches HLL sketch for approximate distinct counting."
---

Accumulates values into a DataSketches HLL sketch for approximate distinct counting.

## Analyze Syntax

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Analyze Examples

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## SQL Syntax

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## SQL Examples

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
