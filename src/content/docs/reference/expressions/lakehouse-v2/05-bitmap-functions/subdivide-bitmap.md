---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP — splits a bitmap into multiple sub-bitmaps of a given size.
---

Splits a bitmap into multiple sub-bitmaps of a given size.

## Analyze Syntax

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Analyze Examples

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## SQL Syntax

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
