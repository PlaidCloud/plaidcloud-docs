---
title: GROUP_CONCAT
description: "Learn how to use the GROUP_CONCAT string function in PlaidCloud Lakehouse. Concatenates values from a group into a single string with a separator."
---

Concatenates values from a group into a single string with a separator.

## Analyze Syntax

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Analyze Examples

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## SQL Syntax

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## SQL Examples

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
