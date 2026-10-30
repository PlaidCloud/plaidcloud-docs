---
title: EXP (Lakehouse v2)
description: EXP — zwraca e podniesione do potęgi podanej liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

Zwraca e podniesione do potęgi podanej liczby.

## Składnia Analyze

```python
func.exp(<x>)
```

## Przykłady Analyze

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## Składnia SQL

```sql
EXP(<x>)
```

## Przykłady SQL

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
