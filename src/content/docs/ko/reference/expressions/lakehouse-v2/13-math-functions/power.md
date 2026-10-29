---
title: POWER (Lakehouse v2)
description: POWER — 숫자를 다른 숫자만큼 거듭제곱한 값을 반환합니다. `POW`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

숫자를 다른 숫자만큼 거듭제곱한 값을 반환합니다. `POW`의 별칭입니다.

## Analyze 구문

```python
func.power(<x>, <y>)
```

## Analyze 예제

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQL 구문

```sql
POWER(<x>, <y>)
```

## SQL 예제

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
