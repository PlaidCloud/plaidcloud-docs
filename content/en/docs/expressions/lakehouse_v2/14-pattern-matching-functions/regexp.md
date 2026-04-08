---
title: REGEXP
description: "Learn how to use the REGEXP pattern matching function in PlaidCloud Lakehouse. Checks whether a string matches a regular expression pattern."
---

Checks whether a string matches a regular expression pattern.

## Analyze Syntax

```python
func.regexp(<str> REGEXP <pattern>)
```

## Analyze Examples

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL Syntax

```sql
REGEXP(<str> REGEXP <pattern>)
```

## SQL Examples

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```
