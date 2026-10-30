---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT — zwraca liczbę ustawionych bitów w bitmapie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

Zwraca liczbę ustawionych bitów w bitmapie.

## Składnia Analyze

```python
func.bitmap_count(<bitmap>)
```

## Przykłady Analyze

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## Składnia SQL

```sql
BITMAP_COUNT(<bitmap>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
