---
title: COT (Lakehouse v2)
description: COT — returns the cotangent of a number in radians.
---

Returns the cotangent of a number in radians.

## Analyze Syntax

```python
func.cot(<x>)
```

## Analyze Examples

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## SQL Syntax

```sql
COT(<x>)
```

## SQL Examples

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
