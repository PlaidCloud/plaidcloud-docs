---
title: TO_INT16
---

Converts a value to INT16 data type.

## Analyze Syntax

```python
func.to_int16( <expr> )
```

## Analyze Examples

```python
func.to_int16('123')

┌──────────────────────┐
│ func.to_int16('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL Syntax

```sql
TO_INT16( <expr> )
```

## SQL Examples

```sql
SELECT TO_INT16('123');

┌─────────────────┐
│ to_int16('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```