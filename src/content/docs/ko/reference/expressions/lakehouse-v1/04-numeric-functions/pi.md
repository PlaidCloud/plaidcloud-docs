---
title: PI (Lakehouse v1)
description: PI — π 값을 부동 소수점 값으로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

π 값을 부동 소수점 값으로 반환합니다.

## Analyze 구문

```python
func.pi()
```

## Analyze 예시

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## SQL 구문

```sql
PI()
```

## SQL 예시

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
