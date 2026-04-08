---
title: BITMAP_EMPTY
description: "Learn how to use the BITMAP_EMPTY bitmap function in PlaidCloud Lakehouse. Returns an empty bitmap - see syntax, examples, and output."
---

Returns an empty bitmap.

## Analyze Syntax

```python
func.bitmap_empty()
```

## Analyze Examples

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## SQL Syntax

```sql
BITMAP_EMPTY()
```

## SQL Examples

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
