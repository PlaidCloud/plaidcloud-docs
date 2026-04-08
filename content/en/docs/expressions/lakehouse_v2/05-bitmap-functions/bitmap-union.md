---
title: BITMAP_UNION
description: "Learn how to use the BITMAP_UNION bitmap function in PlaidCloud Lakehouse. Returns the union of a set of bitmaps (aggregate) - with syntax and examples."
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
