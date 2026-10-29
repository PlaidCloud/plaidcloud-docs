---
title: DSQRT (Lakehouse v2)
description: DSQRT — alias de `SQRT`. Consulte [SQRT](../sqrt/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dsqrt.md
---

Alias de `SQRT`. Consulte [SQRT](../sqrt/).

## Sintaxe do Analyze

```python
func.dsqrt(144)
```

## Exemplos do Analyze

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## Sintaxe SQL

```sql
DSQRT(<x>)
```

## Exemplos de SQL

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
