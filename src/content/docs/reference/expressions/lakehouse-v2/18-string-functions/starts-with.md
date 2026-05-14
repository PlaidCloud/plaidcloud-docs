---
title: STARTS_WITH
description: "Learn how to use the STARTS_WITH string function in PlaidCloud Lakehouse. Checks whether a string starts with a specified prefix - with syntax and examples."
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
