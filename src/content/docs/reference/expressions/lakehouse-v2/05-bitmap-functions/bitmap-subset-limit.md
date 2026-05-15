---
title: BITMAP_SUBSET_LIMIT
description: BITMAP_SUBSET_LIMIT — returns a subset of a bitmap starting from an offset with a cardinality limit.
---

Returns a subset of a bitmap starting from an offset with a cardinality limit.

## Analyze Syntax

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Analyze Examples

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
