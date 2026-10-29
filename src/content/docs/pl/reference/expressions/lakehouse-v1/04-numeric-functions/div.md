---
title: DIV (Lakehouse v1)
description: DIV — zwraca iloraz z dzielenia pierwszej liczby przez drugą, zaokrąglony w dół do najbliższej mniejszej liczby całkowitej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div.md
---

Zwraca iloraz z dzielenia pierwszej liczby przez drugą, zaokrąglony w dół do najbliższej mniejszej liczby całkowitej. Odpowiada operatorowi dzielenia `//`.

Zobacz też: 

- [DIV0](../div0)
- [DIVNULL](../divnull)

## Składnia SQL

```python
func.div(<numerator>, <denominator>)
```

## Przykłady Analyze

```python
# Equivalent to the division operator "//"
func.div(6.1, 2)

┌───────────────────────────────┐
│ func.div(6.1, 2) │ (6.1 // 2) │
├──────────────────┼────────────┤
│                3 │          3 │
└───────────────────────────────┘

# Error when divided by 0
error: APIError: ResponseError with 1006: divided by zero while evaluating function `div(6.1, 0)`
```

## Składnia Analyze

```sql
<number1> DIV <number2>
```

## Aliasy

- [INTDIV](../intdiv)

## Przykłady SQL

```sql
-- Equivalent to the division operator "//"
SELECT 6.1 DIV 2, 6.1//2;

┌──────────────────────────┐
│ (6.1 div 2) │ (6.1 // 2) │
├─────────────┼────────────┤
│           3 │          3 │
└──────────────────────────┘

SELECT 6.1 DIV 2, INTDIV(6.1, 2), 6.1 DIV NULL;

┌───────────────────────────────────────────────┐
│ (6.1 div 2) │ intdiv(6.1, 2) │ (6.1 div null) │
├─────────────┼────────────────┼────────────────┤
│           3 │              3 │ NULL           │
└───────────────────────────────────────────────┘

-- Error when divided by 0
root@localhost:8000/default> SELECT 6.1 DIV 0;
error: APIError: ResponseError with 1006: divided by zero while evaluating function `div(6.1, 0)`
```
