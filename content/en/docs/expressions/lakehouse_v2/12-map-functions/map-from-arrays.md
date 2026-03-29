---
title: MAP_FROM_ARRAYS
---

Creates a map from an array of keys and an array of values.

## Analyze Syntax

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Analyze Examples

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## SQL Syntax

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## SQL Examples

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
