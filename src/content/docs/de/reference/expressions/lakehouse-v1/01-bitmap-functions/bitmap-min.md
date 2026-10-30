---
title: BITMAP_MIN (Lakehouse v1)
description: BITMAP_MIN – ermittelt den Minimalwert in der Bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-min.md
---

Ermittelt den Minimalwert in der Bitmap.

## Analyze-Syntax

```python
func.bitmap_min( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_min(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_min(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             1 │
└───────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_MIN( <bitmap> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_MIN(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_min(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘
```
