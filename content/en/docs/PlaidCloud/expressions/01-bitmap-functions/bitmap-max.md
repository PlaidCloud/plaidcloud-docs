---
title: BITMAP_MAX
---

Gets the maximum value in the bitmap.

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