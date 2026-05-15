---
title: ISNULL (Lakehouse v2)
description: ISNULL — Checks whether a value is NULL. Returns 1 if NULL, 0 otherwise.
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
