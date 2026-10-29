---
title: GROUPING_ID（Lakehouse v2）
description: GROUPING_ID — 列のグループ化に対応するビットマスクを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

列のグループ化に対応するビットマスクを返します。

## Analyzeの構文

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Analyzeの例

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## SQLの構文

```sql
GROUPING_ID(<a>, <b>)
```

## SQLの例

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
