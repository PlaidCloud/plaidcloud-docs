---
title: DIV0 (Lakehouse v1)
description: DIV0 — zwraca iloraz z dzielenia pierwszej liczby przez drugą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

Zwraca iloraz z dzielenia pierwszej liczby przez drugą. Zwraca 0, jeśli druga liczba wynosi 0.

Zobacz też:

- [DIV](../div)
- [DIVNULL](../divnull)

## Składnia Analyze

```python
func.div0(<numerator>, <denominator>)
```

## Przykłady Analyze

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
DIV0(<number1>, <number2>)
```

## Przykłady SQL

```sql
SELECT
  DIV0(20, 6),
  DIV0(20, 0),
  DIV0(20, NULL);

┌───────────────────────────────────────────────────┐
│     div0(20, 6)    │ div0(20, 0) │ div0(20, null) │
├────────────────────┼─────────────┼────────────────┤
│ 3.3333333333333335 │           0 │ NULL           │
└───────────────────────────────────────────────────┘
```
