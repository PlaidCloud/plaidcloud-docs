---
title: JSON_EACH
description: "Learn how to use the JSON_EACH json function in PlaidCloud Lakehouse. Expands the top-level JSON object into a set of key-value pairs."
---

Expands the top-level JSON object into a set of key-value pairs.

## Analyze Syntax

```python
func.json_each(get_column(table, 'data'))
```

## Analyze Examples

```python
func.json_each(get_column(table, 'data'))
```

## SQL Syntax

```sql
JSON_EACH(<data>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
