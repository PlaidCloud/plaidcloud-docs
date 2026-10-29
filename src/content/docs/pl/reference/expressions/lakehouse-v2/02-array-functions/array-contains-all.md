---
title: ARRAY_CONTAINS_ALL (Lakehouse v2)
description: ARRAY_CONTAINS_ALL — sprawdza, czy tablica zawiera wszystkie elementy innej tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-all.md
---

Sprawdza, czy tablica zawiera wszystkie elementy innej tablicy.

## Składnia Analyze

```python
func.array_contains_all([1,2,3], [1,2])
```

## Przykłady Analyze

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## Przykłady SQL

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```
