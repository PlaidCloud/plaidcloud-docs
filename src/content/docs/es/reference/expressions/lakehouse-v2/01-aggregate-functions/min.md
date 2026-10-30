---
title: MIN (Lakehouse v2)
description: MIN — devuelve el valor mínimo de un conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

Devuelve el valor mínimo de un conjunto de valores.

## Sintaxis de Analyze

```python
func.min(get_column(table, 'salary'))
```

## Ejemplos de Analyze

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## Sintaxis de SQL

```sql
MIN(<salary>)
```

## Ejemplos de SQL

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
