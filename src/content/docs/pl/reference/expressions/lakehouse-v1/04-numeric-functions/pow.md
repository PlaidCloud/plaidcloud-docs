---
title: POW (Lakehouse v1)
description: POW — zwraca wartość x podniesioną do potęgi y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

Zwraca wartość `x` podniesioną do potęgi `y`. 

## Składnia Analyze

```python
func.pow( <x, y> )
```

## Przykłady Analyze

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## Składnia SQL

```sql
POW( <x, y> )
```

## Aliasy

- [POWER](../power)

## Przykłady SQL

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```
