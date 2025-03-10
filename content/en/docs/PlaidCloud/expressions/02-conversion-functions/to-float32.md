---
title: TO_FLOAT32
---

Converts a value to FLOAT32 data type.

## Analyze Syntax

```python
func.to_float32( <expr> )
```

## Analyze Examples

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL Syntax

```sql
TO_FLOAT32( <expr> )
```

## SQL Examples

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```