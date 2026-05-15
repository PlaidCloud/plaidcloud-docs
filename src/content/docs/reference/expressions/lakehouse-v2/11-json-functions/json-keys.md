---
title: JSON_KEYS
description: JSON_KEYS — Returns the keys of the top-level JSON object as a JSON array.
---

Returns the keys of the top-level JSON object as a JSON array.

## Analyze Syntax

```python
func.json_keys(get_column(table, 'data'))
```

## Analyze Examples

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## SQL Syntax

```sql
JSON_KEYS(<data>)
```

## SQL Examples

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
