---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX — devuelve el valor máximo de un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-max.md
---

Devuelve el valor máximo de un mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_max(<bitmap>)
```

## Ejemplos de Analyze

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## Sintaxis de SQL

```sql
BITMAP_MAX(<bitmap>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
