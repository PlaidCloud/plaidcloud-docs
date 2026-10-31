---
title: BITMAP_SUBSET_LIMIT (Lakehouse v1)
description: BITMAP_SUBSET_LIMIT – erzeugt eine Teil-Bitmap der Quell-Bitmap, die mit einem Bereich ab dem Startwert beginnt und eine Größenbeschränkung hat.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-limit.md
---

Erzeugt eine Teil-Bitmap der Quell-Bitmap, die mit einem Bereich ab dem Startwert beginnt und eine Größenbeschränkung hat.

## Analyze-Syntax

```python
func.bitmap_subset_limit( <bitmap>, <start>, <limit> )
```

## Analyze-Beispiele

```python
func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2)

┌──────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2) │
├──────────────────────────────────────────────────────────────┤
│ 4,5                                                          │
└──────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_SUBSET_LIMIT( <bitmap>, <start>, <limit> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_SUBSET_LIMIT(BUILD_BITMAP([1,4,5]), 2, 2)::String;

┌────────────────────────────────────────────────────────────┐
│ bitmap_subset_limit(build_bitmap([1, 4, 5]), 2, 2)::string │
├────────────────────────────────────────────────────────────┤
│ 4,5                                                        │
└────────────────────────────────────────────────────────────┘
```
