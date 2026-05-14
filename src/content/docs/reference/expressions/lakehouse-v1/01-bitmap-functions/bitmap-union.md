---
title: BITMAP_UNION
description: "Learn how to use the BITMAP_UNION bitmap function in PlaidCloud Lakehouse. Counts the number of bits set to 1 in the bitmap by performing a logical UNION..."
---

Counts the number of bits set to 1 in the bitmap by performing a logical UNION operation.

## Analyze Syntax

```python
func.bitmap_union( <bitmap> )
```

## Analyze Examples

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_UNION( <bitmap> )
```

## SQL Examples

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
