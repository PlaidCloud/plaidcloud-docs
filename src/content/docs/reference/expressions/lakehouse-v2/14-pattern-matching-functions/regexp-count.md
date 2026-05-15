---
title: REGEXP_COUNT (Lakehouse v2)
description: "Use the REGEXP_COUNT pattern matching function in PlaidCloud Lakehouse. Returns the number of times a regular expression pattern occurs in a string."
---

Returns the number of times a regular expression pattern occurs in a string.

## Analyze Syntax

```python
func.regexp_count(<str>, <pattern>)
```

## Analyze Examples

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## SQL Syntax

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## SQL Examples

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
