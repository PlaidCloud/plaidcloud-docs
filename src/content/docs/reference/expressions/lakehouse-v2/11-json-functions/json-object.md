---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — creates a JSON object from key-value pairs.
---

Creates a JSON object from key-value pairs.

## Analyze Syntax

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Analyze Examples

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL Syntax

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## SQL Examples

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
