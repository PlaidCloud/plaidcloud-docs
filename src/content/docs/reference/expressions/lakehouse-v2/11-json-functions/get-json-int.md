---
title: GET_JSON_INT
description: "Learn how to use the GET_JSON_INT json function in PlaidCloud Lakehouse. Extracts an integer value from a JSON object by a specified path."
---

Extracts an integer value from a JSON object by a specified path.

## Analyze Syntax

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Analyze Examples

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## SQL Syntax

```sql
GET_JSON_INT(<data>, '$.age')
```

## SQL Examples

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
