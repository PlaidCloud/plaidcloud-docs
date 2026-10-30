---
title: BITMAP_XOR (Lakehouse v2)
description: BITMAP_XOR — devuelve la diferencia simétrica de dos mapas de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-xor.md
---

Devuelve la diferencia simétrica de dos mapas de bits.

## Sintaxis de Analyze

```python
func.bitmap_xor(<bm1>, <bm2>)
```

## Ejemplos de Analyze

```python
func.bitmap_xor(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_XOR(<bm1>, <bm2>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_XOR(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3,4')));

┌─────┐
│ 1,4 │
└─────┘
```
