---
title: DROUND
description: "Learn how to use the DROUND math function in PlaidCloud Lakehouse. Alias for `ROUND`. See [ROUND](round) - see syntax, examples, and output."
---

Alias for `ROUND`. See [ROUND](round).

## Analyze Syntax

```python
func.dround(3.14159, 2)
```

## Analyze Examples

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## SQL Syntax

```sql
DROUND(<x>)
```

## SQL Examples

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
