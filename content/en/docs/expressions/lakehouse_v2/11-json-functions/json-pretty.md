---
title: JSON_PRETTY
description: "Learn how to use the JSON_PRETTY json function in PlaidCloud Lakehouse. Formats a JSON value with indentation for readability - with syntax and examples."
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
