---
title: TRIM
description: "Learn how to use the TRIM string function in PlaidCloud Lakehouse. Removes leading and trailing whitespace or specified characters from a string."
---

Removes leading and trailing whitespace or specified characters from a string.

## Analyze Syntax

```python
func.trim(<str>)
```

## Analyze Examples

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL Syntax

```sql
TRIM(<str>)
```

## SQL Examples

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
