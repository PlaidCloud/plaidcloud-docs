---
title: DEXP (Lakehouse v2)
description: DEXP — alias funkcji `EXP`. Zobacz [EXP](../exp/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dexp.md
---

Alias funkcji `EXP`. Zobacz [EXP](../exp/).

## Składnia Analyze

```python
func.dexp(1)
```

## Przykłady Analyze

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## Składnia SQL

```sql
DEXP(<x>)
```

## Przykłady SQL

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```
