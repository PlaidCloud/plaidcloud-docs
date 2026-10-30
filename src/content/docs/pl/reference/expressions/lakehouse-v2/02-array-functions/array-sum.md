---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM — zwraca sumę elementów tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

Zwraca sumę elementów tablicy.

## Składnia Analyze

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Przykłady Analyze

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## Składnia SQL

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## Przykłady SQL

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
