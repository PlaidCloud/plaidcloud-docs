---
title: DS_HLL_COUNT_DISTINCT (Lakehouse v2)
description: "Use la función de agregación DS_HLL_COUNT_DISTINCT en PlaidCloud Lakehouse. Devuelve un recuento aproximado de valores distintos mediante el algoritmo HLL de DataSketches. Más precisa que APPROX_COUNT_DISTINCT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-count-distinct.md
---

Devuelve un recuento aproximado de valores distintos mediante el algoritmo HLL de DataSketches. Es más precisa que `APPROX_COUNT_DISTINCT`.

## Sintaxis de Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Ejemplos de Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## Sintaxis de SQL

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## Ejemplos de SQL

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
