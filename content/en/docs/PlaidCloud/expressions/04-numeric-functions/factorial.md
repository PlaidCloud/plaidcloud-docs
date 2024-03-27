---
title: FACTORIAL
---

Returns the factorial logarithm of `x`. If `x` is less than or equal to 0, the function returns 0.

## SQL Syntax

```sql
FACTORIAL( <x> )
```

## SQL Examples

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```