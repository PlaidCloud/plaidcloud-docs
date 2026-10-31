---
title: BITMAP_TO_BASE64 (Lakehouse v2)
description: BITMAP_TO_BASE64 – wandelt eine Bitmap in eine Base64-kodierte Zeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-base64.md
---

Wandelt eine Bitmap in eine Base64-kodierte Zeichenfolge um.

## Analyze-Syntax

```python
func.bitmap_to_base64(<bitmap>)
```

## Analyze-Beispiele

```python
func.bitmap_to_base64(get_column(table, 'bm'))

┌──────────┐
│ 'AQI...' │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_TO_BASE64(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_BASE64(BITMAP_FROM_STRING('1,2,3'));

┌─────────────────┐
│ (base64 string) │
└─────────────────┘
```
