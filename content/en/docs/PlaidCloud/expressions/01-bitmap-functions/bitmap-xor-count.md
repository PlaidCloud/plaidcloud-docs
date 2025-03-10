---
title: BITMAP_XOR_COUNT
---

Counts the number of bits set to 1 in the bitmap by performing a logical XOR (exclusive OR) operation.

## Analyze Syntax

```python
func.bitmap_xor_count( <bitmap> )
```

## Analyze Examples

```python
func.bitmap_xor_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_xor_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_XOR_COUNT( <bitmap> )
```

## SQL Examples

```sql
SELECT BITMAP_XOR_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_xor_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```