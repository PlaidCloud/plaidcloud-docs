---
title: DFLOOR
description: "Learn how to use the DFLOOR math function in PlaidCloud Lakehouse. Alias for `FLOOR`. See [FLOOR](floor) - see syntax, examples, and output."
---

Alias for `FLOOR`. See [FLOOR](floor).

## Analyze Syntax

```python
func.dfloor(3.7)
```

## Analyze Examples

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## SQL Syntax

```sql
DFLOOR(<x>)
```

## SQL Examples

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
