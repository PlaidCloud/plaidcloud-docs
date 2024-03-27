---
title: GREATEST
---

Returns the maximum value from a set of values.

## SQL Syntax

```sql
GREATEST(<value1>, <value2> ...)
```

## SQL Examples

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```