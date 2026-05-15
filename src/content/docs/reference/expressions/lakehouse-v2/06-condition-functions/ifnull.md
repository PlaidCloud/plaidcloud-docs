---
title: IFNULL (Lakehouse v2)
description: IFNULL — returns the first expression if it is not NULL, otherwise returns the second expression.
---

Returns the first expression if it is not NULL, otherwise returns the second expression.

## Analyze Syntax

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Analyze Examples

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## SQL Syntax

```sql
IFNULL(<phone>, 'N/A')
```

## SQL Examples

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
