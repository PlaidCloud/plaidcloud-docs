---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT — zwraca liczbę różnych wartości w sumie zbioru bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

Zwraca liczbę różnych wartości w sumie zbioru bitmap.

## Składnia Analyze

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Przykłady Analyze

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## Składnia SQL

```sql
BITMAP_UNION_COUNT(<bm>)
```

## Przykłady SQL

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
