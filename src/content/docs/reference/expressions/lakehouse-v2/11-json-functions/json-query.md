---
title: JSON_QUERY
description: "Learn how to use the JSON_QUERY json function in PlaidCloud Lakehouse. Extracts a JSON value from a JSON document using a path expression."
---

Extracts a JSON value from a JSON document using a path expression.

## Analyze Syntax

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Analyze Examples

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## SQL Syntax

```sql
JSON_QUERY(<data>, '$.items')
```

## SQL Examples

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
