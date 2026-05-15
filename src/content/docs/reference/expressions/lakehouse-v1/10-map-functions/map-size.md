---
title: MAP_SIZE (Lakehouse v1)
description: MAP_SIZE — returns the size of a MAP.
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
