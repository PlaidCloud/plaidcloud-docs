---
title: BITMAP_TO_ARRAY (Lakehouse v2)
description: BITMAP_TO_ARRAY – wandelt eine Bitmap in ein Array aus Ganzzahlen um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-array.md
---

Wandelt eine Bitmap in ein Array aus Ganzzahlen um.

## Analyze-Syntax

```python
func.bitmap_to_array(<bitmap>)
```

## Analyze-Beispiele

```python
func.bitmap_to_array(get_column(table, 'bm'))

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQL-Syntax

```sql
BITMAP_TO_ARRAY(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_ARRAY(BITMAP_FROM_STRING('1,2,3'));

┌─────────┐
│ [1,2,3] │
└─────────┘
```
