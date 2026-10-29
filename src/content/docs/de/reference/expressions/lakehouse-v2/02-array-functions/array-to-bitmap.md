---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP – wandelt ein Array aus Ganzzahlen in eine Bitmap um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

Wandelt ein Array aus Ganzzahlen in eine Bitmap um.

## Analyze-Syntax

```python
func.array_to_bitmap([1, 2, 3])
```

## Analyze-Beispiele

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
