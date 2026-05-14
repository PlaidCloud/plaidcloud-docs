---
title: VARIANT_GET
description: "Learn how to use the VARIANT_GET variant function in PlaidCloud Lakehouse. Extracts a typed value from a VARIANT object at a specified path."
---

Extracts a typed value from a VARIANT object at a specified path.

## Analyze Syntax

```python
func.variant_get(<variant>, <path>, <type>)
```

## Analyze Examples

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## SQL Syntax

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## SQL Examples

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
