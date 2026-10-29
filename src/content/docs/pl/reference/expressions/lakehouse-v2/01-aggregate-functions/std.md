---
title: STD (Lakehouse v2)
description: STD — zwraca odchylenie standardowe populacji. Alias funkcji `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/std.md
---

Zwraca odchylenie standardowe populacji. Alias funkcji `STDDEV_POP`.

## Składnia Analyze

```python
func.std(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Składnia SQL

```sql
STD(<score>)
```

## Przykłady SQL

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
