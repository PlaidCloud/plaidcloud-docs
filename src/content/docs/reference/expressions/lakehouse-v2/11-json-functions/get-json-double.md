---
title: GET_JSON_DOUBLE
description: GET_JSON_DOUBLE — extracts a double value from a JSON object by a specified path.
---

Extracts a double value from a JSON object by a specified path.

## Analyze Syntax

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Analyze Examples

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## SQL Syntax

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## SQL Examples

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
