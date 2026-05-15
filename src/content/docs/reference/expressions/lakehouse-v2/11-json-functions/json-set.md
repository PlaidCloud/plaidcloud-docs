---
title: JSON_SET
description: JSON_SET — sets a value in a JSON document at a specified path - see syntax, examples, and output.
---

Sets a value in a JSON document at a specified path.

## Analyze Syntax

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Analyze Examples

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## SQL Syntax

```sql
JSON_SET(<data>, '$.age', 31)
```

## SQL Examples

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
