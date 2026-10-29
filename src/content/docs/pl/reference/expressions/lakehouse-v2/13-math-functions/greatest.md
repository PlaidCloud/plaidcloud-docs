---
title: GREATEST (Lakehouse v2)
description: GREATEST — zwraca największą wartość z listy wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

Zwraca największą wartość z listy wartości.

## Składnia Analyze

```python
func.greatest(<val1>, <val2>[, ...])
```

## Przykłady Analyze

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## Składnia SQL

```sql
GREATEST(<val1>, <val2>[, ...])
```

## Przykłady SQL

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
