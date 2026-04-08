---
title: DIVIDE
description: "Learn how to use the DIVIDE math function in PlaidCloud Lakehouse. Returns the result of dividing one number by another - see syntax, examples, and output."
---

Returns the result of dividing one number by another.

## Analyze Syntax

```python
func.divide(<x>, <y>)
```

## Analyze Examples

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## SQL Syntax

```sql
DIVIDE(<x>, <y>)
```

## SQL Examples

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
