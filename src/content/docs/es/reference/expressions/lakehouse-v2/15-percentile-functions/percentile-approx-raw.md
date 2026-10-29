---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "Use la función de percentil PERCENTILE_APPROX_RAW en PlaidCloud Lakehouse. Devuelve un valor de percentil aproximado a partir de un estado de percentil precalculado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

Devuelve un valor de percentil aproximado a partir de un estado de percentil precalculado.

## Sintaxis de Analyze

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Ejemplos de Analyze

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
