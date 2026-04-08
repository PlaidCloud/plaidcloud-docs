---
title: ENDS_WITH
description: "Learn how to use the ENDS_WITH string function in PlaidCloud Lakehouse. Checks whether a string ends with a specified suffix - with syntax and examples."
---

Checks whether a string ends with a specified suffix.

## Analyze Syntax

```python
func.ends_with(<str>, <suffix>)
```

## Analyze Examples

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
ENDS_WITH(<str>, <suffix>)
```

## SQL Examples

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
