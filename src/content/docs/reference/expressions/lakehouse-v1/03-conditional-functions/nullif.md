---
title: NULLIF
description: "Learn how to use the NULLIF conditional function in PlaidCloud Lakehouse. Returns NULL if two expressions are equal. Includes syntax and examples."
---

Returns NULL if two expressions are equal. Otherwise return expr1. They must have the same data type.

## Analyze Syntax

```python
func.nullif(<expr1>, <expr2>)
```

## Analyze Examples

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## SQL Syntax

```sql
NULLIF(<expr1>, <expr2>)
```

## SQL Examples

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
