---
title: BITMAP_CONTAINS
---

Checks if the bitmap contains a specific value.

## SQL Syntax

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## SQL Examples

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```