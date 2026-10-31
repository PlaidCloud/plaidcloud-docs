---
title: DSQRT (Lakehouse v2)
description: DSQRT – Alias für `SQRT`. Siehe [SQRT](../sqrt/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dsqrt.md
---

Alias für `SQRT`. Siehe [SQRT](../sqrt/).

## Analyze-Syntax

```python
func.dsqrt(144)
```

## Analyze-Beispiele

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## SQL-Syntax

```sql
DSQRT(<x>)
```

## SQL-Beispiele

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
