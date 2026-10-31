---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH — zwraca TRUE, jeśli dowolny element tablicy spełnia podany predykat.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

Zwraca TRUE, jeśli dowolny element tablicy spełnia podany predykat.

## Składnia Analyze

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Przykłady Analyze

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## Przykłady SQL

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
