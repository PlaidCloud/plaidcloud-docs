---
title: BITMAP_INTERSECT
---

Counts the number of bits set to 1 in the bitmap by performing a logical INTERSECT operation.

## Analyze Syntax

```python
func.bitmap_intersect( <bitmap> )
```

## Analyze Examples

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_INTERSECT( <bitmap> )
```

## SQL Examples

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```