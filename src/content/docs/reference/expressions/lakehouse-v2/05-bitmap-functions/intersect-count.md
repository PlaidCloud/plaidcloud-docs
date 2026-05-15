---
title: INTERSECT_COUNT (Lakehouse v2)
description: "Use the INTERSECT_COUNT bitmap function in PlaidCloud Lakehouse. Returns the count of elements in the intersection of multiple bitmaps filtered by dimension."
---

Returns the count of elements in the intersection of multiple bitmaps filtered by dimension.

## Analyze Syntax

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Analyze Examples

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## SQL Syntax

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## SQL Examples

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
