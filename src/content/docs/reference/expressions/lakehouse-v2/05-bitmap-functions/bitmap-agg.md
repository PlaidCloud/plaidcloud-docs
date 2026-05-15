---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG — aggregates integer values into a bitmap.
---

Aggregates integer values into a bitmap.

## Analyze Syntax

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze Examples

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_AGG(<id>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
