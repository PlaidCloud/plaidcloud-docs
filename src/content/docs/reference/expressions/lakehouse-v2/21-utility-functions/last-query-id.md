---
title: LAST_QUERY_ID
description: "Learn how to use the LAST_QUERY_ID utility function in PlaidCloud Lakehouse. Returns the ID of the most recently executed query - with syntax and examples."
---

Returns the ID of the most recently executed query.

## Analyze Syntax

```python
func.last_query_id()
```

## Analyze Examples

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## SQL Syntax

```sql
LAST_QUERY_ID()
```

## SQL Examples

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
