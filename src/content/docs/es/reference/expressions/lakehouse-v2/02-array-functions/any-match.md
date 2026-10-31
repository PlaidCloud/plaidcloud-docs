---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH — devuelve TRUE si algún elemento de una matriz cumple el predicado indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

Devuelve TRUE si algún elemento de una matriz cumple el predicado indicado.

## Sintaxis de Analyze

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Ejemplos de Analyze

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## Ejemplos de SQL

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
