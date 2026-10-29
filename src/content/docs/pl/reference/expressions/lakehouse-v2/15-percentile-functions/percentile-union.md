---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION — zwraca sumę wielu stanów percentyla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

Zwraca sumę wielu stanów percentyla.

## Składnia Analyze

```python
func.percentile_union(<state>)
```

## Przykłady Analyze

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## Składnia SQL

```sql
PERCENTILE_UNION(<state>)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
