---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE — returns the current active role.
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
