---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP – teilt eine Bitmap in mehrere Teil-Bitmaps einer bestimmten Größe auf.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

Teilt eine Bitmap in mehrere Teil-Bitmaps einer bestimmten Größe auf.

## Analyze-Syntax

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Analyze-Beispiele

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## SQL-Syntax

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
