---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "Utilisez la fonction de centile PERCENTILE_APPROX_RAW dans PlaidCloud Lakehouse. Renvoie une valeur de centile approximative à partir d'un état de centile précalculé."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

Renvoie une valeur de centile approximative à partir d'un état de centile précalculé.

## Syntaxe Analyze

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Exemples Analyze

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## Syntaxe SQL

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## Exemples SQL

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
