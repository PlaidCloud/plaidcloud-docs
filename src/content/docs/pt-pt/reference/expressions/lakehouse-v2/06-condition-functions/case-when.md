---
title: CASE (Lakehouse v2)
description: CASE — avalia condições e devolve um valor quando a primeira condição é satisfeita.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/case-when.md
---

Avalia condições e devolve um valor quando a primeira condição é satisfeita.

## Sintaxe do Analyze

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Exemplos do Analyze

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## Sintaxe SQL

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## Exemplos SQL

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
