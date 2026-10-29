---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND — devuelve la intersección de dos mapas de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

Devuelve la intersección de dos mapas de bits.

## Sintaxis de Analyze

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Ejemplos de Analyze

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
