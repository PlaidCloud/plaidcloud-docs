---
title: ARRAY_FILTER (Lakehouse v1)
description: ARRAY_FILTER — tworzy tablicę z tych elementów tablicy wejściowej, dla których funkcja lambda zwraca true.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

Tworzy tablicę z tych elementów tablicy wejściowej, dla których funkcja lambda zwraca true.

## Składnia Analyze

```python
func.array_filter( <array>, <lambda> )
```

## Przykłady Analyze

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## Przykłady SQL

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```
