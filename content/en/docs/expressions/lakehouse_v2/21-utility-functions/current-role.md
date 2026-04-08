---
title: CURRENT_ROLE
description: "Learn how to use the CURRENT_ROLE utility function in PlaidCloud Lakehouse. Returns the current active role - see syntax, examples, and output."
---

Returns the current active role.

## Analyze Syntax

```python
func.current_role()
```

## Analyze Examples

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## SQL Syntax

```sql
CURRENT_ROLE()
```

## SQL Examples

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
