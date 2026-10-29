---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP — zwraca odchylenie standardowe próby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

Zwraca odchylenie standardowe próby.

## Składnia Analyze

```python
func.stddev_samp(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## Składnia SQL

```sql
STDDEV_SAMP(<score>)
```

## Przykłady SQL

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
