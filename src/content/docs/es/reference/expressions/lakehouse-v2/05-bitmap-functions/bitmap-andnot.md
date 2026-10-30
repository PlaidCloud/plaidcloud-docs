---
title: BITMAP_ANDNOT (Lakehouse v2)
description: BITMAP_ANDNOT — devuelve la diferencia de dos mapas de bits (elementos del primero que no están en el segundo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-andnot.md
---

Devuelve la diferencia de dos mapas de bits (elementos del primero que no están en el segundo).

## Sintaxis de Analyze

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Ejemplos de Analyze

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
