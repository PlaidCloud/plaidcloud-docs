---
title: MAP_VALUES (Lakehouse v1)
description: MAP_VALUES — returns the values in a map.
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
