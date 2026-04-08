---
title: BITMAP_AGG
description: "Learn how to use the BITMAP_AGG bitmap function in PlaidCloud Lakehouse. Aggregates integer values into a bitmap - see syntax, examples, and output."
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
