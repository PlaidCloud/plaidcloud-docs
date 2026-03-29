---
title: BITMAP_XOR
---

Returns the symmetric difference of two bitmaps.

## Analyze Syntax

```python
func.bitmap_xor(<bm1>, <bm2>)
```

## Analyze Examples

```python
func.bitmap_xor(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_XOR(<bm1>, <bm2>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_XOR(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3,4')));

┌─────┐
│ 1,4 │
└─────┘
```
