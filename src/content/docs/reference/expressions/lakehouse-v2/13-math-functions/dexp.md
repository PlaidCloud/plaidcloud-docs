---
title: DEXP (Lakehouse v2)
description: DEXP — alias for `EXP`. See [EXP](../exp/).
---

Alias for `EXP`. See [EXP](../exp/).

## Analyze Syntax

```python
func.dexp(1)
```

## Analyze Examples

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## SQL Syntax

```sql
DEXP(<x>)
```

## SQL Examples

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```
