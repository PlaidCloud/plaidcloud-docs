---
title: BITMAP_CONTAINS
description: "Learn how to use the BITMAP_CONTAINS bitmap function in PlaidCloud Lakehouse. Checks whether a bitmap contains a specific value - with syntax and examples."
---

Checks whether a bitmap contains a specific value.

## Analyze Syntax

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Analyze Examples

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## SQL Examples

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
