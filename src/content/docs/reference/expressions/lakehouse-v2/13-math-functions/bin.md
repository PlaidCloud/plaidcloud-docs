---
title: BIN (Lakehouse v2)
description: BIN — returns the binary string representation of an integer.
---

Returns the binary string representation of an integer.

## Analyze Syntax

```python
func.bin(<x>)
```

## Analyze Examples

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## SQL Syntax

```sql
BIN(<x>)
```

## SQL Examples

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
