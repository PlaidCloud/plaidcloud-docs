---
title: RAND (Lakehouse v2)
description: RAND — 0 이상 1 미만의 임의 부동 소수점 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

0 이상 1 미만의 임의 부동 소수점 값을 반환합니다.

## Analyze 구문

```python
func.rand([<seed>])
```

## Analyze 예제

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## SQL 구문

```sql
RAND([<seed>])
```

## SQL 예제

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
