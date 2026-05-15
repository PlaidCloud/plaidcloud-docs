---
title: LTRIM (Lakehouse v2)
description: LTRIM — Removes leading whitespace or specified characters from a string.
---

Removes leading whitespace or specified characters from a string.

## Analyze Syntax

```python
func.ltrim(<str>)
```

## Analyze Examples

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL Syntax

```sql
LTRIM(<str>)
```

## SQL Examples

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
