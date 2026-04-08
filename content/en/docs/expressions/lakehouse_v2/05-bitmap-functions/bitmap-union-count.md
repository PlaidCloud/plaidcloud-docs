---
title: BITMAP_UNION_COUNT
description: "Learn how to use the BITMAP_UNION_COUNT bitmap function in PlaidCloud Lakehouse. Returns the count of distinct values in the union of a set of bitmaps."
---

Returns the count of distinct values in the union of a set of bitmaps.

## Analyze Syntax

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Analyze Examples

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## SQL Syntax

```sql
BITMAP_UNION_COUNT(<bm>)
```

## SQL Examples

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
