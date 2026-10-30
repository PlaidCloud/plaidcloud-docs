---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT — ビットマップの集合の和集合に含まれる、重複を除いた値の数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

ビットマップの集合の和集合に含まれる、重複を除いた値の数を返します。

## Analyzeの構文

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Analyzeの例

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## SQLの構文

```sql
BITMAP_UNION_COUNT(<bm>)
```

## SQLの例

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
