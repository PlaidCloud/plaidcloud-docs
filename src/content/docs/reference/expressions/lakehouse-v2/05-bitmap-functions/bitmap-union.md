---
title: BITMAP_UNION
description: BITMAP_UNION — Returns the union of a set of bitmaps (aggregate).
---

Returns the union of a set of bitmaps (aggregate).

## Analyze Syntax

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Analyze Examples

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_UNION(<bm>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
