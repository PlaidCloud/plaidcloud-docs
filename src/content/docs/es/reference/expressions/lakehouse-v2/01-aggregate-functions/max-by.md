---
title: MAX_BY (Lakehouse v2)
description: MAX_BY — devuelve el valor de una columna asociado al valor máximo de otra columna.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

Devuelve el valor de una columna asociado al valor máximo de otra columna.

## Sintaxis de Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Ejemplos de Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## Sintaxis de SQL

```sql
MAX_BY(<name>, <salary>)
```

## Ejemplos de SQL

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
