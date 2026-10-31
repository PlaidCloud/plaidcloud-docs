---
title: BITMAP_TO_ARRAY (Lakehouse v2)
description: BITMAP_TO_ARRAY — konwertuje bitmapę na tablicę liczb całkowitych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-array.md
---

Konwertuje bitmapę na tablicę liczb całkowitych.

## Składnia Analyze

```python
func.bitmap_to_array(<bitmap>)
```

## Przykłady Analyze

```python
func.bitmap_to_array(get_column(table, 'bm'))

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Składnia SQL

```sql
BITMAP_TO_ARRAY(<bitmap>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_ARRAY(BITMAP_FROM_STRING('1,2,3'));

┌─────────┐
│ [1,2,3] │
└─────────┘
```
