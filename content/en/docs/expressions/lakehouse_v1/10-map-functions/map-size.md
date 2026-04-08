---
title: MAP_SIZE
description: "Learn how to use the MAP_SIZE map function in PlaidCloud Lakehouse. Returns the size of a MAP. Includes detailed syntax, examples, and usage reference."
---

Returns the size of a MAP.

## SQL Syntax

```sql
MAP_SIZE( <map> )
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<map>`   | The input map. |

## Return Type

UInt64.

## SQL Examples

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
