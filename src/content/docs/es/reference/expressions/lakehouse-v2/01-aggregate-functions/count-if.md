---
title: COUNT_IF (Lakehouse v2)
description: COUNT_IF devuelve el número de filas para las que la expresión es TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

Devuelve el número de filas para las que la expresión es TRUE.

## Sintaxis de Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Ejemplos de Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## Sintaxis de SQL

```sql
COUNT_IF(<salary> > 80000)
```

## Ejemplos de SQL

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
