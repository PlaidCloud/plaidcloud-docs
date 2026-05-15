---
title: "REVERSE (String, Lakehouse v2)"
description: REVERSE — reverses a string.
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
