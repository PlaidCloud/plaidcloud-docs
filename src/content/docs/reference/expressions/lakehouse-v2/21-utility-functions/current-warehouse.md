---
title: CURRENT_WAREHOUSE
description: "Learn how to use the CURRENT_WAREHOUSE utility function in PlaidCloud Lakehouse. Returns the name of the current warehouse - with syntax and examples."
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
