---
title: CASE (Lakehouse v2)
description: CASE：依次评估条件，并在满足第一个条件时返回对应的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/case-when.md
---

依次评估条件，并在满足第一个条件时返回对应的值。

## Analyze 语法

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Analyze 示例

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## SQL 语法

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## SQL 示例

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
