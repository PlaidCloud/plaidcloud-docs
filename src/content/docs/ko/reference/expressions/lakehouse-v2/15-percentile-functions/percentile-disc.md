---
title: "PERCENTILE_DISC (백분위수, Lakehouse v2)"
description: "PlaidCloud Lakehouse에서 PERCENTILE_DISC 백분위수 함수를 사용합니다. 누적 분포가 지정한 백분위수 이상인 가장 작은 값을 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-disc.md
---

누적 분포가 지정한 백분위수 이상인 가장 작은 값을 반환합니다.

## Analyze 구문

```python
func.percentile_disc(<percentile>)
```

## Analyze 예제

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000  │
└───────┘
```

## SQL 구문

```sql
PERCENTILE_DISC(<percentile>)
```

## SQL 예제

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
