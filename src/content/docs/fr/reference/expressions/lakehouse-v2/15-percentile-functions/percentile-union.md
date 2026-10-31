---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION — renvoie l'union de plusieurs états de centile.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

Renvoie l'union de plusieurs états de centile.

## Syntaxe Analyze

```python
func.percentile_union(<state>)
```

## Exemples Analyze

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## Syntaxe SQL

```sql
PERCENTILE_UNION(<state>)
```

## Exemples SQL

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
