---
title: SPLIT
description: "Learn how to use the SPLIT string function in PlaidCloud Lakehouse. Splits a string by a delimiter and returns an array - see syntax, examples, and output."
---

Splits a string by a delimiter and returns an array.

## Analyze Syntax

```python
func.split(<str>, <delimiter>)
```

## Analyze Examples

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## SQL Syntax

```sql
SPLIT(<str>, <delimiter>)
```

## SQL Examples

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
