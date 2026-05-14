---
title: BITMAP_MIN
description: "Learn how to use the BITMAP_MIN bitmap function in PlaidCloud Lakehouse. Gets the minimum value in the bitmap. Includes syntax and examples."
---

Gets the minimum value in the bitmap.

## Analyze Syntax

```python
func.bitmap_min( <bitmap> )
```

## Analyze Examples

```python
func.bitmap_min(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_min(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             1 │
└───────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_MIN( <bitmap> )
```

## SQL Examples

```sql
SELECT BITMAP_MIN(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_min(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘
```
