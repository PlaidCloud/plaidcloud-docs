---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT – gibt eine Teilmenge einer Bitmap ab einem Offset mit einer Begrenzung der Kardinalität zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

Gibt eine Teilmenge einer Bitmap ab einem Offset mit einer Begrenzung der Kardinalität zurück.

## Analyze-Syntax

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Analyze-Beispiele

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
