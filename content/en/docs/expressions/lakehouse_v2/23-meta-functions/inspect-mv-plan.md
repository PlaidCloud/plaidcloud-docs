---
title: INSPECT_MV_PLAN
---

Returns the logical plan of a materialized view.

## Analyze Syntax

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Analyze Examples

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## SQL Syntax

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## SQL Examples

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
