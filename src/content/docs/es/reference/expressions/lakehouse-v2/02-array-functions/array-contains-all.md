---
title: ARRAY_CONTAINS_ALL (Lakehouse v2)
description: ARRAY_CONTAINS_ALL — comprueba si una matriz contiene todos los elementos de otra matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-all.md
---

Comprueba si una matriz contiene todos los elementos de otra matriz.

## Sintaxis de Analyze

```python
func.array_contains_all([1,2,3], [1,2])
```

## Ejemplos de Analyze

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```
