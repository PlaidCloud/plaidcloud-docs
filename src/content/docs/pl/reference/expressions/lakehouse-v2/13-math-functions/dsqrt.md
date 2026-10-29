---
title: DSQRT (Lakehouse v2)
description: DSQRT — alias funkcji `SQRT`. Zobacz [SQRT](../sqrt/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dsqrt.md
---

Alias funkcji `SQRT`. Zobacz [SQRT](../sqrt/).

## Składnia Analyze

```python
func.dsqrt(144)
```

## Przykłady Analyze

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## Składnia SQL

```sql
DSQRT(<x>)
```

## Przykłady SQL

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
