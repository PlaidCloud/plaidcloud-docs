---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG — Aggregates HLL values into a single HLL value.
---

Aggregates HLL values into a single HLL value.

## Analyze Syntax

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Analyze Examples

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL Syntax

```sql
HLL_RAW_AGG(<hll_col>)
```

## SQL Examples

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
