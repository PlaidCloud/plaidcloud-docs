---
title: REVERSE
description: "Learn how to use the REVERSE string function in PlaidCloud Lakehouse. Reverses a string - see syntax, examples, and output."
---

Reverses a string.

## Analyze Syntax

```python
func.reverse(<str>)
```

## Analyze Examples

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## SQL Syntax

```sql
REVERSE(<str>)
```

## SQL Examples

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
