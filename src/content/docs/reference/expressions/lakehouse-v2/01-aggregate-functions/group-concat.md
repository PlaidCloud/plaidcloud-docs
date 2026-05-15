---
title: GROUP_CONCAT
description: GROUP_CONCAT — concatenates values from a group into a single string with a separator.
---

Concatenates values from a group into a single string with a separator.

## Analyze Syntax

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Analyze Examples

```python
func.group_concat(get_column(table, 'name'))
```

## SQL Syntax

```sql
GROUP_CONCAT(<name>, literal(','))
```

## SQL Examples

```sql
SELECT department, GROUP_CONCAT(name ORDER BY name SEPARATOR ', ')
FROM employees GROUP BY department;

┌────────────┬──────────────────────────┐
│ department │ group_concat(name)       │
├────────────┼──────────────────────────┤
│ Sales      │ Alice, Bob, Charlie      │
│ IT         │ Dave, Eve                │
└────────────┴──────────────────────────┘
```
