---
title: DSQRT
description: "Learn how to use the DSQRT math function in PlaidCloud Lakehouse. Alias for `SQRT`. See [SQRT](sqrt) - see syntax, examples, and output."
---

Alias for `SQRT`. See [SQRT](sqrt).

## Analyze Syntax

```python
func.dsqrt(144)
```

## Analyze Examples

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## SQL Syntax

```sql
DSQRT(<x>)
```

## SQL Examples

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
