---
title: IS_NOT_NULL
description: "Learn how to use the IS_NOT_NULL conditional function in PlaidCloud Lakehouse. Checks whether a value is not NULL. Includes syntax and examples."
---

Checks whether a value is not NULL.

## Analyze Syntax

```python
func.is_not_null(<expr>)
```

## Analyze Examples

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## SQL Syntax

```sql
IS_NOT_NULL(<expr>)
```

## SQL Examples

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
