---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — returns all values from a map as an array.
---

Returns all values from a map as an array.

## Analyze Syntax

```python
func.map_values(get_column(table, 'map_col'))
```

## Analyze Examples

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## SQL Syntax

```sql
MAP_VALUES(<map_col>)
```

## SQL Examples

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
