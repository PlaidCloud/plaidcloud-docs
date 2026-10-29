---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT — ビットマップの集合の積集合を返します（集計）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

ビットマップの集合の積集合を返します（集計）。

## Analyzeの構文

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Analyzeの例

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_INTERSECT(<bm>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
