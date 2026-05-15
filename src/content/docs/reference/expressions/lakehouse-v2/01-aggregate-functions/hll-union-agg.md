---
title: HLL_UNION_AGG
description: HLL_UNION_AGG — Aggregates HLL values by computing the union.
---

Aggregates HLL values by computing the union.

## Analyze Syntax

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Analyze Examples

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL Syntax

```sql
HLL_UNION_AGG(<hll_col>)
```

## SQL Examples

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
