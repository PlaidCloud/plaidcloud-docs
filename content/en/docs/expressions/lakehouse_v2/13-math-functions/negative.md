---
title: NEGATIVE
description: "Learn how to use the NEGATIVE math function in PlaidCloud Lakehouse. Returns the negation of a number - see syntax, examples, and output."
---

Returns the negation of a number.

## Analyze Syntax

```python
func.negative(<x>)
```

## Analyze Examples

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## SQL Syntax

```sql
NEGATIVE(<x>)
```

## SQL Examples

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
