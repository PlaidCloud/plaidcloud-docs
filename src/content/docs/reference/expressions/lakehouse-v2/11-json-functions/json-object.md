---
title: JSON_OBJECT
description: "Learn how to use the JSON_OBJECT json function in PlaidCloud Lakehouse. Creates a JSON object from key-value pairs - see syntax, examples, and output."
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
