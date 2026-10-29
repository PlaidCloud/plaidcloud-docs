---
title: BASE64_TO_BITMAP (Lakehouse v2)
description: BASE64_TO_BITMAP – wandelt eine Base64-kodierte Zeichenfolge in eine Bitmap um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/base64-to-bitmap.md
---

Wandelt eine Base64-kodierte Zeichenfolge in eine Bitmap um.

## Analyze-Syntax

```python
func.base64_to_bitmap(<str>)
```

## Analyze-Beispiele

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BASE64_TO_BITMAP(<str>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```
