---
title: "PERCENTILE_CONT (백분위수, Lakehouse v2)"
description: PERCENTILE_CONT — 연속 분포를 기준으로 보간된 백분위수 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

연속 분포를 기준으로 보간된 백분위수 값을 반환합니다.

## Analyze 구문

```python
func.percentile_cont(<percentile>)
```

## Analyze 예제

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## SQL 구문

```sql
PERCENTILE_CONT(<percentile>)
```

## SQL 예제

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
