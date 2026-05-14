---
title: VARIANT_TYPEOF
description: "Learn how to use the VARIANT_TYPEOF variant function in PlaidCloud Lakehouse. Returns the type name of a VARIANT value as a string - with syntax and examples."
---

Returns the type name of a VARIANT value as a string.

## Analyze Syntax

```python
func.variant_typeof(<variant>)
```

## Analyze Examples

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## SQL Syntax

```sql
VARIANT_TYPEOF(<variant>)
```

## SQL Examples

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
