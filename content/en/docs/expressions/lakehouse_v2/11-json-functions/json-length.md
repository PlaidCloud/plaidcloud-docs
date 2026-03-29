---
title: JSON_LENGTH
---

Returns the number of elements in a JSON object or array.

## Analyze Syntax

```python
func.json_length(get_column(table, 'data'))
```

## Analyze Examples

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## SQL Syntax

```sql
JSON_LENGTH(<data>)
```

## SQL Examples

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
