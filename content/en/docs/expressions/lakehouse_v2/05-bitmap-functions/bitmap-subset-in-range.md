---
title: BITMAP_SUBSET_IN_RANGE
---

Returns a subset of a bitmap within a specified range.

## Analyze Syntax

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Analyze Examples

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
