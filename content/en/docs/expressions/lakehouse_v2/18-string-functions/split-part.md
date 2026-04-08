---
title: SPLIT_PART
description: "Learn how to use the SPLIT_PART string function in PlaidCloud Lakehouse. Splits a string by a delimiter and returns the element at a specified index."
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
