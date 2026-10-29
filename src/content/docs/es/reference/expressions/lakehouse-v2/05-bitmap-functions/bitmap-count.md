---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT — devuelve el número de bits activados de un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

Devuelve el número de bits activados de un mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_count(<bitmap>)
```

## Ejemplos de Analyze

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## Sintaxis de SQL

```sql
BITMAP_COUNT(<bitmap>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
