---
title: BITMAP_AND
---

Performs a bitwise AND operation on the two bitmaps.

## Analyze Syntax

```python
func.bitmap_and( <bitmap1>, <bitmap2> )
```

## Analyze Examples

```python
func.bitmap_and(func.build_bitmap([1, 4, 5]), func.cast(build_bitmap([4, 5])), string)

┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_and(func.build_bitmap([1, 4, 5]), func.cast(build_bitmap([4, 5])), string) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 4,5                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_AND( <bitmap1>, <bitmap2> )
```

## SQL Examples

```sql
SELECT BITMAP_AND(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([4,5]))::String;

┌───────────────────────────────────────────────────────────────────┐
│ bitmap_and(build_bitmap([1, 4, 5]), build_bitmap([4, 5]))::string │
├───────────────────────────────────────────────────────────────────┤
│ 4,5                                                               │
└───────────────────────────────────────────────────────────────────┘
```