---
title: CASE (Lakehouse v2)
description: CASE — évalue des conditions et renvoie une valeur lorsque la première condition est remplie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/case-when.md
---

Évalue des conditions et renvoie une valeur lorsque la première condition est remplie.

## Syntaxe Analyze

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Exemples Analyze

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## Syntaxe SQL

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## Exemples SQL

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
