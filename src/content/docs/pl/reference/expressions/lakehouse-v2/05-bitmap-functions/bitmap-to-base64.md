---
title: BITMAP_TO_BASE64 (Lakehouse v2)
description: BITMAP_TO_BASE64 — konwertuje bitmapę na ciąg zakodowany w base64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-base64.md
---

Konwertuje bitmapę na ciąg zakodowany w base64.

## Składnia Analyze

```python
func.bitmap_to_base64(<bitmap>)
```

## Przykłady Analyze

```python
func.bitmap_to_base64(get_column(table, 'bm'))

┌──────────┐
│ 'AQI...' │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_TO_BASE64(<bitmap>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_BASE64(BITMAP_FROM_STRING('1,2,3'));

┌─────────────────┐
│ (base64 string) │
└─────────────────┘
```
