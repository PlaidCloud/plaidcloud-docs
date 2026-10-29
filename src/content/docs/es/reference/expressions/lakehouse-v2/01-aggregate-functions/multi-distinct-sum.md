---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM — devuelve la suma de los valores distintos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

Devuelve la suma de los valores distintos.

## Sintaxis de Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Ejemplos de Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## Sintaxis de SQL

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## Ejemplos de SQL

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
