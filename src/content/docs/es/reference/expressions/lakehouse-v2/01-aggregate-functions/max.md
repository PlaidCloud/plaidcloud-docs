---
title: MAX (Lakehouse v2)
description: MAX — devuelve el valor máximo de un conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

Devuelve el valor máximo de un conjunto de valores.

## Sintaxis de Analyze

```python
func.max(get_column(table, 'salary'))
```

## Ejemplos de Analyze

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## Sintaxis de SQL

```sql
MAX(<salary>)
```

## Ejemplos de SQL

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
