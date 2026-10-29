---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION — renvoie l'union d'un ensemble de bitmaps (agrégation).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

Renvoie l'union d'un ensemble de bitmaps (agrégation).

## Syntaxe Analyze

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Exemples Analyze

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_UNION(<bm>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
