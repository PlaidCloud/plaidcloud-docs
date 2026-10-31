---
title: CONTAINS (Lakehouse v1)
description: CONTAINS — sprawdza, czy tablica zawiera określony element.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

Sprawdza, czy tablica zawiera określony element.


## Składnia Analyze

```python
func.contains( <array>, <element> )
```

## Przykłady Analyze

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## Składnia SQL

```sql
CONTAINS( <array>, <element> )
```

## Aliasy

- [ARRAY_CONTAINS](../array-contains)

## Przykłady SQL

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```
