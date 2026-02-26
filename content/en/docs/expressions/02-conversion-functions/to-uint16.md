---
title: TO_UINT16
---

Converts a value to UINT16 data type.

## Analyze Syntax

```python
func.to_uint16( <expr> )
```

## Analyze Examples

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL Syntax

```sql
TO_UINT16( <expr> )
```

## SQL Examples

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```