---
title: JSON_REMOVE
description: "Learn how to use the JSON_REMOVE json function in PlaidCloud Lakehouse. Removes an element from a JSON document at a specified path - with syntax and examples."
---

Removes an element from a JSON document at a specified path.

## Analyze Syntax

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Analyze Examples

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## SQL Syntax

```sql
JSON_REMOVE(<data>, '$.temp')
```

## SQL Examples

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
