---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB — 날짜/시간에서 지정한 시간 수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

날짜/시간에서 지정한 시간 수를 뺍니다.

## Analyze 구문

```python
func.hours_sub(<datetime>, <n>)
```

## Analyze 예제

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
HOURS_SUB(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
