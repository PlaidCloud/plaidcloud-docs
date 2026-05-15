---
title: REGEXP_REPLACE (Lakehouse v2)
description: "Use the REGEXP_REPLACE pattern matching function in PlaidCloud Lakehouse. Replaces substrings matching a regular expression pattern with a replacement string."
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
