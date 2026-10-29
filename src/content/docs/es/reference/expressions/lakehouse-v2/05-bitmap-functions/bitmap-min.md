---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN — devuelve el valor mínimo de un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

Devuelve el valor mínimo de un mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_min(<bitmap>)
```

## Ejemplos de Analyze

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
BITMAP_MIN(<bitmap>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
