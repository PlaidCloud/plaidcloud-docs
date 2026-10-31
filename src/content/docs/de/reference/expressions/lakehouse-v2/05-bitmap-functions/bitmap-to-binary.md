---
title: BITMAP_TO_BINARY (Lakehouse v2)
description: BITMAP_TO_BINARY – wandelt eine Bitmap in einen Binärwert um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-binary.md
---

Wandelt eine Bitmap in einen Binärwert um.

## Analyze-Syntax

```python
func.bitmap_to_binary(<bitmap>)
```

## Analyze-Beispiele

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
