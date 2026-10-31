---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH — zwraca liczbę elementów tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

Zwraca liczbę elementów tablicy.

## Składnia Analyze

```python
func.array_length([1, 2, 3])
```

## Przykłady Analyze

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Składnia SQL

```sql
ARRAY_LENGTH([1, 2, 3])
```

## Przykłady SQL

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
