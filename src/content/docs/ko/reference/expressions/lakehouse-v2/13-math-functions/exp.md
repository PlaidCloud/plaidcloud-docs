---
title: EXP (Lakehouse v2)
description: EXP — e를 숫자만큼 거듭제곱한 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

e를 숫자만큼 거듭제곱한 값을 반환합니다.

## Analyze 구문

```python
func.exp(<x>)
```

## Analyze 예제

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## SQL 구문

```sql
EXP(<x>)
```

## SQL 예제

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
