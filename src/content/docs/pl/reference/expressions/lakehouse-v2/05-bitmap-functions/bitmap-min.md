---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN — zwraca minimalną wartość w bitmapie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

Zwraca minimalną wartość w bitmapie.

## Składnia Analyze

```python
func.bitmap_min(<bitmap>)
```

## Przykłady Analyze

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
BITMAP_MIN(<bitmap>)
```

## Przykłady SQL

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
