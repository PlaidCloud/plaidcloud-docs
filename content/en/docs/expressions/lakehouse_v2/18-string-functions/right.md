---
title: RIGHT
description: "Learn how to use the RIGHT string function in PlaidCloud Lakehouse. Returns the rightmost N characters of a string - see syntax, examples, and output."
---

Returns the rightmost N characters of a string.

## Analyze Syntax

```python
func.right(<str>, <len>)
```

## Analyze Examples

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL Syntax

```sql
RIGHT(<str>, <len>)
```

## SQL Examples

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
