---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "Use a função de percentil PERCENTILE_APPROX_RAW no PlaidCloud Lakehouse. Retorna um valor de percentil aproximado a partir de um estado de percentil pré-calculado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

Retorna um valor de percentil aproximado a partir de um estado de percentil pré-calculado.

## Sintaxe do Analyze

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Exemplos do Analyze

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## Sintaxe SQL

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## Exemplos de SQL

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
