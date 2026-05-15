---
title: INSPECT_MV_META
description: INSPECT_MV_META — returns metadata about a materialized view - see syntax, examples, and output.
---

Returns metadata about a materialized view.

## Analyze Syntax

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Analyze Examples

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## SQL Syntax

```sql
INSPECT_MV_META(<db>, <mv>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
