---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS — sprawdza, czy tablica zawiera określony element.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

Sprawdza, czy tablica zawiera określony element.

## Składnia Analyze

```python
func.array_contains([1, 2, 3], 2)
```

## Przykłady Analyze

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## Przykłady SQL

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
