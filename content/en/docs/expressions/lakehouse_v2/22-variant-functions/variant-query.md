---
title: VARIANT_QUERY
description: "Use the VARIANT_QUERY variant function in PlaidCloud Lakehouse. Queries a value from a VARIANT object using a path expression and returns a VARIANT."
---

Queries a value from a VARIANT object using a path expression and returns a VARIANT.

## Analyze Syntax

```python
func.variant_query(<variant>, <path>)
```

## Analyze Examples

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## SQL Syntax

```sql
VARIANT_QUERY(<variant>, <path>)
```

## SQL Examples

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
