---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT — 형식 문자열에 따라 시간 값의 형식을 지정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

형식 문자열에 따라 시간 값의 형식을 지정합니다.

## Analyze 구문

```python
func.time_format(<time>, <format>)
```

## Analyze 예제

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## SQL 구문

```sql
TIME_FORMAT(<time>, <format>)
```

## SQL 예제

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```
