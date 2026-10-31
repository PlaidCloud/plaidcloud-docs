---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION：返回一组位图的并集（聚合函数）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

返回一组位图的并集（聚合函数）。

## Analyze 语法

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Analyze 示例

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_UNION(<bm>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
