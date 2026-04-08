---
title: TO_FLOAT64
description: "Learn how to use the TO_FLOAT64 conversion function in PlaidCloud Lakehouse. Converts a value to FLOAT64 data type. Includes syntax and examples."
---

Converts a value to FLOAT64 data type.

## Analyze Syntax

```python
func.to_float64( <expr> )
```

## Analyze Examples

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL Syntax

```sql
TO_FLOAT64( <expr> )
```

## SQL Examples

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```