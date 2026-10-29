---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION — ビットマップの集合の和集合を返します（集計）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

ビットマップの集合の和集合を返します（集計）。

## Analyzeの構文

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Analyzeの例

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_UNION(<bm>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
