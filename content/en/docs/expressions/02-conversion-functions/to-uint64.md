---
title: TO_UINT64
---

Converts a value to UINT64 data type.

## Analyze Syntax

```python
func.to_uint64( <expr> )
```

## Analyze Examples

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL Syntax

```sql
TO_UINT64( <expr> )
```

## SQL Examples

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```