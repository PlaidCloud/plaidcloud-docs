---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS — returns dependency relationships for a materialized view.
---

Returns dependency relationships for a materialized view.

## Analyze Syntax

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Analyze Examples

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## SQL Syntax

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
