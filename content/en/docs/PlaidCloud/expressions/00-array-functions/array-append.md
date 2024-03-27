---
title: ARRAY_APPEND
---

Prepends an element to the array.

## SQL Syntax

```sql
ARRAY_APPEND( <array>, <element>)
```

## SQL Examples

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```