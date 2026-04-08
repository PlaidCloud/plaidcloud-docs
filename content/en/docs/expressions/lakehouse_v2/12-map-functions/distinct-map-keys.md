---
title: DISTINCT_MAP_KEYS
description: "Learn how to use the DISTINCT_MAP_KEYS map function in PlaidCloud Lakehouse. Returns the distinct keys from a map - see syntax, examples, and output."
---

Returns the distinct keys from a map.

## Analyze Syntax

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Analyze Examples

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL Syntax

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## SQL Examples

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
