---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION — zwraca sumę zbioru bitmap (agregat).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

Zwraca sumę zbioru bitmap (agregat).

## Składnia Analyze

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Przykłady Analyze

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_UNION(<bm>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
