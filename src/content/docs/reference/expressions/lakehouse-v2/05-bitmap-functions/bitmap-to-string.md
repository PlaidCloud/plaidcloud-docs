---
title: BITMAP_TO_STRING
description: "Learn how to use the BITMAP_TO_STRING bitmap function in PlaidCloud Lakehouse. Converts a bitmap to a comma-separated string - with syntax and examples."
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
