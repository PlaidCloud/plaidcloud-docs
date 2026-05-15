---
title: GET_JSON_OBJECT
description: GET_JSON_OBJECT — extracts a JSON object from a JSON string by a specified path.
---

Extracts a JSON object from a JSON string by a specified path.

## Analyze Syntax

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Analyze Examples

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL Syntax

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## SQL Examples

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
