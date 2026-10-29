---
title: GROUPING (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 GROUPING 聚合函数。指示 GROUP BY 子句中的指定列是否已聚合，已聚合时返回 1。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

指示 GROUP BY 子句中的指定列是否已聚合。已聚合时返回 1，否则返回 0。

## Analyze 语法

```python
func.grouping(get_column(table, 'department'))
```

## Analyze 示例

```python
func.grouping(get_column(table, 'department'))
```

## SQL 语法

```sql
GROUPING(<department>)
```

## SQL 示例

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
