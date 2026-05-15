---
title: BITMAP_TO_STRING
description: BITMAP_TO_STRING — Converts a bitmap to a comma-separated string.
---

Converts a bitmap to a comma-separated string.

## Analyze Syntax

```python
func.bitmap_to_string(<bitmap>)
```

## Analyze Examples

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## SQL Syntax

```sql
BITMAP_TO_STRING(<bitmap>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
