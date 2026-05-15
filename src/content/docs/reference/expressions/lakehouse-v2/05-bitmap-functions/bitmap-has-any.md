---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY — Checks whether two bitmaps have any common elements.
---

Checks whether two bitmaps have any common elements.

## Analyze Syntax

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Analyze Examples

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## SQL Examples

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```
