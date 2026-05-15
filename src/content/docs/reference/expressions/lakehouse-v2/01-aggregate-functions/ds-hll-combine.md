---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE — combines multiple DataSketches HLL sketches into a single sketch.
---

Combines multiple DataSketches HLL sketches into a single sketch.

## Analyze Syntax

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Analyze Examples

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## SQL Syntax

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## SQL Examples

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
