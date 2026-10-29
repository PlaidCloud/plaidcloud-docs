---
title: PERCENTILE_APPROX_WEIGHT (Lakehouse v2)
description: PERCENTILE_APPROX_WEIGHT — retorna um valor de percentil aproximado ponderado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx-weight.md
---

Retorna um valor de percentil aproximado ponderado.

## Sintaxe do Analyze

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)
```

## Exemplos do Analyze

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)

┌──────┐
│ 72.5 │
└──────┘
```

## Sintaxe SQL

```sql
PERCENTILE_APPROX_WEIGHT(<val>, <weight>, 0.5)
```

## Exemplos SQL

```sql
SELECT PERCENTILE_APPROX_WEIGHT(val, weight, 0.5) FROM data;

┌──────┐
│ 72.5 │
└──────┘
```
