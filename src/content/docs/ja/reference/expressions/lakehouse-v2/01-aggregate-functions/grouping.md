---
title: GROUPING（Lakehouse v2）
description: "PlaidCloud LakehouseでGROUPING集計関数を使用します。GROUP BY句で指定した列が集計されているかどうかを示します。集計されている場合は1を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

GROUP BY句で指定した列が集計されているかどうかを示します。集計されている場合は1、そうでない場合は0を返します。

## Analyzeの構文

```python
func.grouping(get_column(table, 'department'))
```

## Analyzeの例

```python
func.grouping(get_column(table, 'department'))
```

## SQLの構文

```sql
GROUPING(<department>)
```

## SQLの例

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
