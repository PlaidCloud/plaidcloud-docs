---
title: ARRAY_TO_STRING
---

Concatenates elements of an array into a single string, using a specified separator.

## SQL Syntax

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## SQL Examples

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```