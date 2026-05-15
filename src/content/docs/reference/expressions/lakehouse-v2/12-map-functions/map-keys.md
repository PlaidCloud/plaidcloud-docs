---
title: MAP_KEYS
description: MAP_KEYS — returns all keys from a map as an array - see syntax, examples, and output.
---

Returns all keys from a map as an array.

## Analyze Syntax

```python
func.map_keys(get_column(table, 'map_col'))
```

## Analyze Examples

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## SQL Syntax

```sql
MAP_KEYS(<map_col>)
```

## SQL Examples

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
