---
title: INSPECT_MV_REFRESH_INFO
description: "Learn how to use the INSPECT_MV_REFRESH_INFO meta function in PlaidCloud Lakehouse. Returns refresh information for a materialized view."
---

Returns refresh information for a materialized view.

## Analyze Syntax

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Analyze Examples

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## SQL Syntax

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
