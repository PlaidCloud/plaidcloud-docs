---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN – gibt den kleinsten Wert einer Bitmap zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

Gibt den kleinsten Wert einer Bitmap zurück.

## Analyze-Syntax

```python
func.bitmap_min(<bitmap>)
```

## Analyze-Beispiele

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
BITMAP_MIN(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
