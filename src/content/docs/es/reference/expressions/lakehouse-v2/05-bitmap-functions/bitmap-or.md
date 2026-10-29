---
title: BITMAP_OR (Lakehouse v2)
description: BITMAP_OR — devuelve la unión de dos mapas de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-or.md
---

Devuelve la unión de dos mapas de bits.

## Sintaxis de Analyze

```python
func.bitmap_or(<bm1>, <bm2>)
```

## Ejemplos de Analyze

```python
func.bitmap_or(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_OR(<bm1>, <bm2>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_OR(
  BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3')));

┌───────┐
│ 1,2,3 │
└───────┘
```
