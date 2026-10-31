---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION — devolve a união de vários estados de percentil.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

Devolve a união de vários estados de percentil.

## Sintaxe de Analyze

```python
func.percentile_union(<state>)
```

## Exemplos de Analyze

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## Sintaxe SQL

```sql
PERCENTILE_UNION(<state>)
```

## Exemplos SQL

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
