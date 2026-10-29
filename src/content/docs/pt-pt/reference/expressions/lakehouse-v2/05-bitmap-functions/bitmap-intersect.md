---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT — devolve a interseção de um conjunto de bitmaps (agregação).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

Devolve a interseção de um conjunto de bitmaps (agregação).

## Sintaxe do Analyze

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Exemplos do Analyze

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_INTERSECT(<bm>)
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
