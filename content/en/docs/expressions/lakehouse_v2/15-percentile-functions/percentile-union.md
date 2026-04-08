---
title: PERCENTILE_UNION
description: "Learn how to use the PERCENTILE_UNION percentile function in PlaidCloud Lakehouse. Returns the union of multiple percentile states - with syntax and examples."
---

Returns the union of multiple percentile states.

## Analyze Syntax

```python
func.percentile_union(<state>)
```

## Analyze Examples

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## SQL Syntax

```sql
PERCENTILE_UNION(<state>)
```

## SQL Examples

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
