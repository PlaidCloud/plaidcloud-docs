---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION — devuelve la unión de varios estados de percentil.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

Devuelve la unión de varios estados de percentil.

## Sintaxis de Analyze

```python
func.percentile_union(<state>)
```

## Ejemplos de Analyze

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_UNION(<state>)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
