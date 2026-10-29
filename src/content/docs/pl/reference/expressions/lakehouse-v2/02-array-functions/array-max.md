---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX — zwraca maksymalny element tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-max.md
---

Zwraca maksymalny element tablicy.

## Składnia Analyze

```python
func.array_max([3, 1, 4, 1, 5])
```

## Przykłady Analyze

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## Składnia SQL

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## Przykłady SQL

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
