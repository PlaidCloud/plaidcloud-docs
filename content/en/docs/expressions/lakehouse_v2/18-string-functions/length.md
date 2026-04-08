---
title: LENGTH
description: "Learn how to use the LENGTH string function in PlaidCloud Lakehouse. Returns the length of a string in bytes - see syntax, examples, and output."
---

Returns the length of a string in bytes.

## Analyze Syntax

```python
func.length(<str>)
```

## Analyze Examples

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL Syntax

```sql
LENGTH(<str>)
```

## SQL Examples

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
