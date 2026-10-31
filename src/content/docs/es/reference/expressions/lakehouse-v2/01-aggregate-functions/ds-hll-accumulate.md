---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "Use la función de agregación DS_HLL_ACCUMULATE en PlaidCloud Lakehouse. Acumula valores en un esbozo HLL de DataSketches para el recuento aproximado de valores distintos."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

Acumula valores en un esbozo HLL de DataSketches para el recuento aproximado de valores distintos.

## Sintaxis de Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Ejemplos de Analyze

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## Sintaxis de SQL

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## Ejemplos de SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
