---
title: LN (Lakehouse v1)
description: LN — x의 자연로그, 즉 x의 밑이 e인 로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

`x`의 자연로그, 즉 `x`의 밑이 e인 로그를 반환합니다. x가 0.0E0 이하이면 NULL을 반환합니다.

## Analyze 구문

```python
func.ln( <x> )
```

## Analyze 예시

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL 구문

```sql
LN( <x> )
```

## SQL 예시

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
