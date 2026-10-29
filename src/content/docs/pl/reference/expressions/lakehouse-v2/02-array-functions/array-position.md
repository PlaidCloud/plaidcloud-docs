---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION — zwraca pozycję pierwszego wystąpienia elementu (numerowanie od 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

Zwraca pozycję pierwszego wystąpienia elementu (numerowanie od 1).

## Składnia Analyze

```python
func.array_position([10, 20, 30], 20)
```

## Przykłady Analyze

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## Składnia SQL

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## Przykłady SQL

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
