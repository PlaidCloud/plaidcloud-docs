---
title: BITMAP_HAS_ALL
---

Checks if the first bitmap contains all the bits in the second bitmap.

## Analyze Syntax

```python
func.bitmap_has_all( <bitmap1>, <bitmap2> )
```

## Analyze Examples

```python
func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) 

┌─────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2]))  │
├─────────────────────────────────────────────────────────────────────┤
│ false                                                               │
└─────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_HAS_ALL( <bitmap1>, <bitmap2> )
```

## SQL Examples

```sql
SELECT BITMAP_HAS_ALL(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ false                                                         │
└───────────────────────────────────────────────────────────────┘
```