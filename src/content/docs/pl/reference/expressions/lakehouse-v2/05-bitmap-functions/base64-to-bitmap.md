---
title: BASE64_TO_BITMAP (Lakehouse v2)
description: BASE64_TO_BITMAP — konwertuje ciąg zakodowany w base64 na bitmapę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/base64-to-bitmap.md
---

Konwertuje ciąg zakodowany w base64 na bitmapę.

## Składnia Analyze

```python
func.base64_to_bitmap(<str>)
```

## Przykłady Analyze

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BASE64_TO_BITMAP(<str>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```
