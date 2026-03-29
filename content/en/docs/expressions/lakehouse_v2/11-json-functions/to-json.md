---
title: TO_JSON
---

Converts a SQL value to a JSON value.

## Analyze Syntax

```python
func.to_json(get_column(table, 'struct_col'))
```

## Analyze Examples

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL Syntax

```sql
TO_JSON(<struct_col>)
```

## SQL Examples

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
