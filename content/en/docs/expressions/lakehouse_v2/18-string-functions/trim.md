---
title: TRIM
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
