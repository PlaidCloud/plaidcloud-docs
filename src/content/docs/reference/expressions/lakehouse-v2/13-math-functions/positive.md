---
title: POSITIVE
description: "Learn how to use the POSITIVE math function in PlaidCloud Lakehouse. Returns the value unchanged (unary plus) - see syntax, examples, and output."
---

Returns the value unchanged (unary plus).

## Analyze Syntax

```python
func.positive(<x>)
```

## Analyze Examples

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## SQL Syntax

```sql
POSITIVE(<x>)
```

## SQL Examples

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
