---
title: BITMAP_REMOVE
description: "Learn how to use the BITMAP_REMOVE bitmap function in PlaidCloud Lakehouse. Removes a specific value from a bitmap - see syntax, examples, and output."
---

Removes a specific value from a bitmap.

## Analyze Syntax

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Analyze Examples

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
