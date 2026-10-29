---
title: COVAR_POP (Lakehouse v2)
description: COVAR_POP — zwraca kowariancję populacji dwóch wyrażeń.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

Zwraca kowariancję populacji dwóch wyrażeń.

## Składnia Analyze

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Przykłady Analyze

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## Składnia SQL

```sql
COVAR_POP(<y>, <x>)
```

## Przykłady SQL

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
