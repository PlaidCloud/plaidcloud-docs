---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX — returns the maximum value in a bitmap.
---

Returns the maximum value in a bitmap.

## Analyze Syntax

```python
func.bitmap_max(<bitmap>)
```

## Analyze Examples

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## SQL Syntax

```sql
BITMAP_MAX(<bitmap>)
```

## SQL Examples

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
