---
title: PARSE_JSON
---

Parses a JSON string and returns a JSON value.

## Analyze Syntax

```python
func.parse_json('{"a":1}')
```

## Analyze Examples

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL Syntax

```sql
PARSE_JSON('{"a":1}')
```

## SQL Examples

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
