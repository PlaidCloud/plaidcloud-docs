---
title: BITMAP_ANDNOT (Lakehouse v2)
description: BITMAP_ANDNOT — zwraca różnicę dwóch bitmap (elementy należące do pierwszej, ale nie do drugiej).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-andnot.md
---

Zwraca różnicę dwóch bitmap (elementy należące do pierwszej, ale nie do drugiej).

## Składnia Analyze

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Przykłady Analyze

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
