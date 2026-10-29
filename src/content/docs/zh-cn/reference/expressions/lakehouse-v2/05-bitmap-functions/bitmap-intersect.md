---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT：返回一组位图的交集（聚合函数）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

返回一组位图的交集（聚合函数）。

## Analyze 语法

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Analyze 示例

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_INTERSECT(<bm>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
