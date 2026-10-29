---
title: GROUPING (Lakehouse v2)
description: "Use la función de agregación GROUPING en PlaidCloud Lakehouse. Indica si una columna especificada de una cláusula GROUP BY está agregada. Devuelve 1 si está agregada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

Indica si una columna especificada de una cláusula GROUP BY está agregada. Devuelve 1 si está agregada y 0 en caso contrario.

## Sintaxis de Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Ejemplos de Analyze

```python
func.grouping(get_column(table, 'department'))
```

## Sintaxis de SQL

```sql
GROUPING(<department>)
```

## Ejemplos de SQL

```sql
SELECT department, GROUPING(department), SUM(salary)
FROM employees GROUP BY ROLLUP(department);

┌────────────┬───────────────────────┬─────────────┐
│ department │ grouping(department)  │ sum(salary)  │
├────────────┼───────────────────────┼─────────────┤
│ Sales      │                     0 │      195000 │
│ IT         │                     0 │      246000 │
│ NULL       │                     1 │      441000 │
└────────────┴───────────────────────┴─────────────┘
```
