---
title: LOG10
description: "Learn how to use the LOG10 math function in PlaidCloud Lakehouse. Returns the base-10 logarithm of a number - see syntax, examples, and output."
---

Returns the base-10 logarithm of a number.

## Analyze Syntax

```python
func.log10(<x>)
```

## Analyze Examples

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL Syntax

```sql
LOG10(<x>)
```

## SQL Examples

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
