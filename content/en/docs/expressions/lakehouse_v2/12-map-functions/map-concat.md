---
title: MAP_CONCAT
---

Concatenates multiple maps into a single map.

## Analyze Syntax

```python
func.map_concat(map1, map2)
```

## Analyze Examples

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## SQL Syntax

```sql
MAP_CONCAT(map1, map2)
```

## SQL Examples

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
