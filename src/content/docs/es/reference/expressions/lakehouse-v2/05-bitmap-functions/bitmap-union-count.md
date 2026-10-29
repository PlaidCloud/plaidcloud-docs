---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT — devuelve el número de valores distintos de la unión de un conjunto de mapas de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

Devuelve el número de valores distintos de la unión de un conjunto de mapas de bits.

## Sintaxis de Analyze

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Ejemplos de Analyze

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## Sintaxis de SQL

```sql
BITMAP_UNION_COUNT(<bm>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
