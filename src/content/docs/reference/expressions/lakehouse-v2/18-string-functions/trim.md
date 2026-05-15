---
title: TRIM (Lakehouse v2)
description: TRIM — removes leading and trailing whitespace or specified characters from a string.
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
