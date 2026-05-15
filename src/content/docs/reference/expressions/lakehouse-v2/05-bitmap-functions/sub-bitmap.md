---
title: SUB_BITMAP
description: SUB_BITMAP — returns a sub-bitmap starting from a specified position with a cardinality limit.
---

Returns a sub-bitmap starting from a specified position with a cardinality limit.

## Analyze Syntax

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Analyze Examples

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
