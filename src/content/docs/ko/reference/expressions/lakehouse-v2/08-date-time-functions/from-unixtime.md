---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME — Unix 타임스탬프를 날짜/시간 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

Unix 타임스탬프를 날짜/시간 문자열로 변환합니다.

## Analyze 구문

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Analyze 예제

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## SQL 예제

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
