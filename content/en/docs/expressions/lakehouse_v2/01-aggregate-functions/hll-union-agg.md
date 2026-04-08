---
title: HLL_UNION_AGG
description: "Learn how to use the HLL_UNION_AGG aggregate function in PlaidCloud Lakehouse. Aggregates HLL values by computing the union - with syntax and examples."
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
