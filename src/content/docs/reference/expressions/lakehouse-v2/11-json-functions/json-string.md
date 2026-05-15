---
title: JSON_STRING
description: JSON_STRING — converts a JSON value to a JSON-encoded string - see syntax, examples, and output.
---

Converts a JSON value to a JSON-encoded string.

## Analyze Syntax

```python
func.json_string(get_column(table, 'data'))
```

## Analyze Examples

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## SQL Syntax

```sql
JSON_STRING(<data>)
```

## SQL Examples

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
