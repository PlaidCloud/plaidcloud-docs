---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP — converts an array of integers to a bitmap.
---

Converts an array of integers to a bitmap.

## Analyze Syntax

```python
func.array_to_bitmap([1, 2, 3])
```

## Analyze Examples

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
