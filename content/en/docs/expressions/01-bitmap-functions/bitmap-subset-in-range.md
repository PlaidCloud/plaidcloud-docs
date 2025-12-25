---
title: BITMAP_SUBSET_IN_RANGE
---

Generates a sub-bitmap of the source bitmap within a specified range.

## Analyze Syntax

```python
func.bitmap_subset_in_range( <bitmap>, <start>, <end> )
```

## Analyze Examples

```python
func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9)

┌─────────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9) │
├─────────────────────────────────────────────────────────────────┤
│ 7                                                               │
└─────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_SUBSET_IN_RANGE( <bitmap>, <start>, <end> )
```

## SQL Examples

```sql
SELECT BITMAP_SUBSET_IN_RANGE(BUILD_BITMAP([5,7,9]), 6, 9)::String;

┌───────────────────────────────────────────────────────────────┐
│ bitmap_subset_in_range(build_bitmap([5, 7, 9]), 6, 9)::string │
├───────────────────────────────────────────────────────────────┤
│ 7                                                             │
└───────────────────────────────────────────────────────────────┘
```