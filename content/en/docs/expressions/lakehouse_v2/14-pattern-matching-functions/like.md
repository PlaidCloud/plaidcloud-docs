---
title: LIKE
---

Matches a string against a pattern using `%` (any characters) and `_` (single character) wildcards.

## Analyze Syntax

```python
func.like(<str> LIKE <pattern>)
```

## Analyze Examples

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL Syntax

```sql
LIKE(<str> LIKE <pattern>)
```

## SQL Examples

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
