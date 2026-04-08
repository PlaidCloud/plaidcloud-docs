---
title: TRANSFORM_KEYS
description: "Learn how to use the TRANSFORM_KEYS map function in PlaidCloud Lakehouse. Applies a lambda expression to transform the keys of a map - with syntax and examples."
---

Applies a lambda expression to transform the keys of a map.

## Analyze Syntax

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Analyze Examples

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## SQL Syntax

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## SQL Examples

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
