---
title: DATABASE (Lakehouse v2)
description: DATABASE — returns the name of the current database.
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
