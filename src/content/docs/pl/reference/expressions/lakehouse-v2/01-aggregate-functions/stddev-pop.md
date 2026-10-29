---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP — zwraca odchylenie standardowe populacji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

Zwraca odchylenie standardowe populacji.

## Składnia Analyze

```python
func.stddev_pop(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Składnia SQL

```sql
STDDEV_POP(<score>)
```

## Przykłady SQL

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
