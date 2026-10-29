---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS – prüft, ob eine Bitmap einen bestimmten Wert enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

Prüft, ob eine Bitmap einen bestimmten Wert enthält.

## Analyze-Syntax

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Analyze-Beispiele

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
