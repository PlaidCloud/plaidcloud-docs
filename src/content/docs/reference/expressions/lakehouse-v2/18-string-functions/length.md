---
title: LENGTH (Lakehouse v2)
description: LENGTH — returns the length of a string in bytes.
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
