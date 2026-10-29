---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE devuelve cualquier valor arbitrario de un grupo de filas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

Devuelve cualquier valor arbitrario de un grupo de filas.

## Sintaxis de Analyze

```python
func.any_value(get_column(table, 'department'))
```

## Ejemplos de Analyze

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## Sintaxis de SQL

```sql
ANY_VALUE(<department>)
```

## Ejemplos de SQL

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
