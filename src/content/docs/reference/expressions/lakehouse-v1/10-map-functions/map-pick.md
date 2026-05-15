---
title: MAP_PICK (Lakehouse v1)
description: MAP_PICK — returns a new MAP containing the specified key-value pairs from an existing MAP.
---

Returns a new MAP containing the specified key-value pairs from an existing MAP.

## SQL Syntax

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## Arguments

| Arguments | Description                                             |
|-----------|-------------------------------------------------------- |
| `<map>`   | The input MAP.                                          |
| `<keyN>`  | The KEYs to be included from the returned MAP.          |
| `<array>` | The Array of KEYs to be included from the returned MAP. |

:::note
- The types of the key expressions and the keys in the map must be the same.
- Key values not found in the map will be ignored.
:::

## Return Type

Map.

## SQL Examples

```sql
SELECT MAP_PICK({'a':1,'b':2,'c':3}, 'a', 'c');
┌─────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, 'a', 'c') │
├─────────────────────────────────────────┤
│ {'a':1,'c':3}                           │
└─────────────────────────────────────────┘

SELECT MAP_PICK({'a':1,'b':2,'c':3}, ['a', 'b']);
┌───────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, ['a', 'b']) │
├───────────────────────────────────────────┤
│ {'a':1,'b':2}                             │
└───────────────────────────────────────────┘
```
