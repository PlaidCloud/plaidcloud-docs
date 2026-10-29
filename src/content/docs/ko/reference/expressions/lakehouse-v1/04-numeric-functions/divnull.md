---
title: DIVNULL (Lakehouse v1)
description: DIVNULL — 첫 번째 수를 두 번째 수로 나눈 몫을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/divnull.md
---

첫 번째 수를 두 번째 수로 나눈 몫을 반환합니다. 두 번째 수가 0 또는 NULL이면 NULL을 반환합니다.

참고:

- [DIV](../div)
- [DIV0](../div0)

## Analyze 구문

```python
func.divnull(<numerator>, <denominator>)
```

## Analyze 예시

```python
func.divnull(20, 6), func.divnull(20, 0), func.divnull(20, null)

┌───────────────────────────────────────────────────────────────────┐
│ func.divnull(20, 6)│ func.divnull(20, 0) │ func.divnull(20, null) │
├────────────────────┼─────────────────────┼────────────────────────┤
│ 3.3333333333333335 │ NULL                │ NULL                   │
└───────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
DIVNULL(<number1>, <number2>)
```

## SQL 예시

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
