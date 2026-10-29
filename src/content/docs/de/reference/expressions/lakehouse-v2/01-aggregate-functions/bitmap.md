---
title: BITMAP (Lakehouse v2)
description: BITMAP gibt die Bitmap-Vereinigung einer Menge von Werten zurück. Wird typischerweise mit BITMAP_AGG verwendet.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

Gibt die Bitmap-Vereinigung einer Menge von Werten zurück. Wird typischerweise mit BITMAP_AGG verwendet.

## Analyze-Syntax

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze-Beispiele

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP(<id>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
