---
title: BITMAP_ANDNOT
---

Returns the difference of two bitmaps (elements in first but not second).

## Analyze Syntax

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Analyze Examples

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
