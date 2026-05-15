---
title: BITMAP_TO_ARRAY (Lakehouse v2)
description: BITMAP_TO_ARRAY — converts a bitmap to an array of integers.
---

Converts a bitmap to an array of integers.

## Analyze Syntax

```python
func.bitmap_to_array(<bitmap>)
```

## Analyze Examples

```python
func.bitmap_to_array(get_column(table, 'bm'))

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQL Syntax

```sql
BITMAP_TO_ARRAY(<bitmap>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_ARRAY(BITMAP_FROM_STRING('1,2,3'));

┌─────────┐
│ [1,2,3] │
└─────────┘
```
