---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP — zwraca wariancję populacji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

Zwraca wariancję populacji.

## Składnia Analyze

```python
func.variance_pop(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Składnia SQL

```sql
VARIANCE_POP(<score>)
```

## Przykłady SQL

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
