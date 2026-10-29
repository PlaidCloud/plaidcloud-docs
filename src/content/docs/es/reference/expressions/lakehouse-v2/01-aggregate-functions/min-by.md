---
title: MIN_BY (Lakehouse v2)
description: MIN_BY — devuelve el valor de una columna asociado al valor mínimo de otra columna.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min-by.md
---

Devuelve el valor de una columna asociado al valor mínimo de otra columna.

## Sintaxis de Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Ejemplos de Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## Sintaxis de SQL

```sql
MIN_BY(<name>, <salary>)
```

## Ejemplos de SQL

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
