---
title: ARRAY_SORTBY
description: "Learn how to use the ARRAY_SORTBY array function in PlaidCloud Lakehouse. Sorts elements of one array by corresponding elements of another array."
---

Sorts elements of one array by corresponding elements of another array.

## Analyze Syntax

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Analyze Examples

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL Syntax

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## SQL Examples

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
