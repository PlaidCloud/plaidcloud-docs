---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: ARRAY_TRANSFORM — zwraca tablicę będącą wynikiem zastosowania funkcji lambda do każdego elementu tablicy wejściowej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

Zwraca tablicę będącą wynikiem zastosowania funkcji lambda do każdego elementu tablicy wejściowej.

## Składnia Analyze

```python
func.array_transform( <array>, <lambda> )
```

## Przykłady Analyze

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## Aliasy

- [ARRAY_APPLY](../array-apply)

## Przykłady SQL

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
