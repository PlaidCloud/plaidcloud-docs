---
title: UCASE (Lakehouse v2)
description: UCASE — converts a string to uppercase. Alias for `UPPER`.
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
