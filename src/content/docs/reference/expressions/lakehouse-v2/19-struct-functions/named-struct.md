---
title: NAMED_STRUCT
description: NAMED_STRUCT — Creates a struct with specified field names and values.
---

Creates a struct with specified field names and values.

## Analyze Syntax

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Analyze Examples

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## SQL Syntax

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## SQL Examples

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
