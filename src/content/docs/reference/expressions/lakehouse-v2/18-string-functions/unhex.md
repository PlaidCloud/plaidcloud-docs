---
title: UNHEX (Lakehouse v2)
description: UNHEX — converts a hexadecimal string to a character string.
---

Converts a hexadecimal string to a character string.

## Analyze Syntax

```python
func.unhex(<hex_str>)
```

## Analyze Examples

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL Syntax

```sql
UNHEX(<hex_str>)
```

## SQL Examples

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
