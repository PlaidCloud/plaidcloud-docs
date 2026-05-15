---
title: BITMAP_OR (Lakehouse v2)
description: BITMAP_OR — returns the union of two bitmaps.
---

Returns the union of two bitmaps.

## Analyze Syntax

```python
func.bitmap_or(<bm1>, <bm2>)
```

## Analyze Examples

```python
func.bitmap_or(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_OR(<bm1>, <bm2>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_OR(
  BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3')));

┌───────┐
│ 1,2,3 │
└───────┘
```
