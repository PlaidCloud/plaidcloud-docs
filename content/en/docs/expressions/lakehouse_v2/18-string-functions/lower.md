---
title: LOWER
description: "Learn how to use the LOWER string function in PlaidCloud Lakehouse. Converts a string to lowercase - see syntax, examples, and output."
---

Converts a string to lowercase.

## Analyze Syntax

```python
func.lower(<str>)
```

## Analyze Examples

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL Syntax

```sql
LOWER(<str>)
```

## SQL Examples

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
