---
title: XXHASH32
---

Calculates an xxHash32 32-bit hash value for a string. The value is returned as a UInt32 or NULL if the argument was NULL.

## Analyze Syntax

```python
func.xxhash32(<expr>)
```

## Analyze Examples

```python
func.xxhash32('1234567890')

+-----------------------------+
| func.xxhash32('1234567890') |
+-----------------------------+
|                  3896585587 |
+-----------------------------+
```

## SQL Syntax

```sql
XXHASH32(<expr>)
```

## SQL Examples

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```