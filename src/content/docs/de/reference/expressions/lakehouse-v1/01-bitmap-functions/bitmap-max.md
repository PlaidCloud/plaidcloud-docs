---
title: BITMAP_MAX (Lakehouse v1)
description: BITMAP_MAX – ermittelt den Maximalwert in der Bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-max.md
---

Ermittelt den Maximalwert in der Bitmap.

## Analyze-Syntax

```python
func.bitmap_max( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_max(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_max(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             5 │
└───────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_MAX( <bitmap> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_MAX(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_max(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   5 │
└─────────────────────────────────────┘
```
