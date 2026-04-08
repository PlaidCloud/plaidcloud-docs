---
title: CARDINALITY
description: "Learn how to use the CARDINALITY map function in PlaidCloud Lakehouse. Returns the number of key-value pairs in a map - see syntax, examples, and output."
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
