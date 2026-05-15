---
title: MAP_APPLY
description: MAP_APPLY — Applies a lambda expression to each key-value pair in a map.
---

Applies a lambda expression to each key-value pair in a map.

## Analyze Syntax

```python
func.map_apply(get_column(table, 'map_col'), lambda k, v: (k, v*2))
```

## Analyze Examples

```python
func.map_apply(MAP{'a':1,'b':2}, lambda k,v: (k, v*2))

┌───────────────┐
│ {'a':2,'b':4} │
└───────────────┘
```

## SQL Syntax

```sql
MAP_APPLY(<map_col>, lambda k, v: (k, v*2))
```

## SQL Examples

```sql
SELECT MAP_APPLY((k, v) -> (k, v * 2), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"a":2,"b":4} │
└───────────────┘
```
