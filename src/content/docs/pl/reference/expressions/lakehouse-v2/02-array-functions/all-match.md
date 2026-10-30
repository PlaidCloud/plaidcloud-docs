---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH — zwraca TRUE, jeśli wszystkie elementy tablicy spełniają podany predykat.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

Zwraca TRUE, jeśli wszystkie elementy tablicy spełniają podany predykat.

## Składnia Analyze

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Przykłady Analyze

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## Przykłady SQL

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
