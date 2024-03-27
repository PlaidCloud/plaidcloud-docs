---
title: ARRAY_PREPEND
---

Prepends an element to the array.

## SQL Syntax

```sql
ARRAY_PREPEND( <element>, <array> )
```

## SQL Examples

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```