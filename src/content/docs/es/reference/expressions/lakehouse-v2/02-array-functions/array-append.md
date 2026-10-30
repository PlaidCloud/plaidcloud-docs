---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND — agrega un elemento al final de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

Agrega un elemento al final de una matriz.

## Sintaxis de Analyze

```python
func.array_append([1, 2, 3], 4)
```

## Ejemplos de Analyze

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Sintaxis de SQL

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
