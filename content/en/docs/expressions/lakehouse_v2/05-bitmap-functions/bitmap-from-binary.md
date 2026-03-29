---
title: BITMAP_FROM_BINARY
---

Converts a binary value to a bitmap.

## Analyze Syntax

```python
func.bitmap_from_binary(<binary>)
```

## Analyze Examples

```python
func.bitmap_from_binary(get_column(table, 'bin_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_FROM_BINARY(<binary>)
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_BINARY(bm_binary)) FROM data;

┌───┐
│ 5 │
└───┘
```
