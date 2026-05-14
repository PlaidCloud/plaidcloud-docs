---
title: BITMAP_CONTAINS
description: "Learn how to use the BITMAP_CONTAINS bitmap function in PlaidCloud Lakehouse. Checks if the bitmap contains a specific value. Includes syntax and examples."
---

Checks if the bitmap contains a specific value.


## Analyze Syntax

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Analyze Examples

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## SQL Examples

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
