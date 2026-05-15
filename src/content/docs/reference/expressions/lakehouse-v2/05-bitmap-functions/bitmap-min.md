---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN — returns the minimum value in a bitmap.
---

Returns the minimum value in a bitmap.

## Analyze Syntax

```python
func.bitmap_min(<bitmap>)
```

## Analyze Examples

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
BITMAP_MIN(<bitmap>)
```

## SQL Examples

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
