---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT：返回一组位图并集中不同值的个数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

返回一组位图并集中不同值的个数。

## Analyze 语法

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Analyze 示例

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## SQL 语法

```sql
BITMAP_UNION_COUNT(<bm>)
```

## SQL 示例

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
