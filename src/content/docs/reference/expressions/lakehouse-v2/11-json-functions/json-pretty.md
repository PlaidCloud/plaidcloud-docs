---
title: JSON_PRETTY
description: JSON_PRETTY — Formats a JSON value with indentation for readability.
---

Formats a JSON value with indentation for readability.

## Analyze Syntax

```python
func.json_pretty(get_column(table, 'data'))
```

## Analyze Examples

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## SQL Syntax

```sql
JSON_PRETTY(<data>)
```

## SQL Examples

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
