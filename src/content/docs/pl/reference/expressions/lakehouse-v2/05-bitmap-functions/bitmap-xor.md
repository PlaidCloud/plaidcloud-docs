---
title: BITMAP_XOR (Lakehouse v2)
description: BITMAP_XOR — zwraca różnicę symetryczną dwóch bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-xor.md
---

Zwraca różnicę symetryczną dwóch bitmap.

## Składnia Analyze

```python
func.bitmap_xor(<bm1>, <bm2>)
```

## Przykłady Analyze

```python
func.bitmap_xor(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_XOR(<bm1>, <bm2>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_XOR(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3,4')));

┌─────┐
│ 1,4 │
└─────┘
```
