---
title: "PERCENTILE_DISC (Percentyl, Lakehouse v2)"
description: "Użyj funkcji percentyli PERCENTILE_DISC w PlaidCloud Lakehouse. Zwraca najmniejszą wartość, której dystrybuanta jest większa lub równa podanemu percentylowi."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-disc.md
---

Zwraca najmniejszą wartość, której dystrybuanta jest większa lub równa podanemu percentylowi.

## Składnia Analyze

```python
func.percentile_disc(<percentile>)
```

## Przykłady Analyze

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000  │
└───────┘
```

## Składnia SQL

```sql
PERCENTILE_DISC(<percentile>)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
