---
title: UPPER
description: "Learn how to use the UPPER string function in PlaidCloud Lakehouse. Converts a string to uppercase - see syntax, examples, and output."
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
