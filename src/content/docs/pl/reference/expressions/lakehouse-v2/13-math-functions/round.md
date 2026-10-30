---
title: ROUND (Lakehouse v2)
description: ROUND — zaokrągla liczbę do określonej liczby miejsc dziesiętnych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

Zaokrągla liczbę do określonej liczby miejsc dziesiętnych.

## Składnia Analyze

```python
func.round(<x>[, <d>])
```

## Przykłady Analyze

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Składnia SQL

```sql
ROUND(<x>[, <d>])
```

## Przykłady SQL

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
