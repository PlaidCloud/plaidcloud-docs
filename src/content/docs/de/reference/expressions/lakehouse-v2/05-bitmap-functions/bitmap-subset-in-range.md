---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE – gibt eine Teilmenge einer Bitmap innerhalb eines angegebenen Bereichs zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

Gibt eine Teilmenge einer Bitmap innerhalb eines angegebenen Bereichs zurück.

## Analyze-Syntax

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Analyze-Beispiele

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
