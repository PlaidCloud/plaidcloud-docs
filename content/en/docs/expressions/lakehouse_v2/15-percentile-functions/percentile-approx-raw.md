---
title: PERCENTILE_APPROX_RAW
---

Returns an approximate percentile value from a precomputed percentile state.

## Analyze Syntax

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Analyze Examples

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## SQL Syntax

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## SQL Examples

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
