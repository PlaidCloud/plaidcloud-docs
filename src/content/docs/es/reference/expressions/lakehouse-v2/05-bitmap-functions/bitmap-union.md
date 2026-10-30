---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION — devuelve la unión de un conjunto de mapas de bits (agregación).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

Devuelve la unión de un conjunto de mapas de bits (agregación).

## Sintaxis de Analyze

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Ejemplos de Analyze

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_UNION(<bm>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
