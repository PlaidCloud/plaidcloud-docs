---
title: HLL_RAW_AGG
description: "Learn how to use the HLL_RAW_AGG aggregate function in PlaidCloud Lakehouse. Aggregates HLL values into a single HLL value - with syntax and examples."
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
