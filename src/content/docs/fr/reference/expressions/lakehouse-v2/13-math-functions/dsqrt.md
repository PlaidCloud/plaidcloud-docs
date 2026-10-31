---
title: DSQRT (Lakehouse v2)
description: DSQRT — alias de `SQRT`. Voir [SQRT](../sqrt/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dsqrt.md
---

Alias de `SQRT`. Voir [SQRT](../sqrt/).

## Syntaxe Analyze

```python
func.dsqrt(144)
```

## Exemples Analyze

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## Syntaxe SQL

```sql
DSQRT(<x>)
```

## Exemples SQL

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
