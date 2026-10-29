---
title: DIV0 (Lakehouse v1)
description: DIV0 — 첫 번째 수를 두 번째 수로 나눈 몫을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

첫 번째 수를 두 번째 수로 나눈 몫을 반환합니다. 두 번째 수가 0이면 0을 반환합니다.

참고:

- [DIV](../div)
- [DIVNULL](../divnull)

## Analyze 구문

```python
func.div0(<numerator>, <denominator>)
```

## Analyze 예시

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
DIV0(<number1>, <number2>)
```

## SQL 예시

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
