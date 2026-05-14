---
title: BITMAP_HASH64
description: "Learn how to use the BITMAP_HASH64 bitmap function in PlaidCloud Lakehouse. Computes a 64-bit hash of a value and returns a bitmap containing that hash."
---

Computes a 64-bit hash of a value and returns a bitmap containing that hash.

## Analyze Syntax

```python
func.bitmap_hash64(<value>)
```

## Analyze Examples

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_HASH64(<value>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```
