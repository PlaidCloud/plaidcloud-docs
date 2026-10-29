---
title: SIGN (Lakehouse v1)
description: SIGN — zwraca znak argumentu jako -1, 0 lub 1, zależnie od tego, czy x jest ujemne, zerowe, czy dodatnie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

Zwraca znak argumentu jako -1, 0 lub 1, zależnie od tego, czy `x` jest ujemne, zerowe, czy dodatnie, lub NULL, jeśli argument miał wartość NULL.

## Składnia Analyze

```python
func.sign( <x> )
```

## Przykłady Analyze

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## Składnia SQL

```sql
SIGN( <x> )
```

## Przykłady SQL

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
