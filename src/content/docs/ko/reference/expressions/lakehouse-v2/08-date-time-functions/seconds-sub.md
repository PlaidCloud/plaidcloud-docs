---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB — 날짜/시간 값에서 지정한 초 수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

날짜/시간 값에서 지정한 초 수를 뺍니다.

## Analyze 구문

```python
func.seconds_sub(<datetime>, <n>)
```

## Analyze 예제

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
SECONDS_SUB(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
