---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY — ordena los elementos de una matriz según los elementos correspondientes de otra matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

Ordena los elementos de una matriz según los elementos correspondientes de otra matriz.

## Sintaxis de Analyze

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Ejemplos de Analyze

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
