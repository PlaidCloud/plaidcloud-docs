---
title: LEFT
description: "Learn how to use the LEFT string function in PlaidCloud Lakehouse. Returns the leftmost N characters of a string - see syntax, examples, and output."
---

Returns the leftmost N characters of a string.

## Analyze Syntax

```python
func.left(<str>, <len>)
```

## Analyze Examples

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL Syntax

```sql
LEFT(<str>, <len>)
```

## SQL Examples

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
