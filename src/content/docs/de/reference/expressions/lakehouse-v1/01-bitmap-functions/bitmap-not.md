---
title: BITMAP_NOT (Lakehouse v1)
description: BITMAP_NOT – erzeugt eine neue Bitmap mit den Elementen der ersten Bitmap, die nicht in der zweiten enthalten sind.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not.md
---

Erzeugt eine neue Bitmap mit den Elementen der ersten Bitmap, die nicht in der zweiten enthalten sind.

## Analyze-Syntax

```python
func.bitmap_not( <bitmap1>, <bitmap2> )
```

## Analyze-Beispiele

```python
func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)  │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_NOT( <bitmap1>, <bitmap2> )
```

## Aliasse

- [BITMAP_AND_NOT](../bitmap-and-not)

## SQL-Beispiele

```sql
SELECT BITMAP_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────┐
│ bitmap_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                  │
└──────────────────────────────────────────────────────────────────────┘

SELECT BITMAP_AND_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────────┐
│ bitmap_and_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                      │
└──────────────────────────────────────────────────────────────────────────┘
```
