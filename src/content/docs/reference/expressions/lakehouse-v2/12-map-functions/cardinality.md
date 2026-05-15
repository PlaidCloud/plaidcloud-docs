---
title: "CARDINALITY (Map, Lakehouse v2)"
description: CARDINALITY — returns the number of key-value pairs in a map.
---

Returns the number of key-value pairs in a map.

## Analyze Syntax

```python
func.cardinality(get_column(table, 'map_col'))
```

## Analyze Examples

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL Syntax

```sql
CARDINALITY(<map_col>)
```

## SQL Examples

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
