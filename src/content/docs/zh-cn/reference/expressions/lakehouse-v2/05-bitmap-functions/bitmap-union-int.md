---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT：返回不同整数值的个数（聚合函数）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

返回不同整数值的个数（聚合函数）。

## Analyze 语法

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Analyze 示例

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## SQL 语法

```sql
BITMAP_UNION_INT(<id>)
```

## SQL 示例

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
