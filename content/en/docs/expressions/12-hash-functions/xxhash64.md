---
title: XXHASH64
---

Calculates an xxHash64 64-bit hash value for a string. The value is returned as a UInt64 or NULL if the argument was NULL.

## Analyze Syntax

```python
func.xxhash64(<expr>)
```

## Analyze Examples

```python
func.xxhash64('1234567890')

+-----------------------------+
| func.xxhash64('1234567890') |
+-----------------------------+
|        12237639266330420150 |
+-----------------------------+
```

## SQL Syntax

```sql
XXHASH64(<expr>)
```

## SQL Examples

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```