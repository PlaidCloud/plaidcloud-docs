---
title: STDDEV (Lakehouse v2)
description: STDDEV — zwraca odchylenie standardowe populacji. Alias funkcji `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

Zwraca odchylenie standardowe populacji. Alias funkcji `STDDEV_POP`.

## Składnia Analyze

```python
func.stddev(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Składnia SQL

```sql
STDDEV(<score>)
```

## Przykłady SQL

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
