---
title: DIV（Lakehouse v1）
description: DIV — 最初の数を 2 番目の数で割った商を、より小さい最も近い整数に切り捨てて返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div.md
---

最初の数を 2 番目の数で割った商を、より小さい最も近い整数に切り捨てて返します。除算演算子 `//` と同等です。

関連項目： 

- [DIV0](../div0)
- [DIVNULL](../divnull)

## SQL 構文

```python
func.div(<numerator>, <denominator>)
```

## Analyze の例

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

## Analyze 構文

```sql
<number1> DIV <number2>
```

## エイリアス

- [INTDIV](../intdiv)

## SQL の例

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
