---
title: RANDOM (Lakehouse v2)
description: RANDOM — 0과 1 사이의 임의 부동 소수점 값을 반환합니다. `RAND`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

0과 1 사이의 임의 부동 소수점 값을 반환합니다. `RAND`의 별칭입니다.

## Analyze 구문

```python
func.random([<seed>])
```

## Analyze 예제

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## SQL 구문

```sql
RANDOM([<seed>])
```

## SQL 예제

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
