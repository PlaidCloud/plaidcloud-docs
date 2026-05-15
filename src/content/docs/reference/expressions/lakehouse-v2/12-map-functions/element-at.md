---
title: "ELEMENT_AT (Map, Lakehouse v2)"
description: ELEMENT_AT — Returns the value associated with a specified key in a map.
---

Returns the value associated with a specified key in a map.

## Analyze Syntax

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Analyze Examples

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## SQL Syntax

```sql
ELEMENT_AT(<map_col>, 'key')
```

## SQL Examples

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
