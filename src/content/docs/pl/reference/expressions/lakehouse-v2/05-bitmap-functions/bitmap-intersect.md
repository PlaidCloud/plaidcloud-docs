---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT — zwraca część wspólną zbioru bitmap (agregat).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

Zwraca część wspólną zbioru bitmap (agregat).

## Składnia Analyze

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Przykłady Analyze

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_INTERSECT(<bm>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
