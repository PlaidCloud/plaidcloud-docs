---
title: TO_BITMAP
description: "Learn how to use the TO_BITMAP bitmap function in PlaidCloud Lakehouse. Converts an integer value to a bitmap containing that single value."
---

Converts an integer value to a bitmap containing that single value.

## Analyze Syntax

```python
func.to_bitmap(<value>)
```

## Analyze Examples

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
TO_BITMAP(<value>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
