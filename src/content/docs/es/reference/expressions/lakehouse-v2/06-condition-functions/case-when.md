---
title: CASE (Lakehouse v2)
description: CASE — evalúa condiciones y devuelve un valor cuando se cumple la primera condición.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/case-when.md
---

Evalúa condiciones y devuelve un valor cuando se cumple la primera condición.

## Sintaxis de Analyze

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Ejemplos de Analyze

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## Sintaxis de SQL

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## Ejemplos de SQL

```sql
SELECT name,
  CASE WHEN salary > 100000 THEN 'High'
       WHEN salary > 60000 THEN 'Medium'
       ELSE 'Low' END AS band
FROM employees;

┌─────────┬────────┐
│ name    │ band   │
├─────────┼────────┤
│ Alice   │ High   │
│ Bob     │ Medium │
│ Charlie │ Low    │
└─────────┴────────┘
```
