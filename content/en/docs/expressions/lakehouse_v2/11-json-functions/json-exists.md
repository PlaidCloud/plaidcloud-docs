---
title: JSON_EXISTS
---

Checks whether a JSON document contains a value at a specified path.

## Analyze Syntax

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Analyze Examples

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
JSON_EXISTS(<data>, '$.name')
```

## SQL Examples

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
