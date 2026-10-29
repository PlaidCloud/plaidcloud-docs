---
title: DEXP (Lakehouse v2)
description: DEXP — alias de `EXP`. Consulte [EXP](../exp/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dexp.md
---

Alias de `EXP`. Consulte [EXP](../exp/).

## Sintaxis de Analyze

```python
func.dexp(1)
```

## Ejemplos de Analyze

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## Sintaxis de SQL

```sql
DEXP(<x>)
```

## Ejemplos de SQL

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```
