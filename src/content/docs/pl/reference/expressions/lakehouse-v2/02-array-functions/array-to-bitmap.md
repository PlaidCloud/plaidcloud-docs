---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP — konwertuje tablicę liczb całkowitych na bitmapę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

Konwertuje tablicę liczb całkowitych na bitmapę.

## Składnia Analyze

```python
func.array_to_bitmap([1, 2, 3])
```

## Przykłady Analyze

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
