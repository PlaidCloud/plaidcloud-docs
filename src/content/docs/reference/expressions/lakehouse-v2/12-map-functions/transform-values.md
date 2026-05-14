---
title: TRANSFORM_VALUES
description: "Learn how to use the TRANSFORM_VALUES map function in PlaidCloud Lakehouse. Applies a lambda expression to transform the values of a map."
---

Applies a lambda expression to transform the values of a map.

## Analyze Syntax

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Analyze Examples

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL Syntax

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## SQL Examples

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
