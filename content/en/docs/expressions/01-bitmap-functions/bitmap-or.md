---
title: BITMAP_OR
---

Performs a bitwise OR operation on the two bitmaps.

## Analyze Syntax

```python
func.bitmap_or( <bitmap1>, <bitmap2> )
```

## Analyze Examples

```python
func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7]))

┌─────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7])) │
├─────────────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_OR( <bitmap1>, <bitmap2> )
```

## SQL Examples

```sql
SELECT BITMAP_OR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([6,7]))::String;

┌──────────────────────────────────────────────────────────────────┐
│ bitmap_or(build_bitmap([1, 4, 5]), build_bitmap([6, 7]))::string │
├──────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                        │
└──────────────────────────────────────────────────────────────────┘
```