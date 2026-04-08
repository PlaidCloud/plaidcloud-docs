---
title: IS_ROLE_IN_SESSION
description: "Learn how to use the IS_ROLE_IN_SESSION utility function in PlaidCloud Lakehouse. Checks whether a specified role is active in the current session."
---

Checks whether a specified role is active in the current session.

## Analyze Syntax

```python
func.is_role_in_session(<role_name>)
```

## Analyze Examples

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## SQL Syntax

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## SQL Examples

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
