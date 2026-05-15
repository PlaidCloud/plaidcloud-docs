---
title: GET_JSON_STRING
description: GET_JSON_STRING — extracts a string value from a JSON object by a specified path.
---

Extracts a string value from a JSON object by a specified path.

## Analyze Syntax

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Analyze Examples

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## SQL Syntax

```sql
GET_JSON_STRING(<data>, '$.name')
```

## SQL Examples

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
