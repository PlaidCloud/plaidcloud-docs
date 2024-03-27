---
title: ARRAY_REMOVE_LAST
---

Removes the last element from the array.

## SQL Syntax

```sql
ARRAY_REMOVE_LAST( <array> )
```

## SQL Examples

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```