---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ — comprueba si una matriz contiene todos los elementos de otra matriz en el mismo orden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

Comprueba si una matriz contiene todos los elementos de otra matriz en el mismo orden.

## Sintaxis de Analyze

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Ejemplos de Analyze

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```
