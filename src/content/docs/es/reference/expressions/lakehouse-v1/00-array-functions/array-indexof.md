---
title: ARRAY_INDEXOF (Lakehouse v1)
description: ARRAY_INDEXOF — devuelve el índice (base 1) de un elemento si el arreglo lo contiene.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

Devuelve el índice (base 1) de un elemento si el arreglo lo contiene.

## Sintaxis de Analyze

```python
func.array_indexof( <array>, <element> )
```

## Ejemplos de Analyze

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```
