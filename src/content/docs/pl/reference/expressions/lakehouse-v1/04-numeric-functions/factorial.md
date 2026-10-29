---
title: FACTORIAL (Lakehouse v1)
description: FACTORIAL — zwraca silnię x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

Zwraca silnię `x`. Jeśli `x` jest mniejsze lub równe 0, funkcja zwraca 0.

## Składnia Analyze

```python
func.factorial( <x> )
```

## Przykłady Analyze

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## Składnia SQL

```sql
FACTORIAL( <x> )
```

## Przykłady SQL

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
