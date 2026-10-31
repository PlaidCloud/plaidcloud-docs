---
title: BITMAP_HAS_ANY (Lakehouse v1)
description: BITMAP_HAS_ANY – prüft, ob die erste Bitmap mindestens ein Bit hat, das mit den Bits der zweiten Bitmap übereinstimmt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-any.md
---

Prüft, ob die erste Bitmap mindestens ein Bit hat, das mit den Bits der zweiten Bitmap übereinstimmt.

## Analyze-Syntax

```python
func.bitmap_has_any( <bitmap1>, <bitmap2> )
```

## Analyze-Beispiele

```python
func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))

┌───────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))  │
├───────────────────────────────────────────────────────────────────────────────┤
│ true                                                                          │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_HAS_ANY( <bitmap1>, <bitmap2> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_HAS_ANY(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_any(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ true                                                          │
└───────────────────────────────────────────────────────────────┘
```
