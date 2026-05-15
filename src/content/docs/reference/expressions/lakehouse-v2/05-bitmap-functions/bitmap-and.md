---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND — returns the intersection of two bitmaps.
---

Returns the intersection of two bitmaps.

## Analyze Syntax

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Analyze Examples

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
