---
title: DEXP (Lakehouse v2)
description: DEXP — alias de `EXP`. Voir [EXP](../exp/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dexp.md
---

Alias de `EXP`. Voir [EXP](../exp/).

## Syntaxe Analyze

```python
func.dexp(1)
```

## Exemples Analyze

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## Syntaxe SQL

```sql
DEXP(<x>)
```

## Exemples SQL

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```
