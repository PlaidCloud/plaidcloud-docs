---
title: LAST_QUERY_ID
---

Returns the last query ID of query in current session, index can be (-1, 1, 1+2)..., out of range index will return empty string.

## Analyze Syntax

```python
func.last_query_id(<index>)
```

## Analyze Examples

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## SQL Syntax

```sql
LAST_QUERY_ID(<index>)
```

## SQL Examples

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```