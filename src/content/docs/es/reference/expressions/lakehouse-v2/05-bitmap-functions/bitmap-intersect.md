---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT — devuelve la intersección de un conjunto de mapas de bits (agregación).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

Devuelve la intersección de un conjunto de mapas de bits (agregación).

## Sintaxis de Analyze

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Ejemplos de Analyze

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_INTERSECT(<bm>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
