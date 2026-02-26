---
title: BITMAP_NOT
---

Generates a new bitmap with elements from the first bitmap that are not in the second one.

## Analyze Syntax

```python
func.bitmap_not( <bitmap1>, <bitmap2> )
```

## Analyze Examples

```python
func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)  │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_NOT( <bitmap1>, <bitmap2> )
```

## Aliases

- [BITMAP_AND_NOT](../bitmap-and-not)

## SQL Examples

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