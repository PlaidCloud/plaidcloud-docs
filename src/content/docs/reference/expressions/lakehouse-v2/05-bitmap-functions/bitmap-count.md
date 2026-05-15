---
title: BITMAP_COUNT
description: BITMAP_COUNT — returns the number of set bits in a bitmap - see syntax, examples, and output.
---

Returns the number of set bits in a bitmap.

## Analyze Syntax

```python
func.bitmap_count(<bitmap>)
```

## Analyze Examples

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## SQL Syntax

```sql
BITMAP_COUNT(<bitmap>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
