---
title: IS_NULL
description: "Learn how to use the IS_NULL conditional function in PlaidCloud Lakehouse. Checks whether a value is NULL. Includes usage and syntax details."
---

Checks whether a value is NULL.

## Analyze Syntax

```python
func.is_null(<expr>)
```

## Analyze Examples

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## SQL Syntax

```sql
IS_NULL(<expr>)
```

## SQL Examples

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
