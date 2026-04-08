---
title: BITMAP_MAX
description: "Learn how to use the BITMAP_MAX bitmap function in PlaidCloud Lakehouse. Returns the maximum value in a bitmap - see syntax, examples, and output."
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
