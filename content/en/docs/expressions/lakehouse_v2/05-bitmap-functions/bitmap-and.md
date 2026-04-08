---
title: BITMAP_AND
description: "Learn how to use the BITMAP_AND bitmap function in PlaidCloud Lakehouse. Returns the intersection of two bitmaps - see syntax, examples, and output."
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
