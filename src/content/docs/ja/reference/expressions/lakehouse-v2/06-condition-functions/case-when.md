---
title: CASE (Lakehouse v2)
description: CASE — 条件を評価し、最初に満たされた条件に対応する値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/case-when.md
---

条件を評価し、最初に満たされた条件に対応する値を返します。

## Analyzeの構文

```python
case((get_column(table, 'status') == 1, 'Active'), else_='Inactive')
```

## Analyzeの例

```python
case((get_column(table, 'salary') > 100000, 'High'), (get_column(table, 'salary') > 60000, 'Medium'), else_='Low')
```

## SQLの構文

```sql
CASE((<status> == 1, 'Active'), else_='Inactive')
```

## SQLの例

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
