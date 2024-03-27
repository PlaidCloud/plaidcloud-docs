---
title: ARRAY_TRANSFORM
---

Returns an array that is the result of applying the lambda function to each element of the input array.

## SQL Syntax

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## SQL Examples

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```