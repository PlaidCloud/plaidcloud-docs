---
title: ARRAY_UNIQUE_AGG
---

Aggregates values into an array of distinct values.

## Analyze Syntax

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Analyze Examples

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL Syntax

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## SQL Examples

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
