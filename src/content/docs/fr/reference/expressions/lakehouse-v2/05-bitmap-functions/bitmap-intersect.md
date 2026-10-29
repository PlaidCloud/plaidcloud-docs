---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT — renvoie l'intersection d'un ensemble de bitmaps (agrégation).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

Renvoie l'intersection d'un ensemble de bitmaps (agrégation).

## Syntaxe Analyze

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Exemples Analyze

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_INTERSECT(<bm>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
