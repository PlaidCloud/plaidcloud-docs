---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF — Returns the type name of a VARIANT value as a string.
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
