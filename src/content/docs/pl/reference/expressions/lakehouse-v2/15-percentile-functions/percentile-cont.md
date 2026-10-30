---
title: "PERCENTILE_CONT (Percentyl, Lakehouse v2)"
description: PERCENTILE_CONT — zwraca interpolowaną wartość percentyla na podstawie rozkładu ciągłego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

Zwraca interpolowaną wartość percentyla na podstawie rozkładu ciągłego.

## Składnia Analyze

```python
func.percentile_cont(<percentile>)
```

## Przykłady Analyze

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## Składnia SQL

```sql
PERCENTILE_CONT(<percentile>)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
