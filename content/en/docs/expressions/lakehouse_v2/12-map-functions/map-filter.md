---
title: MAP_FILTER
---

Filters key-value pairs in a map using a lambda expression.

## Analyze Syntax

```python
func.map_filter(get_column(table, 'map_col'), lambda k, v: v > 1)
```

## Analyze Examples

```python
func.map_filter(MAP{'a':1,'b':2,'c':3}, lambda k,v: v>1)

┌───────────────┐
│ {'b':2,'c':3} │
└───────────────┘
```

## SQL Syntax

```sql
MAP_FILTER(<map_col>, lambda k, v: v > 1)
```

## SQL Examples

```sql
SELECT MAP_FILTER((k, v) -> v > 1, MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ {"b":2,"c":3} │
└───────────────┘
```
