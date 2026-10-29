---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN — zwraca minimalny element tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

Zwraca minimalny element tablicy.

## Składnia Analyze

```python
func.array_min([3, 1, 4, 1, 5])
```

## Przykłady Analyze

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## Przykłady SQL

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
