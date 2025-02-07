---
title: TO_UINT32
---

Converts a value to UINT32 data type.

## Analyze Syntax

```python
func.to_uint32( <expr> )
```

## Analyze Examples

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL Syntax

```sql
TO_UINT32( <expr> )
```

## SQL Examples

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```