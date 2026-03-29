---
title: HLL_UNION
---

Returns the union of multiple HLL values.

## Analyze Syntax

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Analyze Examples

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL Syntax

```sql
HLL_UNION(<hll_col>)
```

## SQL Examples

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
