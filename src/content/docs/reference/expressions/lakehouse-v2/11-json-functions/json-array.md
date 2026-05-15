---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — creates a JSON array from a list of values.
---

Creates a JSON array from a list of values.

## Analyze Syntax

```python
func.json_array(1, 'hello', None)
```

## Analyze Examples

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## SQL Syntax

```sql
JSON_ARRAY(1, 'hello', None)
```

## SQL Examples

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
