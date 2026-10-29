---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB — 날짜/시간 값에서 지정한 마이크로초 수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

날짜/시간 값에서 지정한 마이크로초 수를 뺍니다.

## Analyze 구문

```python
func.microseconds_sub(<datetime>, <n>)
```

## Analyze 예제

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## SQL 예제

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
