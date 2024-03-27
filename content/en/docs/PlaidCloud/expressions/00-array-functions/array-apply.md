---
title: ARRAY_APPLY
---

Alias for [ARRAY_TRANSFORM](array-transform.md).

## SQL Syntax

```sql
ARRAY_APPLY( <array>, <lambda> )
```

## SQL Examples

```sql
SELECT ARRAY_APPLY([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────┐
│ array_apply([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────┤
│ [2,3,4]                              │
└──────────────────────────────────────┘
```