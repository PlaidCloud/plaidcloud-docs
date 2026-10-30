---
title: LEAST (Lakehouse v2)
description: LEAST — zwraca najmniejszą wartość z listy wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/least.md
---

Zwraca najmniejszą wartość z listy wartości.

## Składnia Analyze

```python
func.least(<val1>, <val2>[, ...])
```

## Przykłady Analyze

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
LEAST(<val1>, <val2>[, ...])
```

## Przykłady SQL

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
