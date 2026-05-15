---
title: JSON_CONTAINS
description: JSON_CONTAINS — checks whether a JSON document contains a specific value at a path.
---

Checks whether a JSON document contains a specific value at a path.

## Analyze Syntax

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Analyze Examples

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## SQL Examples

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
