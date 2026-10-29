---
title: POWER (Lakehouse v2)
description: POWER — zwraca liczbę podniesioną do potęgi o wykładniku równym drugiej liczbie. Alias funkcji `POW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

Zwraca liczbę podniesioną do potęgi o wykładniku równym drugiej liczbie. Alias funkcji `POW`.

## Składnia Analyze

```python
func.power(<x>, <y>)
```

## Przykłady Analyze

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Składnia SQL

```sql
POWER(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
