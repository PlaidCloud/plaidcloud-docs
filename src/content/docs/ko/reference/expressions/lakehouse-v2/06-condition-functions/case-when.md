---
title: CASE (Lakehouse v2)
description: CASE — 조건을 평가하여 첫 번째로 충족되는 조건의 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/case-when.md
---

조건을 평가하여 첫 번째로 충족되는 조건의 값을 반환합니다.

## Analyze 구문

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Analyze 예제

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## SQL 구문

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## SQL 예제

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
