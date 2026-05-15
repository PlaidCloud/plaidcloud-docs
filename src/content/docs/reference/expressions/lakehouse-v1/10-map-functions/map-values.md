---
title: MAP_VALUES
description: MAP_VALUES — returns the values in a map. Includes detailed syntax, examples, and usage reference.
---

Returns the values in a map.

## SQL Syntax

```sql
MAP_VALUES( <map> )
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<map>`   | The input map. |

## Return Type

Array.

## SQL Examples

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
