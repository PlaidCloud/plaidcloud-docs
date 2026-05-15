---
title: CASE
description: CASE — evaluates conditions and returns a value when the first condition is met.
---

Evaluates conditions and returns a value when the first condition is met.

## Analyze Syntax

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Analyze Examples

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## SQL Syntax

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## SQL Examples

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
