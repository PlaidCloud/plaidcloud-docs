---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND — zwraca część wspólną dwóch bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

Zwraca część wspólną dwóch bitmap.

## Składnia Analyze

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Przykłady Analyze

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
