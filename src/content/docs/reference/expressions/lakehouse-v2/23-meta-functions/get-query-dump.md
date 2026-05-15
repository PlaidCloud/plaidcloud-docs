---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP — returns a query dump for diagnostic purposes.
---

Returns a query dump for diagnostic purposes.

## Analyze Syntax

```python
func.get_query_dump(<query>)
```

## Analyze Examples

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## SQL Syntax

```sql
GET_QUERY_DUMP(<query>)
```

## SQL Examples

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
