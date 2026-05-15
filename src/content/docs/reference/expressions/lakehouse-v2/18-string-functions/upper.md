---
title: UPPER (Lakehouse v2)
description: UPPER — converts a string to uppercase.
---

Converts a string to uppercase.

## Analyze Syntax

```python
func.upper(<str>)
```

## Analyze Examples

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL Syntax

```sql
UPPER(<str>)
```

## SQL Examples

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
