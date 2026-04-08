---
title: GET_JSON_BOOL
description: "Learn how to use the GET_JSON_BOOL json function in PlaidCloud Lakehouse. Extracts a boolean value from a JSON object by a specified path."
---

Extracts a boolean value from a JSON object by a specified path.

## Analyze Syntax

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Analyze Examples

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## SQL Examples

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
