---
title: GET_QUERY_PROFILE
---

Returns the query profile for a specified query ID. Useful for performance analysis and debugging.

## Analyze Syntax

```python
func.get_query_profile('query_id')
```

## Analyze Examples

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## SQL Syntax

```sql
GET_QUERY_PROFILE(<query_id>)
```

## SQL Examples

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
