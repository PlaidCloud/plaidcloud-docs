---
title: REGEXP_REPLACE
---

Replaces substrings matching a regular expression pattern with a replacement string.

## Analyze Syntax

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Analyze Examples

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL Syntax

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## SQL Examples

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
