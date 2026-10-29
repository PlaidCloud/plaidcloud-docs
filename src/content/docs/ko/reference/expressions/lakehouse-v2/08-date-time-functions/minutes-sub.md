---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — 날짜/시간 값에서 지정한 분 수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

날짜/시간 값에서 지정한 분 수를 뺍니다.

## Analyze 구문

```python
func.minutes_sub(<datetime>, <n>)
```

## Analyze 예제

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
MINUTES_SUB(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
