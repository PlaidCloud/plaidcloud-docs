---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "Utilize a função de percentil PERCENTILE_APPROX_RAW no PlaidCloud Lakehouse. Devolve um valor de percentil aproximado a partir de um estado de percentil pré-calculado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

Devolve um valor de percentil aproximado a partir de um estado de percentil pré-calculado.

## Sintaxe de Analyze

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
