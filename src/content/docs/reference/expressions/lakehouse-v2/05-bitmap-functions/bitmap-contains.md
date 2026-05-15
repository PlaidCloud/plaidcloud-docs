---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS — Checks whether a bitmap contains a specific value.
---

Checks whether a bitmap contains a specific value.

## Analyze Syntax

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Analyze Examples

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## SQL Examples

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
