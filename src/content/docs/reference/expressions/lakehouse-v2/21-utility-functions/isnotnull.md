---
title: ISNOTNULL
description: "Learn how to use the ISNOTNULL utility function in PlaidCloud Lakehouse. Checks whether a value is not NULL. Returns 1 if not NULL, 0 otherwise."
---

Checks whether a value is not NULL. Returns 1 if not NULL, 0 otherwise.

## Analyze Syntax

```python
func.isnotnull(<expr>)
```

## Analyze Examples

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
ISNOTNULL(<expr>)
```

## SQL Examples

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
