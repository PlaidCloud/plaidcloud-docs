---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "Use la función de agregación DS_THETA_COUNT_DISTINCT en PlaidCloud Lakehouse. Devuelve un recuento aproximado de valores distintos mediante el algoritmo Theta de DataSketches. Admite operaciones de conjuntos."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

Devuelve un recuento aproximado de valores distintos mediante el algoritmo Theta de DataSketches. Admite operaciones de conjuntos como la intersección y la diferencia.

## Sintaxis de Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Ejemplos de Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## Sintaxis de SQL

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## Ejemplos de SQL

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
