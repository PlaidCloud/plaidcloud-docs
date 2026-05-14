---
title: LOG
description: "Learn how to use the LOG math function in PlaidCloud Lakehouse. Returns the logarithm of a number with a specified base - see syntax, examples, and output."
---

Returns the logarithm of a number with a specified base.

## Analyze Syntax

```python
func.log(<base>, <x>)
```

## Analyze Examples

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## SQL Syntax

```sql
LOG(<base>, <x>)
```

## SQL Examples

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
