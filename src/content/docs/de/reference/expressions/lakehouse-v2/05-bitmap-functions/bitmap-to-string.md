---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING – wandelt eine Bitmap in eine durch Kommas getrennte Zeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

Wandelt eine Bitmap in eine durch Kommas getrennte Zeichenfolge um.

## Analyze-Syntax

```python
func.bitmap_to_string(<bitmap>)
```

## Analyze-Beispiele

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## SQL-Syntax

```sql
BITMAP_TO_STRING(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
