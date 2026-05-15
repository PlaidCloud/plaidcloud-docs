---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV — Returns materialized views related to a table.
---

Returns materialized views related to a table.

## Analyze Syntax

```python
func.inspect_related_mv(<db>, <table>)
```

## Analyze Examples

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## SQL Syntax

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
