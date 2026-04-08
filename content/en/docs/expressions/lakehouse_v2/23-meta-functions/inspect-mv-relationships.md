---
title: INSPECT_MV_RELATIONSHIPS
description: "Learn how to use the INSPECT_MV_RELATIONSHIPS meta function in PlaidCloud Lakehouse. Returns dependency relationships for a materialized view."
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
