---
title: ISNULL
description: "Learn how to use the ISNULL utility function in PlaidCloud Lakehouse. Checks whether a value is NULL. Returns 1 if NULL, 0 otherwise - with syntax and examples."
---

Checks whether a value is NULL. Returns 1 if NULL, 0 otherwise.

## Analyze Syntax

```python
func.isnull(<expr>)
```

## Analyze Examples

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
ISNULL(<expr>)
```

## SQL Examples

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
