---
title: SPLIT (Lakehouse v2)
description: SPLIT — splits a string by a delimiter and returns an array.
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
