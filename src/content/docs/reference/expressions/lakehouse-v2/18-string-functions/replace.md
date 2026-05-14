---
title: REPLACE
description: "Learn how to use the REPLACE string function in PlaidCloud Lakehouse. Replaces all occurrences of a substring with another substring - with syntax and examples."
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
