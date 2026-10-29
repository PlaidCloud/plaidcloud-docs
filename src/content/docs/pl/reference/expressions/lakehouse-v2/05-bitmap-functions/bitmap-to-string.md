---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING — konwertuje bitmapę na ciąg wartości oddzielonych przecinkami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

Konwertuje bitmapę na ciąg wartości oddzielonych przecinkami.

## Składnia Analyze

```python
func.bitmap_to_string(<bitmap>)
```

## Przykłady Analyze

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## Składnia SQL

```sql
BITMAP_TO_STRING(<bitmap>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
