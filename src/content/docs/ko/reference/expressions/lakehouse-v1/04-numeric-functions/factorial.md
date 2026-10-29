---
title: FACTORIAL (Lakehouse v1)
description: FACTORIAL — x의 팩토리얼 로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

`x`의 팩토리얼 로그를 반환합니다. `x`가 0 이하이면 0을 반환합니다.

## Analyze 구문

```python
func.factorial( <x> )
```

## Analyze 예시

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## SQL 구문

```sql
FACTORIAL( <x> )
```

## SQL 예시

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
