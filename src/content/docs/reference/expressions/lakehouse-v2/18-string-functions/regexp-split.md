---
title: REGEXP_SPLIT
description: REGEXP_SPLIT — splits a string by a regular expression pattern and returns an array of substrings.
---

Splits a string by a regular expression pattern and returns an array of substrings.

## Analyze Syntax

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Analyze Examples

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## SQL Syntax

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## SQL Examples

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
