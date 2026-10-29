---
title: BITMAP_FROM_STRING (Lakehouse v2)
description: BITMAP_FROM_STRING — konwertuje ciąg liczb całkowitych oddzielonych przecinkami na bitmapę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-string.md
---

Konwertuje ciąg liczb całkowitych oddzielonych przecinkami na bitmapę.

## Składnia Analyze

```python
func.bitmap_from_string(<str>)
```

## Przykłady Analyze

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_FROM_STRING(<str>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
