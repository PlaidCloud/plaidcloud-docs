---
title: BITMAP_EMPTY
description: BITMAP_EMPTY — returns an empty bitmap - see syntax, examples, and output.
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
