---
title: BITNOT (Lakehouse v2)
description: BITNOT — returns the bitwise NOT of a numeric value.
---

Returns the bitwise NOT of a numeric value.

## Analyze Syntax

```python
func.bitnot(<x>)
```

## Analyze Examples

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## SQL Syntax

```sql
BITNOT(<x>)
```

## SQL Examples

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
