---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT — renvoie le nombre de valeurs distinctes dans l'union d'un ensemble de bitmaps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

Renvoie le nombre de valeurs distinctes dans l'union d'un ensemble de bitmaps.

## Syntaxe Analyze

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Exemples Analyze

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## Syntaxe SQL

```sql
BITMAP_UNION_COUNT(<bm>)
```

## Exemples SQL

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
