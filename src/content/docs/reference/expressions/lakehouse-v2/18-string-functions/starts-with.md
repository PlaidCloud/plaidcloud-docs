---
title: STARTS_WITH
description: STARTS_WITH — Checks whether a string starts with a specified prefix.
---

Checks whether a string starts with a specified prefix.

## Analyze Syntax

```python
func.starts_with(<str>, <prefix>)
```

## Analyze Examples

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
STARTS_WITH(<str>, <prefix>)
```

## SQL Examples

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
