---
title: LOWER (Lakehouse v2)
description: LOWER — converts a string to lowercase.
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
