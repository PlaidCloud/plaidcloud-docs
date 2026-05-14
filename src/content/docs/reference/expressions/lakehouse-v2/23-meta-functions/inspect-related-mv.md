---
title: INSPECT_RELATED_MV
description: "Learn how to use the INSPECT_RELATED_MV meta function in PlaidCloud Lakehouse. Returns materialized views related to a table - with syntax and examples."
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
