---
title: BITMAP_OR_COUNT
---

Counts the number of bits set to 1 in the bitmap by performing a logical OR operation.

## Analyze Syntax

```python
func.bitmap_or_count( <bitmap> )
```

## Analyze Examples

```python
func.bitmap_or_count(func.to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────────┐
│ func.bitmap_or_count(func.to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────────┤
│                                               3 │
└─────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
BITMAP_OR_COUNT( <bitmap> )
```

## SQL Examples

```sql
SELECT BITMAP_OR_COUNT(TO_BITMAP('1, 3, 5'));

┌───────────────────────────────────────┐
│ bitmap_or_count(to_bitmap('1, 3, 5')) │
├───────────────────────────────────────┤
│                                     3 │
└───────────────────────────────────────┘
```