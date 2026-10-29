---
title: CASE (Lakehouse v2)
description: CASE – wertet Bedingungen aus und gibt einen Wert zurück, sobald die erste Bedingung erfüllt ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/case-when.md
---

Wertet Bedingungen aus und gibt einen Wert zurück, sobald die erste Bedingung erfüllt ist.

## Analyze-Syntax

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Analyze-Beispiele

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## SQL-Syntax

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## SQL-Beispiele

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
