---
title: RANGE
---

Returns an array collected by [start, end).

## SQL Syntax

```sql
RANGE( <start>, <end> )
```

## SQL Examples

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```