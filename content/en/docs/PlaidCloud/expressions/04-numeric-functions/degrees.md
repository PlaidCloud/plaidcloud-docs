---
title: DEGREES
---

Returns the argument `x`, converted from radians to degrees, where `x` is given in radians.

## SQL Syntax

```sql
DEGREES( <x> )
```

## SQL Examples

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```