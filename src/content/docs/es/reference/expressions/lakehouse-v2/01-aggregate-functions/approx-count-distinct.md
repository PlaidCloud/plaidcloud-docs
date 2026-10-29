---
title: APPROX_COUNT_DISTINCT (Lakehouse v2)
description: APPROX_COUNT_DISTINCT devuelve un recuento aproximado de valores distintos mediante HyperLogLog.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

Devuelve un recuento aproximado de valores distintos mediante HyperLogLog.

## Sintaxis de Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Ejemplos de Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## Sintaxis de SQL

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## Ejemplos de SQL

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
