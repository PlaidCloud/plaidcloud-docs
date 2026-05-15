---
title: DSQRT (Lakehouse v2)
description: DSQRT — alias for `SQRT`. See [SQRT](sqrt).
---

Alias for `SQRT`. See [SQRT](sqrt).

## Analyze Syntax

```python
func.dsqrt(144)
```

## Analyze Examples

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## SQL Syntax

```sql
DSQRT(<x>)
```

## SQL Examples

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
