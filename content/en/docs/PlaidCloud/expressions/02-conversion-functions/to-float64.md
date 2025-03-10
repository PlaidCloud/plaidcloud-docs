---
title: TO_FLOAT64
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