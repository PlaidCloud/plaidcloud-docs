---
title: REPLACE
description: REPLACE — Replaces all occurrences of a substring with another substring.
---

Replaces all occurrences of a substring with another substring.

## Analyze Syntax

```python
func.replace(<str>, <old>, <new>)
```

## Analyze Examples

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## SQL Syntax

```sql
REPLACE(<str>, <old>, <new>)
```

## SQL Examples

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
