---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — returns the size in bytes of a column value in its serialized form.
---

Returns the size in bytes of a column value in its serialized form.

## Analyze Syntax

```python
func.column_size(get_column(table, 'name'))
```

## Analyze Examples

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## SQL Syntax

```sql
COLUMN_SIZE(<expr>)
```

## SQL Examples

```sql
SELECT name, COLUMN_SIZE(name) FROM users LIMIT 3;

┌──────���┬───────────────────┐
│ name  │ column_size(name) │
├───────┼───────────────────┤
│ Alice │                 5 │
│ Bob   │                 3 │
│ Eve   │                 3 │
└───────┴───────────────────┘
```
