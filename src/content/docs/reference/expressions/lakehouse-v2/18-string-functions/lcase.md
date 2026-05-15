---
title: LCASE
description: LCASE — converts a string to lowercase. Alias for `LOWER` - see syntax, examples, and output.
---

Converts a string to lowercase. Alias for `LOWER`.

## Analyze Syntax

```python
func.lcase(<str>)
```

## Analyze Examples

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL Syntax

```sql
LCASE(<str>)
```

## SQL Examples

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
