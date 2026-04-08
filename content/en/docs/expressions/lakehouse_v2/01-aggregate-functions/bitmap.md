---
title: BITMAP
description: "Learn how to use the BITMAP aggregate function in PlaidCloud Lakehouse. Returns a bitmap union of a set of values. Typically used with BITMAP_AGG."
---

Returns a bitmap union of a set of values. Typically used with BITMAP_AGG.

## Analyze Syntax

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze Examples

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP(<id>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
