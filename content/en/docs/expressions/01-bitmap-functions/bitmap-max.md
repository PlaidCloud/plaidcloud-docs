---
title: BITMAP_MAX
---

Gets the maximum value in the bitmap.

## Analyze Syntax

```python
func.bitmap_max( <bitmap> )
```

## Analyze Examples

```python
func.bitmap_max(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_max(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             5 │
└───────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_MAX( <bitmap> )
```

## SQL Examples

```sql
SELECT BITMAP_MAX(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_max(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   5 │
└─────────────────────────────────────┘
```