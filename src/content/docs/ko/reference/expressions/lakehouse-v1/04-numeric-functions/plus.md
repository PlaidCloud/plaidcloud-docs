---
title: PLUS (Lakehouse v1)
description: PLUS — 두 숫자 또는 십진수 값의 합을 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

두 숫자 또는 십진수 값의 합을 계산합니다.

## Analyze 구문

```python
func.plus(<number1>, <number2>)
```

## Analyze 예시

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## SQL 구문

```sql
PLUS(<number1>, <number2>)
```

## 별칭

- [ADD](../add)

## SQL 예시

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```
