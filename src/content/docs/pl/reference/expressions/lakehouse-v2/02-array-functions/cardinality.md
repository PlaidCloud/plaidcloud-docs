---
title: "CARDINALITY (Array, Lakehouse v2)"
description: CARDINALITY — zwraca liczbę elementów tablicy. Alias funkcji `ARRAY_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

Zwraca liczbę elementów tablicy. Alias funkcji `ARRAY_LENGTH`.

## Składnia Analyze

```python
func.cardinality([1, 2, 3])
```

## Przykłady Analyze

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Składnia SQL

```sql
CARDINALITY([1, 2, 3])
```

## Przykłady SQL

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
