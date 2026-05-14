---
title: DATABASE
description: "Learn how to use the DATABASE utility function in PlaidCloud Lakehouse. Returns the name of the current database - see syntax, examples, and output."
---

Returns the name of the current database.

## Analyze Syntax

```python
func.database()
```

## Analyze Examples

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## SQL Syntax

```sql
DATABASE()
```

## SQL Examples

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
