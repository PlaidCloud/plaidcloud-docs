---
title: DIVNULL (Lakehouse v1)
description: DIVNULL — zwraca iloraz z dzielenia pierwszej liczby przez drugą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/divnull.md
---

Zwraca iloraz z dzielenia pierwszej liczby przez drugą. Zwraca NULL, jeśli druga liczba wynosi 0 lub NULL.

Zobacz też:

- [DIV](../div)
- [DIV0](../div0)

## Składnia Analyze

```python
func.divnull(<numerator>, <denominator>)
```

## Przykłady Analyze

```python
func.divnull(20, 6), func.divnull(20, 0), func.divnull(20, null)

┌───────────────────────────────────────────────────────────────────┐
│ func.divnull(20, 6)│ func.divnull(20, 0) │ func.divnull(20, null) │
├────────────────────┼─────────────────────┼────────────────────────┤
│ 3.3333333333333335 │ NULL                │ NULL                   │
└───────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
DIVNULL(<number1>, <number2>)
```

## Przykłady SQL

```sql
SELECT
  DIVNULL(20, 6),
  DIVNULL(20, 0),
  DIVNULL(20, NULL);

┌─────────────────────────────────────────────────────────┐
│   divnull(20, 6)   │ divnull(20, 0) │ divnull(20, null) │
├────────────────────┼────────────────┼───────────────────┤
│ 3.3333333333333335 │ NULL           │ NULL              │
└─────────────────────────────────────────────────────────┘
```
