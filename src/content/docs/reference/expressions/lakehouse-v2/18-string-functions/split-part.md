---
title: SPLIT_PART
description: SPLIT_PART — splits a string by a delimiter and returns the element at a specified index.
---

Splits a string by a delimiter and returns the element at a specified index.

## Analyze Syntax

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Analyze Examples

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## SQL Syntax

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## SQL Examples

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
