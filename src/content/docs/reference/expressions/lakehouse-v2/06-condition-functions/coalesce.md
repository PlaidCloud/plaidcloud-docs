---
title: COALESCE
description: "Learn how to use the COALESCE condition function in PlaidCloud Lakehouse. Returns the first non-NULL expression from a list of expressions."
---

Returns the first non-NULL expression from a list of expressions.

## Analyze Syntax

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Analyze Examples

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## SQL Syntax

```sql
COALESCE(<nickname>, <name>)
```

## SQL Examples

```sql
SELECT COALESCE(nickname, first_name, 'Unknown') AS display_name FROM users;

┌──────────────┐
│ display_name │
├──────────────┤
│ Bob          │
│ Alice        │
│ Unknown      │
└──────────────┘
```
