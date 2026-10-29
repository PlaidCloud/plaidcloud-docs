---
title: DIV (Lakehouse v1)
description: DIV — 첫 번째 수를 두 번째 수로 나눈 몫을 반환하며, 가장 가까운 작은 정수로 내림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div.md
---

첫 번째 수를 두 번째 수로 나눈 몫을 반환하며, 가장 가까운 작은 정수로 내림합니다. 나눗셈 연산자 `//`와 같습니다.

참고: 

- [DIV0](../div0)
- [DIVNULL](../divnull)

## SQL 구문

```python
func.div(<numerator>, <denominator>)
```

## Analyze 예시

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

## Analyze 구문

```sql
<number1> DIV <number2>
```

## 별칭

- [INTDIV](../intdiv)

## SQL 예시

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
