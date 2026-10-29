---
title: EXP (Lakehouse v1)
description: EXP — zwraca wartość e (podstawy logarytmów naturalnych) podniesioną do potęgi x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

Zwraca wartość e (podstawy logarytmów naturalnych) podniesioną do potęgi `x`.

## Składnia Analyze

```python
func.exp( <x> )
```

## Przykłady Analyze

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## Składnia SQL

```sql
EXP( <x> )
```

## Przykłady SQL

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
