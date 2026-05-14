---
title: NULL_OR_EMPTY
description: "Learn how to use the NULL_OR_EMPTY string function in PlaidCloud Lakehouse. Checks whether a string is NULL or empty. Returns 1 if true, 0 otherwise."
---

Checks whether a string is NULL or empty. Returns 1 if true, 0 otherwise.

## Analyze Syntax

```python
func.null_or_empty(<str>)
```

## Analyze Examples

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
NULL_OR_EMPTY(<str>)
```

## SQL Examples

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
