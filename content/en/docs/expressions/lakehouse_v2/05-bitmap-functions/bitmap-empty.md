---
title: BITMAP_EMPTY
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
