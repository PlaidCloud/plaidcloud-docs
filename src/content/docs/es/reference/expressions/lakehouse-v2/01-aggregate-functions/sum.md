---
title: SUM (Lakehouse v2)
description: SUM — devuelve la suma de todos los valores de un grupo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

Devuelve la suma de todos los valores de un grupo.

## Sintaxis de Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Ejemplos de Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Sintaxis de SQL

```sql
SUM(<amount>)
```

## Ejemplos de SQL

```sql
SELECT department, SUM(salary) FROM employees GROUP BY department;

┌────────────┬─────────────┐
│ department │ sum(salary) │
├────────────┼─────────────┤
│ Sales      │      195000 │
│ IT         │      246000 │
│ HR         │      210000 │
└────────────┴─────────────┘
```
