---
title: CURRENT_WAREHOUSE (Lakehouse v2)
description: CURRENT_WAREHOUSE — Returns the name of the current warehouse.
---

Returns the name of the current warehouse.

## Analyze Syntax

```python
func.current_warehouse()
```

## Analyze Examples

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## SQL Syntax

```sql
CURRENT_WAREHOUSE()
```

## SQL Examples

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
