---
title: TO_UINT8
---

Converts a value to UINT8 data type.

## Analyze Syntax

```python
func.to_uint8( <expr> )
```

## Analyze Examples

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL Syntax

```sql
TO_UINT8( <expr> )
```

## SQL Examples

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```