---
title: UCASE
description: "Learn how to use the UCASE string function in PlaidCloud Lakehouse. Converts a string to uppercase. Alias for `UPPER` - see syntax, examples, and output."
---

Converts a string to uppercase. Alias for `UPPER`.

## Analyze Syntax

```python
func.ucase(<str>)
```

## Analyze Examples

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL Syntax

```sql
UCASE(<str>)
```

## SQL Examples

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
