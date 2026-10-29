---
title: BITMAP_FROM_STRING (Lakehouse v2)
description: BITMAP_FROM_STRING — convierte una cadena de enteros separados por comas en un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-string.md
---

Convierte una cadena de enteros separados por comas en un mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_from_string(<str>)
```

## Ejemplos de Analyze

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_FROM_STRING(<str>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
