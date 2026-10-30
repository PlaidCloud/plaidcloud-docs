---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH — devuelve TRUE si todos los elementos de una matriz cumplen el predicado indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

Devuelve TRUE si todos los elementos de una matriz cumplen el predicado indicado.

## Sintaxis de Analyze

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Ejemplos de Analyze

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## Ejemplos de SQL

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
