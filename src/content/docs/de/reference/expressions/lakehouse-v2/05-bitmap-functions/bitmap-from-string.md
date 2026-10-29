---
title: BITMAP_FROM_STRING (Lakehouse v2)
description: BITMAP_FROM_STRING – wandelt eine durch Kommas getrennte Zeichenfolge aus Ganzzahlen in eine Bitmap um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-string.md
---

Wandelt eine durch Kommas getrennte Zeichenfolge aus Ganzzahlen in eine Bitmap um.

## Analyze-Syntax

```python
func.bitmap_from_string(<str>)
```

## Analyze-Beispiele

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_FROM_STRING(<str>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
