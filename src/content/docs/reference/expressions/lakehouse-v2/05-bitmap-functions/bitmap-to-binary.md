---
title: BITMAP_TO_BINARY
description: BITMAP_TO_BINARY — converts a bitmap to a binary value - see syntax, examples, and output.
---

Converts a bitmap to a binary value.

## Analyze Syntax

```python
func.bitmap_to_binary(<bitmap>)
```

## Analyze Examples

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## SQL Examples

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
