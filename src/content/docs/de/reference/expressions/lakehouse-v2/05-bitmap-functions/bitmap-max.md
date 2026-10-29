---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX – gibt den größten Wert einer Bitmap zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-max.md
---

Gibt den größten Wert einer Bitmap zurück.

## Analyze-Syntax

```python
func.bitmap_max(<bitmap>)
```

## Analyze-Beispiele

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## SQL-Syntax

```sql
BITMAP_MAX(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
