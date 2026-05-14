---
title: BITMAP_HASH
description: "Learn how to use the BITMAP_HASH bitmap function in PlaidCloud Lakehouse. Computes a 32-bit hash of a value and returns a bitmap containing that hash."
---

Computes a 32-bit hash of a value and returns a bitmap containing that hash.

## Analyze Syntax

```python
func.bitmap_hash(<value>)
```

## Analyze Examples

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_HASH(<value>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
