---
title: MAP_SIZE
description: MAP_SIZE — returns the number of key-value pairs in a map - see syntax, examples, and output.
---

Returns the number of key-value pairs in a map.

## Analyze Syntax

```python
func.map_size(get_column(table, 'map_col'))
```

## Analyze Examples

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL Syntax

```sql
MAP_SIZE(<map_col>)
```

## SQL Examples

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
