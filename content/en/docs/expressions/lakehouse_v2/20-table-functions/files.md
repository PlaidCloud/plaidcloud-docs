---
title: FILES
---

Reads data directly from cloud storage files.

## Analyze Syntax

```python
func.files(<path_or_properties>)
```

## Analyze Examples

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## SQL Syntax

```sql
FILES(<path_or_properties>)
```

## SQL Examples

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
