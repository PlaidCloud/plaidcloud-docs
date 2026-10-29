---
title: INTERSECT_COUNT (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 INTERSECT_COUNT 位图函数。返回按维度筛选的多个位图交集中的元素个数。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

返回按维度筛选的多个位图交集中的元素个数。

## Analyze 语法

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Analyze 示例

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## SQL 语法

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## SQL 示例

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
