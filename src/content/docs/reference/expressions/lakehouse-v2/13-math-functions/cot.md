---
title: COT
description: "Learn how to use the COT math function in PlaidCloud Lakehouse. Returns the cotangent of a number in radians - see syntax, examples, and output."
---

Returns the cotangent of a number in radians.

## Analyze Syntax

```python
func.cot(<x>)
```

## Analyze Examples

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## SQL Syntax

```sql
COT(<x>)
```

## SQL Examples

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
