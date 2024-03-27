---
title: SIGN
---

Returns the sign of the argument as -1, 0, or 1, depending on whether `x` is negative, zero, or positive or NULL if the argument was NULL.

## SQL Syntax

```sql
SIGN( <x> )
```

## SQL Examples

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```