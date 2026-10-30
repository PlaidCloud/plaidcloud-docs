---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID：返回与列分组对应的位掩码。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

返回与列分组对应的位掩码。

## Analyze 语法

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Analyze 示例

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## SQL 语法

```sql
GROUPING_ID(<a>, <b>)
```

## SQL 示例

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
