---
title: BITMAP_FROM_BINARY (Lakehouse v2)
description: BITMAP_FROM_BINARY — konwertuje wartość binarną na bitmapę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-binary.md
---

Konwertuje wartość binarną na bitmapę.

## Składnia Analyze

```python
func.bitmap_from_binary(<binary>)
```

## Przykłady Analyze

```python
func.bitmap_from_binary(get_column(table, 'bin_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_FROM_BINARY(<binary>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_BINARY(bm_binary)) FROM data;

┌───┐
│ 5 │
└───┘
```
