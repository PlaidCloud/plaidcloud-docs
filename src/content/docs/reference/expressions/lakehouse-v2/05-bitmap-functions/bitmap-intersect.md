---
title: BITMAP_INTERSECT
description: BITMAP_INTERSECT — returns the intersection of a set of bitmaps (aggregate).
---

Returns the intersection of a set of bitmaps (aggregate).

## Analyze Syntax

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Analyze Examples

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_INTERSECT(<bm>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
