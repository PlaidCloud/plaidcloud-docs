---
title: BITMAP_FROM_STRING
description: "Learn how to use the BITMAP_FROM_STRING bitmap function in PlaidCloud Lakehouse. Converts a comma-separated string of integers to a bitmap."
---

Converts a comma-separated string of integers to a bitmap.

## Analyze Syntax

```python
func.bitmap_from_string(<str>)
```

## Analyze Examples

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_FROM_STRING(<str>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
