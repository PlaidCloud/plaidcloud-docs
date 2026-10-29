---
title: EXP (Lakehouse v1)
description: EXP — e(자연로그의 밑)의 x제곱 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

e(자연로그의 밑)의 `x`제곱 값을 반환합니다.

## Analyze 구문

```python
func.exp( <x> )
```

## Analyze 예시

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## SQL 구문

```sql
EXP( <x> )
```

## SQL 예시

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
