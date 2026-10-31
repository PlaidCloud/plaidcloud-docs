---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE – entfernt einen bestimmten Wert aus einer Bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

Entfernt einen bestimmten Wert aus einer Bitmap.

## Analyze-Syntax

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Analyze-Beispiele

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
