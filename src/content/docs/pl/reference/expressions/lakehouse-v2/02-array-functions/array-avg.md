---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG — zwraca średnią elementów tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

Zwraca średnią elementów tablicy.

## Składnia Analyze

```python
func.array_avg([1, 2, 3, 4])
```

## Przykłady Analyze

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## Składnia SQL

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## Przykłady SQL

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
