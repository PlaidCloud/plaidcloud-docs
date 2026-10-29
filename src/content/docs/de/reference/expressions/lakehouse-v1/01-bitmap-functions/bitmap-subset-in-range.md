---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v1)
description: BITMAP_SUBSET_IN_RANGE – erzeugt eine Teil-Bitmap der Quell-Bitmap innerhalb eines angegebenen Bereichs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-in-range.md
---

Erzeugt eine Teil-Bitmap der Quell-Bitmap innerhalb eines angegebenen Bereichs.

## Analyze-Syntax

```python
func.bitmap_subset_in_range( <bitmap>, <start>, <end> )
```

## Analyze-Beispiele

```python
func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9)

┌─────────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9) │
├─────────────────────────────────────────────────────────────────┤
│ 7                                                               │
└─────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_SUBSET_IN_RANGE( <bitmap>, <start>, <end> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_SUBSET_IN_RANGE(BUILD_BITMAP([5,7,9]), 6, 9)::String;

┌───────────────────────────────────────────────────────────────┐
│ bitmap_subset_in_range(build_bitmap([5, 7, 9]), 6, 9)::string │
├───────────────────────────────────────────────────────────────┤
│ 7                                                             │
└───────────────────────────────────────────────────────────────┘
```
