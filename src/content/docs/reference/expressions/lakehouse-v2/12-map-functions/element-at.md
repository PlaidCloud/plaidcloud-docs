---
title: ELEMENT_AT
description: "Learn how to use the ELEMENT_AT map function in PlaidCloud Lakehouse. Returns the value associated with a specified key in a map - with syntax and examples."
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
