---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP — convierte una matriz de enteros en un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

Convierte una matriz de enteros en un mapa de bits.

## Sintaxis de Analyze

```python
func.array_to_bitmap([1, 2, 3])
```

## Ejemplos de Analyze

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
