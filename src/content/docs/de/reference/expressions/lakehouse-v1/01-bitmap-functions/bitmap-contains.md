---
title: BITMAP_CONTAINS (Lakehouse v1)
description: BITMAP_CONTAINS – prüft, ob die Bitmap einen bestimmten Wert enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

Prüft, ob die Bitmap einen bestimmten Wert enthält.


## Analyze-Syntax

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Analyze-Beispiele

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
